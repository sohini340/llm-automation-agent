import sqlite3

# Database path
db_path = "data/ticket-sales.db"
output_path = "data/ticket-sales-gold.txt"

def calculate_gold_sales():
    """Calculate total sales for 'Gold' tickets from the database."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Query to calculate total sales for "Gold" tickets
    cursor.execute("SELECT SUM(units * price) FROM tickets WHERE type = 'Gold'")
    total_sales = cursor.fetchone()[0]  # Fetch the result

    conn.close()
    return total_sales

def process():
    """Process function to compute and save total Gold ticket sales."""
    total_sales = calculate_gold_sales()

    # Write the result to file
    with open(output_path, "w") as f:
        f.write(str(total_sales))

    print(f"Total Gold ticket sales: {total_sales} (saved to {output_path})")

# Run when executed directly
if __name__ == "__main__":
    process()
