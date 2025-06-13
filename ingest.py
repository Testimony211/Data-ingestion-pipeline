import requests
import os
import json
from datetime import datetime, timezone
import argparse

# === Configuration ===
MAX_FILE_SIZE_MB = 10
ALLOWED_EXTENSIONS = ['.csv', '.txt']

def is_valid_file(file_path):
    if not any(file_path.endswith(ext) for ext in ALLOWED_EXTENSIONS):
        return False
    file_size_mb = os.path.getsize(file_path) / (1024 * 1024)
    return file_size_mb <= MAX_FILE_SIZE_MB

def log_upload(file_name, url):
    log_data = {
        "file_name": file_name,
        "url": url,
        "timestamp": datetime.now(timezone.utc).isoformat()
    }
    with open("upload_log.json", "a") as log_file:
        log_file.write(json.dumps(log_data) + "\n")

import time  # Add this at the top if not already imported

def download_file(url, retries=3, delay=2):
    file_name = url.split("/")[-1]

    for attempt in range(1, retries + 1):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            with open(file_name, 'wb') as f:
                f.write(response.content)
            print(f"✅ Downloaded: {file_name}")
            return file_name

        except Exception as e:
            print(f"❌ Attempt {attempt} failed: {e}")
            if attempt < retries:
                print(f"🔁 Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                print("🚫 All retry attempts failed.")

    return None

def download_file(url):
    file_name = url.split("/")[-1]
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(file_name, 'wb') as f:
            f.write(response.content)
        print(f"✅ Downloaded: {file_name}")
        return file_name
    except Exception as e:
        print(f"❌ Error downloading file: {e}")
        return None

def parse_args():
    parser = argparse.ArgumentParser(description="Download and log a file from a URL")
    parser.add_argument("url", help="URL of the file to download")
    return parser.parse_args()

def main():
    args = parse_args()
    url = args.url
    file_name = download_file(url)

    if not file_name:
        return

    if not is_valid_file(file_name):
        print("❌ Invalid file. Must be CSV/TXT and <= 10MB.")
        return

    print("📤 Simulating upload to S3 bucket...")
    print(f"📁 s3://your-bucket-name/{file_name} [SIMULATED]")

    log_upload(file_name, url)
    print("📝 Upload logged in 'upload_log.json'")

if __name__ == "__main__":
    main()
import argparse

def main():
    parser = argparse.ArgumentParser(
        description="📥 Download a file from a URL, validate it, simulate an S3 upload, and log the action."
    )
    parser.add_argument(
        "url",
        type=str,
        help="🔗 URL of the file to download (must be .csv or .txt and <= 10MB)"
    )
    args = parser.parse_args()

    url = args.url
    file_name = download_file(url)

    if not file_name:
        print("🚫 File download failed.")
        return

    if not is_valid_file(file_name):
        print("❌ Invalid file. Must be CSV/TXT and <= 10MB.")
        return

    print("📤 Simulating upload to S3 bucket...")
    print(f"📁 s3://your-bucket-name/{file_name} [SIMULATED]")

    log_upload(file_name, url)
    print("📝 Upload logged in 'upload_log.json'")
    print("✅ All done!")

if __name__ == "__main__":
    main()
