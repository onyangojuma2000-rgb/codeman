"""
Dairy Co-op Payment Calculator
-------------------------------
Farmer enters their name and litres supplied.
Tool shows total owed at the current buying price.

Usage:
    python dairy_calculator.py

Config:
    Update the current buying price in price.txt.
    The file should contain only a number, e.g. 55.0.
"""

import math
from pathlib import Path

PRICE_FILE = Path(__file__).with_name("price.txt")
DEFAULT_PRICE = 55.0


def get_current_price():
    """Read current price from price.txt, fall back to default."""
    try:
        price = float(PRICE_FILE.read_text(encoding="utf-8").strip())

        if price <= 0:
            raise ValueError("Price must be greater than zero.")

        return price

    except FileNotFoundError:
        print("Warning: price.txt was not found.")
    except ValueError:
        print("Warning: price.txt contains an invalid price.")
    except OSError:
        print("Warning: price.txt could not be read.")

    print(f"Using default price: KES {DEFAULT_PRICE:.2f}")
    return DEFAULT_PRICE


def calculate_payment(litres, price_per_litre):
    """Calculate the total amount owed to the farmer."""
    return litres * price_per_litre


def run():
    print("Kiambu Dairy Co-op Payment Calculator")
    print("---------------------------------------")

    price = get_current_price()
    print(f"Current buying price: KES {price:.2f} per litre")
    print()

    name = input("Farmer name: ").strip()

    if not name:
        print("Name is required.")
        return

    try:
        litres = float(input("Litres supplied today: "))

        if litres <= 0:
            print("Litres must be greater than zero.")
            return

    except ValueError:
        print("Please enter a valid number for litres.")
        return

    total = calculate_payment(litres, price)

    print()
    print("Payment Summary")
    print("---------------")
    print(f"Farmer: {name}")
    print(f"Litres: {litres:.2f}")
    print(f"Price: KES {price:.2f}/litre")
    print(f"Total: KES {total:,.2f}")


if __name__ == "__main__":
    run()