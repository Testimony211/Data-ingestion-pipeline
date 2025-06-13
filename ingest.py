import requests
import os
import json
from datetime import datetime

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
        "timestamp": datetime.utcnow().isoformat()
    }
    with open("upload_log.json", "a") as log_file:
        log_file.write(json.dumps(log_data) + "\n")

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

def main():
    url = input("Enter URL to download: ").strip()
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
