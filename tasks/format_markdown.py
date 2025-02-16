import re
import os

project_root = os.path.dirname(os.path.abspath(__file__))  # Get the current script directory
file_path = os.path.join(project_root, "data", "format.md")  # Set the correct path

def clean_markdown():
    """Cleans up Markdown formatting by removing extra spaces while preserving structure."""
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.readlines()

    formatted_lines = [re.sub(r"\s+", " ", line).strip() for line in content]

    return "\n".join(formatted_lines) + "\n"

def process():
    """Process function to clean and save the formatted Markdown."""
    formatted_content = clean_markdown()

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(formatted_content)

    print(f"Formatted markdown file saved at {file_path}")

# Run when executed directly
if __name__ == "__main__":
    process()
