import os
import json
import re

docs_directory = "data/docs"
output_index_file = "data/docs/index.json"

def extract_h1_title(file_path):
    """Extract the first H1 title (# Title) from a Markdown file."""
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            match = re.match(r"^# (.+)", line.strip())
            if match:
                return match.group(1)
    return None

def create_markdown_index():
    """Create an index of Markdown files mapping filenames to their H1 titles."""
    index = {}
    
    for root, _, files in os.walk(docs_directory):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                title = extract_h1_title(file_path)
                if title:
                    relative_path = os.path.relpath(file_path, docs_directory)
                    index[relative_path] = title
    
    return index

def process():
    """Process function to generate and save the Markdown index."""
    index = create_markdown_index()
    
    with open(output_index_file, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=4)
    
    print(f"Index file created at {output_index_file}")

# Run when executed directly
if __name__ == "__main__":
    process()
