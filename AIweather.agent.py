
"""
Kericho Tea Harvesting Agent
----------------------------
A command-line AI agent that checks weather conditions
and provides practical tea-harvesting recommendations.

Install:
    python -m pip install anthropic python-dotenv requests

Run:
    python tea_agent.py
"""

import os
import json
import requests
import anthropic

from datetime import datetime
from dotenv import load_dotenv


# 1. Load API key
load_dotenv()

API_KEY = os.getenv("ANTHROPIC_API_KEY")

if not API_KEY:
    raise ValueError(
        "ANTHROPIC_API_KEY is missing. Add it to your .env file."
    )

client = anthropic.Anthropic(api_key=API_KEY)

MODEL = "claude-haiku-4-5"


# 2. Kericho location and weather API
LATITUDE = 0.3676
LONGITUDE = 35.2834

WEATHER_URL = "https://api.open-meteo.com/v1/forecast"


# 3. Weather tool function
def get_kericho_weather():
    """Retrieve current and next six hours of weather."""

    params = {
        "latitude": LATITUDE,
        "longitude": LONGITUDE,
        "current": (
            "temperature_2m,"
            "relative_humidity_2m,"
            "precipitation,"
            "rain"
        ),
        "hourly": (
            "temperature_2m,"
            "relative_humidity_2m,"
            "precipitation,"
            "precipitation_probability"
        ),
        "forecast_hours": 8,
        "timezone": "Africa/Nairobi",
    }

    response = requests.get(
        WEATHER_URL,
        params=params,
        timeout=20
    )

    response.raise_for_status()

    data = response.json()

    current = data["current"]
    hourly = data["hourly"]

    # Identify the next six forecast hours
    current_time = current["time"]
    current_datetime = datetime.fromisoformat(current_time)

    start_index = next(
        (
            i for i, forecast_time in enumerate(hourly["time"])
            if datetime.fromisoformat(forecast_time) > current_datetime
        ),
        None
    )

    if start_index is None:
        raise ValueError("No upcoming hourly forecast data available.")

    next_hours = []

    for i in range(start_index, min(start_index + 6, len(hourly["time"]))):

        next_hours.append({
            "time": hourly["time"][i],
            "temperature": hourly["temperature_2m"][i],
            "humidity": hourly["relative_humidity_2m"][i],
            "rainfall_mm": hourly["precipitation"][i],
            "rain_probability": hourly[
                "precipitation_probability"
            ][i]
        })

    if len(next_hours) < 6:
        raise ValueError("Weather API returned fewer than six forecast hours.")

    return {
        "location": "Kericho, Kenya",
        "current_time": current_time,
        "current_temperature": current["temperature_2m"],
        "current_humidity": current["relative_humidity_2m"],
        "current_rainfall_mm": current["precipitation"],
        "current_rain_mm": current["rain"],
        "next_six_hours": next_hours
    }


