from datetime import datetime

def format_date(date_str):
    try:
        date_obj = datetime.strptime(date_str, "%m/%d/%Y")
        return date_obj.strftime("%B %d, %Y")
    except ValueError:
        return "Invalid date format. Please use mm/dd/yyyy."

def main():
    date_input = input("Enter the date (mm/dd/yyyy): ")
    formatted_date = format_date(date_input)
    print(f"Date Output: {formatted_date}")

if __name__ == "__main__":
    main()
