"""
Kisumu Pharmacy Chatbot
-----------------------
a command_line assistant for pharmacy staff.

Install:
 Python -m pip install anthropic python-dotenv

Run:
python pharmacy_chatbot.py
"""
import os
import anthropic
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ANTHROPIC_API_KEY")

if not API_KEY:
    raise ValueError(
        "ANTHROPIC_API_KEY is missing. Add it to your .env file."
    )

client = anthropic.Anthropic(api_key=API_KEY)

MODEL = "claude-haiku-4-5"
SYSTEM_PROMPT = """
You are the staff support chatbot for Kisumu Pharmacy in Kisumu, Kenya.

PHARMACY HOURS
- Monday to Saturday: 8:00 AM to 8:00 PM
- Sunday: 10:00 AM to 4:00 PM

SERVICES
Kisumu Pharmacy provides the following services, subject to staff
availability and professional assessment:
1. Prescription dispensing.
2. Over-the-counter medicine sales.
3. Prescription refill assistance.
4. Blood pressure checks.
5. Blood glucose screening.
6. Medicine-use information and counselling by a qualified pharmacist.
7. General enquiries about medicine availability.
8. Guidance on prescription requirements.

RULES FOR ANSWERING
- Answer clearly, politely, and consistently.
- Use the stated opening hours when answering hours questions.
- Never claim a specific medicine is in stock unless verified by staff.
- Never invent prescription processing times. Explain that timing depends
  on prescription review, medicine availability, and workload. Staff
  should confirm the estimated time.
- For repeat prescriptions, explain that requirements may include the
  previous prescription or refill record and patient identification.
  Requirements vary by medicine and pharmacy policy, so staff must verify
  the exact documents before advising the customer.
- Do not diagnose conditions, prescribe medicines, recommend a dosage,
  or advise customers to start, stop, or change medication.
  Refer clinical questions to the pharmacist.
- Do not invent prices, services, stock levels, or pharmacy policies.
- If information is unavailable, clearly say it must be confirmed by staff.
- Keep track of the conversation. Use earlier messages to understand
  follow-up questions and references such as "it", "that medicine",
  "my prescription", or "how long will it take?"
- Do not ask customers to repeat information already given unless
  clarification is genuinely necessary.
- Treat each new conversation as a separate interaction.
- This chatbot supports pharmacy staff; it does not replace a pharmacist
  or the pharmacy's official records.
"""


def get_reply(conversation_history: list) -> str:
    """Send the conversation history to claude and return its reply."""

    response = client.messages.create(
        model=MODEL,
        max_tokens=500,
        system=SYSTEM_PROMPT,
        messages=conversation_history,
    )

    return "".join(
        block.text
        for block in response.content
        if block.type == "text"
    ).strip()


def main() -> None:
    """Run the command-line chatbot and retain conversation context."""

    conversation_history = []

    print("=" * 45)
    print("   KISUMU PHARMACY CHATBOT")
    print("-" * 45)
    print("Ask about opening hours, services, prescriptions,")
    print("or medicine availability.")
    print("Commands: /reset to start a new conversation, /quit to exit.")
    print("-" * 45)

    while True:
        try:
            user_message = input("\nStaff: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nChatbot closed.")
            break

        if not user_message:
            continue

        if user_message.lower() == "/quit":
            print("Chatbot closed. Goodbye!")
            break

        if user_message.lower() == "/reset":
            conversation_history.clear()
            print("Conversation memory cleared. Start a new conversation.")
            continue

        # Add the new message to the conversation.
        conversation_history.append(
            {"role": "user", "content": user_message}
        )

        try:
            reply = get_reply(conversation_history)
            print(f"\nKisumu Pharmacy Bot: {reply}")

            # Save the assistant reply so future questions have context.
            conversation_history.append(
                {"role": "assistant", "content": reply}
            )

        except anthropic.APIError as error:
            # Remove the unanswered user message so history stays valid.
            conversation_history.pop()
            print(f"API error: {error}")
            print("Please check the connection and API account, then retry.")

        except Exception as error:
            conversation_history.pop()
            print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()

   