
import os
from dotenv import load_dotenv
import anthropic

# Load API key
load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")

if not api_key:
    raise ValueError("Add ANTHROPIC_API_KEY to your .env file.")

# Initialize Claude Haiku 4.5
client = anthropic.Anthropic(api_key=api_key)

MODEL = "claude-haiku-4-5"

SYSTEM_PROMPT = """
You are a concise FAQ assistant for a matatu SACCO in Thika, Kenya.

Answer only questions about member balances, meetings, and membership fees.

APPROVED DEMONSTRATION ANSWERS

1. MEMBER BALANCE
Individual balances must be confirmed with the SACCO treasurer.
Members should provide their member number.
Never invent a member's balance.

2. NEXT MEETING
Date: Saturday, 7 November 2026.
Time: 10:00 AM.
Venue: SACCO office, Thika.
Tell members to confirm the schedule with the secretary.

3. MEMBERSHIP FEES
Joining fee: KES 2,000.
Monthly membership fee: KES 500.
Tell members to confirm the fees with the secretary before paying.

RULES
- Recognize different ways of asking the same question.
- Give short, direct answers in plain English.
- Never invent balances, fees, dates, or other information.
- For unrelated questions, reply:
  "Please contact the SACCO secretary for assistance."
"""


def answer_question(question):
    """Get a focused FAQ answer from Claude Haiku 4.5."""

    response = client.messages.create(
        model=MODEL,
        max_tokens=150,
        system=SYSTEM_PROMPT,
        messages=[
            {
                "role": "user",
                "content": question
            }
        ]
    )

    for block in response.content:
        if block.type == "text":
            return block.text.strip()

    return "Sorry, please contact the SACCO secretary."


def run_tests():
    """Test six ways members might ask the FAQs."""

    questions = [
        "What is my balance?",
        "How much do I owe?",
        "When is our next meeting?",
        "What time is the SACCO meeting?",
        "How much is the joining fee?",
        "What is the monthly membership fee?"
    ]

    for question in questions:
        print(f"\nQuestion: {question}")

        try:
            print("Answer:", answer_question(question))
        except anthropic.APIError as error:
            print("API error:", error)


def main():
    print("MATATU SACCO FAQ ASSISTANT")
    print("Ask about balances, meetings, or membership fees.")
    print("Type 'test' to test the questions or 'quit' to exit.")

    while True:
        question = input("\nMember question: ").strip()

        if question.lower() == "quit":
            print("Goodbye!")
            break

        if question.lower() == "test":
            run_tests()
            continue

        if not question:
            print("Please enter a question.")
            continue

        try:
            print("\nAnswer:", answer_question(question))
        except anthropic.APIError as error:
            print(f"Claude API error: {error}")


if __name__ == "__main__":
    main()
