
"""
Kenyan Business Currency Tracker
--------------------------------
Converts an amount in Kenyan shillings (KES) into USD, EUR, and GBP
using ExchangeRate-API.

Requirements:
    pip install requests python-dotenv

Configuration:
    Add EXCHANGE_RATE_API_KEY to your .env file.

Usage:
    python currency_tracker.py
"""

import os
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from urllib import response

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("EXCHANGE_RATE_API_KEY")
API_URL = (
    f"https://v6.exchangerate-api.com/v6/"
    f"{API_KEY}/latest/KES"
)

TARGET_CURRENCIES = {
    "USD": "US Dollar",
    "EUR": "Euro",
    "GBP": "British Pound",
}


def get_exchange_rates():
    """Fetch current KES exchange rates from the API."""
    if not API_KEY:
        raise ValueError(
            "API key missing. Add it to your .env file."
        )

    response = requests.get(API_URL, timeout=15)
    response.raise_for_status()

    data = response.json()

    if data.get("result") != "success":
        raise ValueError(
            f"Exchange API error: {data.get('error-type', 'Unknown error')}"
        )

    if data.get("base_code") != "KES":
        raise ValueError("Unexpected base currency returned.")

    rates = data.get("conversion_rates", {})

    for currency in TARGET_CURRENCIES:
        if currency not in rates:
            raise ValueError(f"Missing exchange rate: {currency}")

    return rates, data.get("time_last_update_utc", "Unknown")




def convert_currency(amount, rate):
    """Convert an amount and round it to two decimal places."""
    converted = amount * Decimal(str(rate))
    return converted.quantize(
        Decimal("0.01"),
        rounding=ROUND_HALF_UP
    )


def main():
    print("\nKENYAN BUSINESS CURRENCY TRACKER")
    print("=" * 38)

    try:
        amount = Decimal(input("Enter amount in KES: ").strip())

        if not amount.is_finite() or amount <= 0:
            print("Please enter a positive, valid amount.")
            return

        rates, last_updated = get_exchange_rates()

        print(f"\nKES {amount:,.2f} converts approximately to:")
        print("-" * 38)

        for currency, name in TARGET_CURRENCIES.items():
            result = convert_currency(amount, rates[currency])
            print(f"{currency} ({name}): {result:,.2f}")

        print(f"\nRate data last updated: {last_updated}")
        print("Note: Actual bank or payment-provider rates may differ.")

    except InvalidOperation:
        print("Invalid amount. Enter a number, e.g. 10000 or 2500.50.")

    except requests.exceptions.Timeout:
        print("Request timed out. Check your internet and try again.")

    except requests.exceptions.RequestException as error:
        print(f"Network/API request failed: {error}")

    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
