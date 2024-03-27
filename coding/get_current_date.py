# filename: get_current_date.py

from datetime import datetime

# Get the current date
current_date = datetime.now()

# Print the current date in YYYY-MM-DD format
print(current_date.strftime('%Y-%m-%d'))