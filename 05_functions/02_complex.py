# Function to fetch sales data
def fetch_sales():
    print("Fetching the sales data")


# Function to filter out invalid sales data
def filter_valid_sales():
    print("Filtering valid sales data")


# Function to summarize the filtered sales data
def summarize_data():
    print("Summarizing sales data")


# Main function to generate the sales report
def generate_report():
    fetch_sales()  # Step 1: Get sales data
    filter_valid_sales()  # Step 2: Clean/validate data
    summarize_data()  # Step 3: Summarize results
    print("Report is ready")  # Final step: Notify report is done


# Calling the main function
generate_report()
