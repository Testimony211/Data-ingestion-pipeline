# Data Ingestion Pipeline (Local Version)

This is a simple script that:
- Takes a file URL (e.g., CSV)
- Downloads and validates the file
- Simulates uploading to AWS S3
- Logs the action locally in `upload_log.json`

## Technologies
- Python
- requests
- json
- datetime

## Usage

```bash
python3 ingest.py
