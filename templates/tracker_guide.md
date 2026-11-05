# Kiambu Poultry Egg Production Tracker

A simple web-based application built with Python and Flask to help poultry farmers record daily egg production and monitor totals across multiple sheds.

## Features

- Record daily egg production by shed.
- View production records in a browser dashboard.
- Automatically calculate total eggs produced.
- Track production totals per shed.
- Validate dates and egg counts.
- Update the dashboard without reloading the page.

## Tools

- Python and Flask
- HTML and CSS
- JavaScript (`fetch()`)
- JSON

## Installation

1. Clone the repository:

```bash
git clone <your-repository-url>
cd poultry_egg_tracker
```

2. Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Start the application:

```bash
python app.py
```

5. Open `http://127.0.0.1:5000/` in your browser.

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| POST | `/api/eggs` | Record egg production |
| GET | `/api/eggs` | Retrieve records and totals |

## Potential Customers in Kenya

- Small and medium-sized poultry farms.
- Kienyeji egg producers.
- Egg collection and packing businesses.
- Poultry farmer cooperatives.

## Suggested Pricing

| Service | Price |
|---|---:|
| Basic installation and setup | KES 8,000–12,000 |
| Customized version | KES 15,000–25,000 |
| Monthly maintenance | KES 1,000–2,000 |

*Prices are introductory estimates. Hosting and major upgrades are charged separately.*

## Current Limitation

Records are stored temporarily in memory and are lost when the server restarts. Database integration is required for permanent storage.

## Future Improvements

- Database integration.
- Weekly and monthly reports.
- Excel and PDF exports.
- User login and access control.

## Author
Felix Juma
Python Developer | Flask | Web Applications