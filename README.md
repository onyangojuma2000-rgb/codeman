<<<<<<< HEAD

# Dairy Co-op Price Checker

A simple Python command-line tool for calculating the amount owed to dairy farmers.

## Requirements
- Python 3.9 or newer
- No additional packages required

## How to run

Open a terminal in this project folder and run:

```bash
python dairy_calculator.py
```

## Update the milk price

Open `price.txt` and replace the existing number with the new buying price per litre.

Example:

```text
58.5
```

Save the file and run the program again.

## Calculation

Total owed = Litres supplied × Current price per litre

## Current limitations

This version calculates the amount owed but does not save daily milk deliveries, farmer records, or payment history.
=======
<<<<<<< HEAD
# codeman
Working on a project

#app.py
# Carpentry Workshop Daily Production Log

A simple Streamlit app for recording daily chair production and material usage.

## Run locally

1. Install Python.
2. Open Command Prompt/PowerShell in this folder.
3. Run:

```bash
pip install -r requirements.txt
streamlit run app.py
```

The app lets you:
- Add daily workshop records
- Calculate total chairs, timber, nails and paint
- Calculate daily averages
- View a production chart
- Download records as CSV
- Reset the sample data
=======
# Kenyan Business Currency Tracker

A Python application that converts Kenyan Shillings (KES) to US Dollars (USD), Euros (EUR), and British Pounds (GBP) using ExchangeRate-API.

## Features
- Converts KES to USD, EUR, and GBP.
- Retrieves current exchange rates from the API.
- Validates user input and handles common errors.
- Uses environment variables to protect API credentials.

## Requirements
- Python 3.10+
- ExchangeRate-API key

## Setup

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Create a `.env` file using `.env.example` as a template.
3. Add your API key:

   ```text
   EXCHANGE_RATE_API_KEY=your_api_key
   ```

## Run

```bash
python currency_tracker.py
```

Enter an amount in KES to view the converted values.

## Security
Never share or commit your `.env` file or API key to GitHub.

**Note:** Exchange rates may change. Results depend on the rates provided by the API when the application runs.
link explaininng project structure: kenyan_business_currency_tracker/
│
├── currency_tracker.py
├── README.md
├── requirements.txt
├── .env.example
└── .gitignore
>>>>>>> b3ba95a (Readme file for currency tracker)
>>>>>>> 97512283f667febf9b9fd6ee943ad86edec540e3
