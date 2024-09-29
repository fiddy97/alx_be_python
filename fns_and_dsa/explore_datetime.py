from datetime import datetime, timedelta

# Part 1: Display the Current Date and Time
def display_current_datetime():
    current_date = datetime.now()  # Get the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # Format it as "YYYY-MM-DD HH:MM:SS"
    print(f"Current date and time: {formatted_date}")

# Part 2: Calculate a Future Date
def calculate_future_date():
    days_to_add = int(input("Enter the number of days to add to the current date: "))  # Prompt the user for input
    current_date = datetime.now()  # Get the current date and time
    future_date = current_date + timedelta(days=days_to_add)  # Calculate the future date
    formatted_future_date = future_date.strftime("%Y-%m-%d")  # Format the future date as "YYYY-MM-DD"
    print(f"Future date: {formatted_future_date}")

# Main execution
if __name__ == "__main__":
    display_current_datetime()  # Display current date and time
    calculate_future_date()     # Calculate and display future date