from fastapi import FastAPI, HTTPException, Query
import os
import requests
import git
import sqlite3
import duckdb
import pandas as pd
import markdown
import whisper
from PIL import Image
from bs4 import BeautifulSoup

data_dir = "/data"  # Restrict operations to this directory

def validate_path(file_path: str):
    """Ensure the file path is within the /data directory."""
    abs_path = os.path.abspath(file_path)
    if not abs_path.startswith(data_dir):
        raise HTTPException(status_code=403, detail="Access to this path is restricted")
    return abs_path

def fetch_data_from_api(url: str):
    response = requests.get(url)
    with open(f"{data_dir}/api_data.json", "w") as file:
        file.write(response.text)
    return "Data fetched and saved."

def clone_git_repo(repo_url: str):
    git.Repo.clone_from(repo_url, f"{data_dir}/repo")
    return "Repository cloned."

def run_sql_query(query: str, db_type: str):
    db_path = f"{data_dir}/database.db"
    conn = sqlite3.connect(db_path) if db_type == "sqlite" else duckdb.connect(db_path)
    result = conn.execute(query).fetchall()
    conn.close()
    return result

def scrape_website(url: str):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    with open(f"{data_dir}/scraped_data.html", "w") as file:
        file.write(str(soup))
    return "Website scraped."

def resize_image():
    image_path = validate_path(f"{data_dir}/image.png")
    img = Image.open(image_path)
    img = img.resize((100, 100))
    img.save(f"{data_dir}/image_resized.png")
    return "Image resized."

def transcribe_audio():
    model = whisper.load_model("base")
    result = model.transcribe(f"{data_dir}/audio.mp3")
    with open(f"{data_dir}/transcription.txt", "w") as file:
        file.write(result["text"])
    return "Audio transcribed."

def convert_markdown_to_html():
    md_path = validate_path(f"{data_dir}/document.md")
    with open(md_path, "r") as file:
        html_content = markdown.markdown(file.read())
    with open(f"{data_dir}/document.html", "w") as file:
        file.write(html_content)
    return "Markdown converted to HTML."

def filter_csv_to_json():
    csv_path = validate_path(f"{data_dir}/data.csv")
    df = pd.read_csv(csv_path)
    filtered_df = df[df["column_name"] == "value"]
    return filtered_df.to_json(orient="records")
