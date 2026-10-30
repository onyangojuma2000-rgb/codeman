# Property Inquiry Extractor

A Python AI-powered tool that extracts structured property requirements from WhatsApp inquiries using **Claude Haiku 4.5**.

## Features
- Extracts property type and number of bedrooms.
- Identifies the requested location.
- Extracts rental or purchase budgets in KES.
- Identifies whether the customer wants to rent or buy.
- Handles missing information using `null`.
- Includes three sample test inquiries.

## Requirements
- Python 3.10+
- Anthropic API key
- Internet connection

## Installation

Install the required packages:

```bash
python -m pip install anthropic python-dotenv
```

Create a `.env` file in the project directory:

```text
ANTHROPIC_API_KEY=your_api_key_here
```

## Run the Script

```bash
python property_inquiry_extractor.py
```

Choose an option:
- `1` – Enter a customer inquiry.
- `2` – Run the three sample tests.

## Example Input

> I am looking for a 3-bedroom house in Kileleshwa, budget around 80k per month.

## Expected Output

```text
Extracted Property Details
------------------------------
Property type : house
Bedrooms      : 3
Location      : Kileleshwa
Budget (KES)  : 80000
Purpose       : rental
```

## Tools
Python | Claude Haiku 4.5 | Anthropic API | JSON | python-dotenv

## Notes
- Missing or unspecified information is returned as `null`.
- Requires a valid Anthropic API key; API charges may apply.
- This version runs in the terminal and does not automatically connect to WhatsApp or a property database.
- Keep your `.env` file private and exclude it from GitHub.