# Data Ingestion Pipeline (Local Version)

A simple Python script that:
- Takes a file URL (e.g., CSV)
- Downloads and validates the file
- Simulates uploading to AWS S3
- Logs the action locally in `upload_log.json`

---

## Technologies Used

- Python 3
- `requests` – For downloading files
- `json` – For logging
- `datetime` – For timestamping actions

---

## How It Works

1. You pass a URL pointing to a `.csv` or `.txt` file.
2. The script downloads the file.
3. It validates:
   - Extension (only `.csv`, `.txt`)
   - Size (≤ 10MB)
4. Simulates upload to AWS S3
5. Logs details in `upload_log.json`

---

##  Example

```bash
python ingest.py https://people.sc.fsu.edu/~jburkardt/data/csv/addresses.csv


##Screenshot

Here’s an example of the pipeline running locally:

![Pipeline Output](images/screenshot.png)
