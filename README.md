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
# Legal Document Sorter

A Python automation tool that organizes legal documents into folders based on file type. It helps law firms reduce manual filing time, keep documents organized, and track file movements.

## File Categories

| Folder | File Types |
|---|---|
| Contracts | `.docx`, `.doc` |
| Evidence | `.jpg`, `.jpeg`, `.png` |
| Filings | `.pdf` |
| Correspondence | `.txt`, `.eml` |
| Other | All remaining files |

## How to Run

Requires Python 3.10 or newer.

```powershell
python sort_documents.py "C:\path\to\your\documents"
```

The script creates the folders automatically and records every move, timestamp, original path, and destination path in `sort_log.txt`.

## Testing

Run the automated tests:


# Job Market Scraper

A Python web-scraping tool that collects structured information from a practice website and saves it to CSV.

The practice website contains quotes, not job adverts. It demonstrates the techniques needed to build an authorised job-market monitoring tool.

## Extracted Fields

- Quote text
- Author
- Tags
- Author profile URL
- Source URL
- Date and time collected

## Installation

Requires Python 3.10 or newer.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run the Scraper

```powershell
python scraper.py
```

The output is saved as `quotes.csv`.

To control the number of pages:

```powershell
python scraper.py --pages 3 --delay 1.5
```

## Testing

```powershell
python -m unittest discover -s tests -v
```

<<<<<<< HEAD
Tested successfully with 11 dummy files and 2 automated tests.

## Business Value

- **Target users:** Small law firms and legal offices.
- **Time saved:** Approximately 1 hour per week when sorting 200 files.
- **Setup price:** KES 8,000 (one-time).

## Technology

Python, pathlib, shutil, argparse, and datetime.

**Note:** Test on copies before sorting actual client documents. The tool sorts by file extension and does not upload or read document contents.
=======
## Adapting for an HR Consultancy

With written client approval, the scraper can be adapted to an authorised jobs board.

Potential fields:

- Job title
- Company name
- Job location
- Salary range
- Posting date
- Job listing URL

The script's HTML selectors would be updated to match the jobs board. Salary values would be cleaned and standardised, duplicate listings removed, and results exported into a weekly Excel or CSV report.

## Ethical and Legal Considerations

Before scraping a live website:

1. Obtain written permission and confirm the client is authorised to collect the information.
2. Review the website's terms of service, robots.txt, API terms and applicable restrictions.
3. Check Kenya's Data Protection Act, 2019 and relevant ODPC guidance where personal data is involved.
4. Collect only information necessary for the agreed business purpose.
5. Avoid collecting candidate names, CVs and contact details unless specifically authorised and legally justified.
6. Use reasonable request delays and respect access restrictions.
7. Agree on data security, report recipients and retention periods.

Publicly accessible information is not automatically free to reuse. Seek legal advice where necessary.

This project is a technical demonstration, not legal advice.

## Pricing Proposal

Suggested HR consultancy pricing:

| Service | Price |
|---|---:|
| One-time setup | KES 12,000 |
| Monthly retainer | KES 18,000 |

Setup includes one approved source, field configuration, testing and report template.

The monthly retainer includes:
- Weekly scraping
- Data cleaning and duplicate removal
- CSV/Excel report delivery
- Brief job-market trend summary
- Basic maintenance

Assumed scope: up to three approved sources and ten agreed search terms. Complex dashboards, additional sources and major website changes are quoted separately.

## Technology

Python, Requests, Beautiful Soup, CSV and unittest.
>>>>>>> 75377ff (Web scrapping Tool)
