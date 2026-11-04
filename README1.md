# Kiambu Poultry Egg Production Tracker

A simple Flask REST API that helps poultry farmers record daily egg production across multiple sheds and automatically calculate production totals.

## Features

- Record daily egg production by shed.
- Retrieve all production records.
- Calculate total eggs produced.
- View production totals per shed.
- Validate dates, shed names, and egg counts.

## Tools

- Python
- Flask
- REST API
- JSON

## Installation

```bash
git clone <your-repository-url>
cd poultry-egg-tracker

python -m venv venv
```

Activate the virtual environment:

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install Flask
```

Run the application:

```bash
python app.py
```

API base URL: `http://127.0.0.1:5000`

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| POST | `/api/eggs` | Record daily egg production |
| GET | `/api/eggs` | Retrieve records and production totals |

### Sample POST Request

```json
{
    "shed": "Shed A",
    "date": "2026-11-04",
    "count": 120
}
```

## Pricing Estimate

| Service | Proposed charge |
|---|---:|
| Development and deployment (one-time) | **KES 15,000** |
| Monthly maintenance and support | **KES 2,000** |

*The one-time fee covers setup, testing, and deployment. Monthly support covers basic monitoring, troubleshooting, and minor maintenance. Hosting fees and major feature upgrades are charged separately.*

## Storage Limitation

Records are stored temporarily in memory and are lost when the application restarts. Database integration is recommended for permanent storage.

## Future Improvements

- Weekly and monthly production reports.
- Database integration.
- Farmer-friendly dashboard.
- Excel report exports.