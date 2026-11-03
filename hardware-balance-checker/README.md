# Hardware Shop Credit Balance Checker

A simple Flask web app that allows an Eldoret hardware shop to search for a customer and view their outstanding credit balance in KES.

## Features
- Search customers by name.
- Display outstanding balances in KES.
- Case-insensitive name search.
- JSON API response.
- Handles missing and unknown customers.

## Installation

```bash
pip install -r requirements.txt
python hardware.py
```

Open: http://127.0.0.1:5000/

## Test the API

```text
http://127.0.0.1:5000/api/balance?name=John%20Kamau
```

## Sample Customers
Five sample customers with hardcoded balances are included in `app.py`.

## Tools
Python | Flask | HTML | JavaScript | JSON

**Estimated Development Charge: KES 6,000 (one-time fee).**

*Note: This is a demonstration version. A database and authentication are recommended for real business use.*