# 4. Define the weather tool for Claude
TOOLS = [
    {
        "name": "get_kericho_weather",
        "description": (
            "Gets current weather and the next six hours of "
            "temperature, humidity and rainfall in Kericho, Kenya. "
            "Use this tool when the user asks about harvesting, "
            "weather conditions or whether today is suitable for harvesting."
        ),
        "input_schema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    }
]


# 5. System prompt

SYSTEM_PROMPT = """
You are the official Weather and Tea Operations Assistant
for a tea estate in Kericho, Kenya.

SCOPE OF RESPONSIBILITY
You are ONLY allowed to answer questions related to:
1. Current weather conditions in Kericho.
2. Weather forecasts and expected rainfall.
3. Temperature, humidity and other weather conditions.
4. Tea harvesting recommendations.
5. Tea farming and tea estate operations.
6. Tea harvesting equipment and field practices.
7. Weather-related planning for tea workers.

OUT-OF-SCOPE QUESTIONS
- Do not answer questions unrelated to weather,
  tea farming or Kericho tea estate operations.
- Do not answer general knowledge, politics,
  entertainment, coding, financial or unrelated questions.
- Politely decline unrelated questions.
- Use this response:
  "I can only assist with Kericho weather information
  and tea estate operations. Please ask a relevant question."

WEATHER TOOL RULES
- Call get_kericho_weather whenever the user asks about
  current weather, forecasts or harvesting conditions.
- Do not call the weather tool for general tea farming
  or tea operations questions that do not require weather.
- Never invent weather readings.
- If weather information is unavailable, say so clearly.

TEA HARVESTING RULES

GOOD CONDITIONS:
- No rain expected in the next six hours.
- Temperature between 15°C and 25°C.
- Relative humidity below 70%.

BAD CONDITIONS:
- Active rainfall.
- Temperature above 28°C.

RECOMMENDATIONS:
- Recommend HARVEST when all good conditions are met.
- Recommend DELAY when there is active rain or
  temperatures exceed 28°C.
- Recommend PROCEED WITH CAUTION when conditions
  are mixed or less favourable.
- Temperatures above 25°C and up to 28°C are
  less favourable.
- Humidity of 70% or higher is not considered low.
- Explain the reasons behind every recommendation.

RESPONSE STYLE
- Use simple, professional and practical language.
- Keep responses brief and relevant.
- Give recommendations suitable for field supervisors.
- Do not provide medical, legal or unrelated advice.
- Never claim that a forecast guarantees actual conditions.
"""


# 6. Agent function with tool execution
def ask_agent(question):
    """Process a question and execute the weather tool if requested."""

    messages = [
        {"role": "user", "content": question}
    ]

    response = client.messages.create(
        model=MODEL,
        max_tokens=600,
        system=SYSTEM_PROMPT,
        tools=TOOLS,
        messages=messages
    )

    # Execute tools whenever Claude requests them
    while response.stop_reason == "tool_use":

        messages.append({
            "role": "assistant",
            "content": response.content
        })

        tool_results = []

        for block in response.content:

            if block.type == "tool_use":

                if block.name == "get_kericho_weather":

                    print("\n[Weather tool called]")

                    try:
                        result = get_kericho_weather()

                        print("[Weather data retrieved successfully]")

                        is_error = False

                    except (
                        requests.RequestException,
                        KeyError,
                        ValueError,
                        StopIteration
                    ) as error:

                        result = {
                            "error": (
                                "Weather information is unavailable. "
                                "The supervisor should check again later."
                            )
                        }

                        is_error = True

                        print(f"[Weather error: {error}]")

                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": json.dumps(result),
                        "is_error": is_error
                    })

        if not tool_results:
            break

        messages.append({
            "role": "user",
            "content": tool_results
        })

        response = client.messages.create(
            model=MODEL,
            max_tokens=600,
            system=SYSTEM_PROMPT,
            tools=TOOLS,
            messages=messages
        )

    return "".join(
        block.text
        for block in response.content
        if block.type == "text"
    ).strip()


# 7. Test the agent with three questions
def run_tests():

    test_questions = [
        "Is today good for harvesting tea?",
        "What are the benefits of harvesting tea early in the morning?",
        "What equipment should tea field workers carry?"
    ]

    print("\nRUNNING AGENT TESTS")
    print("=" * 45)

    for number, question in enumerate(test_questions, start=1):

        print(f"\nTEST {number}")
        print(f"Question: {question}")

        try:
            answer = ask_agent(question)
            print(f"\nAgent: {answer}")

        except anthropic.APIError as error:
            print(f"API error: {error}")

        except Exception as error:
            print(f"Unexpected error: {error}")

        print("-" * 45)


# 8. Command-line interface
def main():

    print("=" * 45)
    print("   KERICHO TEA HARVESTING AGENT")
    print("=" * 45)

    print("Ask questions about harvesting and weather.")
    print("Commands: /test to run tests, /quit to exit.")
    print("-" * 45)

    while True:

        try:
            question = input("\nSupervisor: ").strip()

        except (EOFError, KeyboardInterrupt):
            print("\nAgent closed. Goodbye!")
            break

        if not question:
            continue

        if question.lower() == "/quit":
            print("Agent closed. Goodbye!")
            break

        if question.lower() == "/test":
            run_tests()
            continue

        try:
            answer = ask_agent(question)

            print("\nTea Harvesting Agent:")
            print(answer)

        except anthropic.APIError as error:
            print(f"Anthropic API error: {error}")

        except Exception as error:
            print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()
