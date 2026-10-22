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
