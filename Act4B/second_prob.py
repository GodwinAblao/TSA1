import csv
import os

# Function to load exchange rates from CSV
def load_currency_rates(filename):
    currency_rates = {}
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found. Make sure it is in the same directory as this script.")
        exit(1)  # Exit the program if the file is missing

    with open(filename, mode="r", encoding="utf-8", errors="replace") as file:
        reader = csv.reader(file)
        next(reader, None)  # Skip header row if present

        for row in reader:
            if len(row) >= 3:  # Ensure the row has at least 3 columns
                currency_code = row[0].strip().upper()
                exchange_value = row[2].strip()

                try:
                    currency_rates[currency_code] = float(exchange_value)
                except ValueError:
                    print(f"Warning: Invalid exchange rate for {currency_code}. Skipping entry.")

    if not currency_rates:
        print("Error: No valid exchange rates found in the file.")
        exit(1)

    return currency_rates

# Function to get a valid numeric input
def get_positive_float(prompt):
    while True:
        user_input = input(prompt).strip()
        try:
            value = float(user_input)
            if value > 0:
                return value
            else:
                print("Amount must be greater than zero.")
        except ValueError:
            print("Invalid input! Please enter a valid positive number.")

# Function to get a valid currency code
def get_valid_currency(prompt, currency_rates):
    while True:
        currency = input(prompt).strip().upper()
        if currency in currency_rates:
            return currency
        print("Invalid currency code. Available currencies:", ", ".join(currency_rates.keys()))

# Main program
def main():
    filename = "currency.csv"  # Ensure the file is in the correct location
    currency_rates = load_currency_rates(filename)

    usd_balance = get_positive_float("\nHow much dollar do you have? ")
    desired_currency = get_valid_currency("What currency do you want to have? ", currency_rates)

    # Perform conversion
    final_amount = usd_balance * currency_rates[desired_currency]

    # Display results
    print(f"\nDollar: {usd_balance:.2f} USD")
    print(f"{desired_currency}: {final_amount:.9f}")  # 9 decimal places

if __name__ == "__main__":
    main()