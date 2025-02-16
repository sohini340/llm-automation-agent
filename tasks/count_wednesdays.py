from datetime import datetime
import os

def process():
    """Count the number of Wednesdays in a list of dates."""
    input_file = "/data/dates.txt"
    output_file = "/data/dates-wednesdays.txt"

    if not os.path.exists(input_file):
        raise FileNotFoundError(f"{input_file} does not exist")

    with open(input_file, "r", encoding="utf-8") as f:
        dates = f.read().splitlines()

    wednesday_count = 0

    for date in dates:
        try:
            dt = datetime.strptime(date, "%Y-%m-%d")  # Ensure format matches the file
            if dt.weekday() == 2:  # 2 represents Wednesday (Mon=0, Sun=6)
                wednesday_count += 1
        except ValueError:
            continue  # Skip invalid date formats

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(str(wednesday_count) + "\n")

    return f"Number of Wednesdays: {wednesday_count} (Saved in {output_file})"

