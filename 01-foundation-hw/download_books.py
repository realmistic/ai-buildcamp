import csv
import os
import requests
import io
from urllib.parse import urlparse

def download_books(csv_url='https://raw.githubusercontent.com/alexeygrigorev/ai-engineering-buildcamp-code/main/01-foundation/homework/books.csv', output_dir='books'):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created directory: {output_dir}")

    print(f"Fetching books list from {csv_url}...")
    try:
        response = requests.get(csv_url)
        response.raise_for_status()
        csv_content = io.StringIO(response.text)
        
        reader = csv.DictReader(csv_content)
        
        for row in reader:
            title = row.get('title')
            pdf_url = row.get('pdf_url')
            
            if not title or not pdf_url:
                continue

            # Extract filename from URL
            parsed_url = urlparse(pdf_url)
            filename = os.path.basename(parsed_url.path)
            
            # Fallback if filename is empty or invalid
            if not filename or filename == '.':
                filename = f"{title.replace(' ', '_')}.pdf"

            output_path = os.path.join(output_dir, filename)
            
            if os.path.exists(output_path):
                print(f"File {filename} already exists. Skipping download.")
                continue
            
            print(f"Downloading '{title}' from {pdf_url}...")
            
            try:
                pdf_response = requests.get(pdf_url, stream=True)
                pdf_response.raise_for_status()
                
                with open(output_path, 'wb') as pdf_file:
                    for chunk in pdf_response.iter_content(chunk_size=8192):
                        pdf_file.write(chunk)
                
                print(f"Saved to {output_path}")
            except requests.exceptions.RequestException as e:
                print(f"Failed to download '{title}': {e}")
                
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch CSV file: {e}")