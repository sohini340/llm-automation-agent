import json

input_path = "data/contacts.json"
output_path = "data/contacts-sorted.json"

def sort_contacts():
    """Sort contacts by last_name, then first_name and return the sorted list."""
    with open(input_path, "r", encoding="utf-8") as f:
        contacts = json.load(f)

    # Sort by last_name, then first_name
    contacts.sort(key=lambda c: (c.get("last_name", "").lower(), c.get("first_name", "").lower()))

    return contacts

def process():
    """Process function to sort and save contacts."""
    sorted_contacts = sort_contacts()

    # Write sorted contacts to output file
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(sorted_contacts, f, indent=4)

    print(f"Sorted contacts saved to {output_path}")

# Run when executed directly
if __name__ == "__main__":
    process()
