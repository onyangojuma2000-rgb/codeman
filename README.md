
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
