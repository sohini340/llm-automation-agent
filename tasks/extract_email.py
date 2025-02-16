import re
import openai

# File paths
email_file = "data/email.txt"
output_file = "data/email-sender.txt"

def extract_email(content):
    """Extract sender email using regex."""
    match = re.search(r"From: .*?<?([\w\.-]+@[\w\.-]+\.\w+)>?", content)
    return match.group(1) if match else None

def process():
    """Process function to extract sender's email and save it to a file."""
    with open(email_file, "r", encoding="utf-8") as f:
        email_content = f.read()

    # Extract sender email
    email_address = extract_email(email_content)

    # If regex fails, call LLM API
    if not email_address:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Extract the sender's email address from the given email content."},
                {"role": "user", "content": email_content}
            ]
        )
        email_address = response["choices"][0]["message"]["content"].strip()

    # Write to output file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(email_address + "\n")

    print(f"Sender's email extracted and saved to {output_file}")

# Run when executed directly
if __name__ == "__main__":
    process()
