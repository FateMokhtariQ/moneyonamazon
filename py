import csv
import requests
from io import StringIO

# Log in to your Amazon account and go to your "Order History" page
# Click on "Download order reports" and download the report for the desired date range
# Save the report file to your local machine

# Replace this with the path to the downloaded report file
REPORT_FILE_PATH = 'path/to/your/amazon/order/report.csv'

# Read the CSV report file into a list of dictionaries
with open(REPORT_FILE_PATH, 'r') as f:
    csv_data = f.read()

csv_file = StringIO(csv_data)
reader = csv.DictReader(csv_file)

# Parse the order data to calculate the total amount spent
total_spent = 0
for row in reader:
    try:
        total_spent += float(row['Item Total'])
    except ValueError:
        # Ignore rows that don't have a valid 'Item Total' value
        pass

# Print the total amount spent
print(f"You have spent ${total_spent:.2f} on Amazon.")
