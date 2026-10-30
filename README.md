# Matatu SACCO FAQ Assistant

A Python AI assistant powered by **Claude Haiku 4.5** that helps a Thika Matatu SACCO secretary answer common member questions about balances, meetings, and membership fees.

## Features
- Answers common questions clearly and consistently.
- Recognizes different ways of asking the same question.
- Includes six sample questions for testing.

## Setup

Install dependencies:

```bash
python -m pip install anthropic python-dotenv
```

Create a `.env` file and add your Anthropic API key:

```text
ANTHROPIC_API_KEY=your_api_key_here
```

## Run

```bash
python sacco_faq_assistant.py
```

Type a question, `test` to run sample questions, or `quit` to exit.

## Example Interactions

**Member:** What is my balance?

**Assistant:** Please contact the SACCO treasurer to confirm your balance.

**Member:** When is our next meeting?

**Assistant:** The demonstration schedule lists Saturday, 7 November 2026, at 10:00 AM at the SACCO office in Thika. Please confirm with the secretary.

**Member:** How much is the monthly fee?

**Assistant:** The demonstration monthly membership fee is KES 500. Please confirm the amount with the secretary before paying.

## Important Notes
- Replace demonstration fees (KES 2,000 joining; KES 500 monthly) and meeting details with SACCO-approved information.
- Individual balances must be verified by the treasurer.
- Requires internet access and a valid Anthropic API key; API charges may apply.
- Runs in the terminal; automatic WhatsApp integration is not included.
- Keep `.env` private and exclude it from GitHub.

**Technology:** Python · Claude Haiku 4.5 · Anthropic API

# Matatu SACCO FAQ Assistant

A Python AI assistant powered by **Claude Haiku 4.5** that helps a Thika Matatu SACCO secretary answer common member questions about balances, meetings, and membership fees.

## Features
- Answers common questions clearly and consistently.
- Recognizes different ways of asking the same question.
- Includes six sample questions for testing.

## Setup

Install dependencies:

```bash
python -m pip install anthropic python-dotenv
```

Create a `.env` file and add your Anthropic API key:

```text
ANTHROPIC_API_KEY=your_api_key_here
```

## Run

```bash
python sacco_faq_assistant.py
```

Type a question, `test` to run sample questions, or `quit` to exit.

## Example Interactions

**Member:** What is my balance?

**Assistant:** Please contact the SACCO treasurer to confirm your balance.

**Member:** When is our next meeting?

**Assistant:** The demonstration schedule lists Saturday, 7 November 2026, at 10:00 AM at the SACCO office in Thika. Please confirm with the secretary.

**Member:** How much is the monthly fee?

**Assistant:** The demonstration monthly membership fee is KES 500. Please confirm the amount with the secretary before paying.

## Important Notes
- Replace demonstration fees (KES 2,000 joining; KES 500 monthly) and meeting details with SACCO-approved information.
- Individual balances must be verified by the treasurer.
- Requires internet access and a valid Anthropic API key; API charges may apply.
- Runs in the terminal; automatic WhatsApp integration is not included.
- Keep `.env` private and exclude it from GitHub.

**Technology:** Python · Claude Haiku 4.5 · Anthropic API
