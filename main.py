from fastapi import FastAPI, HTTPException, Query
import os
from phase_b import (
    fetch_data_from_api, clone_git_repo, run_sql_query, scrape_website,
    resize_image, transcribe_audio, convert_markdown_to_html, filter_csv_to_json
)
from tasks import (
    count_wednesdays, extract_comments, extract_credit_card, extract_email,
    extract_gold_sales, extract_logs, format_markdown, index_markdown, sort_contacts
)

app = FastAPI()

data_dir = "/data"  # Restrict operations to this directory

def validate_path(file_path: str):
    """Ensure the file path is within the /data directory."""
    abs_path = os.path.abspath(file_path)
    if not abs_path.startswith(data_dir):
        raise HTTPException(status_code=403, detail="Access to this path is restricted")
    return abs_path

@app.post("/run")
async def run_task(task: str = Query(..., description="Task description")):
    """Parse and execute the given task."""
    try:
        # Phase B tasks
        if "fetch data" in task.lower():
            url = "https://api.example.com/data"  # Replace with dynamic URL extraction logic
            result = fetch_data_from_api(url)
        elif "clone git repo" in task.lower():
            repo_url = "https://github.com/example/repo.git"  # Replace with dynamic repo extraction
            result = clone_git_repo(repo_url)
        elif "run sql query" in task.lower():
            query = "SELECT * FROM table_name"  # Extract actual query from task
            result = run_sql_query(query, "sqlite")
        elif "scrape website" in task.lower():
            url = "https://example.com"  # Extract URL dynamically
            result = scrape_website(url)
        elif "resize image" in task.lower():
            result = resize_image()
        elif "transcribe audio" in task.lower():
            result = transcribe_audio()
        elif "convert markdown" in task.lower():
            result = convert_markdown_to_html()
        elif "filter csv" in task.lower():
            result = filter_csv_to_json()
        
        # Phase A (tasks folder) tasks
        elif "format markdown" in task.lower():
            result = format_markdown.process()
        elif "count wednesdays" in task.lower():
            result = count_wednesdays.process()
        elif "sort contacts" in task.lower():
            result = sort_contacts.process()
        elif "extract logs" in task.lower():
            result = extract_logs.process()
        elif "index markdown" in task.lower():
            result = index_markdown.process()
        elif "extract email" in task.lower():
            result = extract_email.process()
        elif "extract credit card" in task.lower():
            result = extract_credit_card.process()
        elif "find similar comments" in task.lower():
            result = extract_comments.process()
        elif "calculate gold sales" in task.lower():
            result = extract_gold_sales.process()
        else:
            raise HTTPException(status_code=400, detail="Unknown task")

        return {"status": "success", "message": result}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/read")
async def read_file(path: str = Query(..., description="File path")):
    """Return the content of the specified file."""
    try:
        abs_path = validate_path(path)
        if not os.path.exists(abs_path):
            raise HTTPException(status_code=404, detail="File not found")
        
        with open(abs_path, "r") as file:
            content = file.read()
        return {"content": content}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
