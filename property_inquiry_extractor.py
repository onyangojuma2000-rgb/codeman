
"""
Property Inquiry Extractor
--------------------------
Extracts property requirements from raw WhatsApp messages
and returns structured JSON as a Python dictionary.

Requirements:
    python -m pip install anthropic python-dotenv

Setup:
    Add ANTHROPIC_API_KEY to your .env file.
"""

import os
import json
import anthropic
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")

if not api_key:
    raise ValueError(
        "ANTHROPIC_API_KEY is missing. Add it to your .env file."
    )

client = anthropic.Anthropic(api_key=api_key)

MODEL = "claude-haiku-4-5"

SYSTEM_PROMPT = """
You are a property inquiry extraction assistant for a real estate
agent in Nairobi, Kenya.

Extract the following fields from the customer's message:

1. property_type:
   The requested property type, such as house, apartment,
   bedsitter, studio, townhouse, or land. Use null if unknown.

2. bedrooms:
   Number of bedrooms as an integer. Use null if not specified.
   Do not assume the number of bedrooms from the property type.

3. location:
   The requested neighbourhood or location. Preserve the
   location as stated. Use null if unknown.

4. budget_kes:
   The budget in Kenyan shillings (KES) as a number.
   For "under 20k", use 20000 as the maximum budget.
   For "around 80k", use 80000.
   Convert expressions such as "80 thousand" to 80000.
   Use null if no budget is mentioned.
   Do not invent a budget or convert currencies without evidence.

5. rental_or_sale:
   Return "rental" for a property to rent, "sale" for a
   property to buy, or null if the intent is unclear.

Rules:
- Return exactly one valid JSON object.
- Include all five fields.
- Use null for missing or unclear information.
- Do not guess or invent details.
- Do not include Markdown, explanations, or code fences.
"""

def extract_inquiry(message: str) -> dict:
    """Extract property details and return them as a dictionary."""

    response = client.messages.create(
        model=MODEL,
        max_tokens=300,
        system=SYSTEM_PROMPT,
        messages=[
            {
                "role": "user",
                "content": f"Extract the details from this inquiry:\n{message}"
            }
        ],
    )

    response_text = response.content[0].text.strip()

    # Convert the JSON text into a Python dictionary.
    data = json.loads(response_text)

    # Check that the expected fields are present.
    required_fields = [
        "property_type",
        "bedrooms",
        "location",
        "budget_kes",
        "rental_or_sale",
    ]

    for field in required_fields:
        if field not in data:
            raise ValueError(f"Missing field in AI response: {field}")

    return data


def print_inquiry(data: dict) -> None:
    """Print extracted property details clearly."""

    print("\nExtracted Property Details")
    print("-" * 30)
    print(f"Property type : {data['property_type']}")
    print(f"Bedrooms      : {data['bedrooms']}")
    print(f"Location      : {data['location']}")
    print(f"Budget (KES)  : {data['budget_kes']}")
    print(f"Purpose       : {data['rental_or_sale']}")


def run_tests() -> None:
    """Test three different customer inquiries."""

    test_messages = [
        (
            "I am looking for a 3-bedroom house in Kileleshwa, "
            "budget around 80k per month"
        ),
        (
            "Do you have any bedsitters near Westlands under 20k?"
        ),
        (
            "I need a property in Nairobi. Please let me know "
            "what is available."
        ),
    ]

    for number, message in enumerate(test_messages, start=1):
        print(f"\nTEST {number}")
        print(f"Customer message: {message}")

        try:
            result = extract_inquiry(message)
            print_inquiry(result)
        except (json.JSONDecodeError, ValueError) as error:
            print(f"Could not process the AI response: {error}")
        except anthropic.APIError as error:
            print(f"Anthropic API error: {error}")


def main() -> None:
    print("Property Inquiry Extractor")
    print("1. Enter a customer inquiry")
    print("2. Run three test messages")

    choice = input("Choose 1 or 2: ").strip()

    if choice == "1":
        message = input("\nEnter the WhatsApp inquiry: ").strip()

        if not message:
            print("Please enter an inquiry.")
            return

        try:
            result = extract_inquiry(message)
            print_inquiry(result)
        except json.JSONDecodeError:
            print("The AI returned invalid JSON. Please try again.")
        except ValueError as error:
            print(error)
        except anthropic.APIError as error:
            print(f"Anthropic API error: {error}")

    elif choice == "2":
        run_tests()
    else:
        print("Invalid choice. Please select 1 or 2.")


if __name__ == "__main__":
    main()
