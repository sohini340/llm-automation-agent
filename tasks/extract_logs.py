import os
import glob

logs_directory = "data/logs"
output_path = "data/logs-recent.txt"

def extract_recent_logs():
    """Extract the first line of the 10 most recent .log files and return them."""
    
    # Get a list of all .log files in the directory, sorted by modification time (newest first)
    log_files = sorted(glob.glob(os.path.join(logs_directory, "*.log")), key=os.path.getmtime, reverse=True)[:10]
    
    lines = []
    
    for log_file in log_files:
        try:
            with open(log_file, "r", encoding="utf-8") as f:
                first_line = f.readline().strip()  # Read first line
                if first_line:
                    lines.append(first_line)
        except Exception as e:
            print(f"Skipping {log_file} due to error: {e}")

    return lines

def process():
    """Process function to extract and save recent log headers."""
    log_lines = extract_recent_logs()

    # Write the extracted lines to the output file
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(log_lines) + "\n")

    print(f"Extracted logs saved to {output_path}")

# Run when executed directly
if __name__ == "__main__":
    process()
