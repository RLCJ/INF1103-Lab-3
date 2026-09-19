def process_stock_deliveries():
    # 1. Initialize variables
    total_inventory = 0
    failed_entries = 0

def calculate_tax(total_sales):
    tax_rate = 0.08
    tax_amount = total_sales * tax_rate

def generate_report(total_inventory, failed_entries):
    print("\n" + "=" * 30)
    print("Daily Summary Report")
    print("=" * 30)
    print(f"Total Deliveries Processed: {total_inventory}")
    print(f"Number of Failed/Rejected Entries: {failed_entries}")

    # 2. Run in a continuous loop
    while True:
        user_input = input("Enter stock quantity (or type 'quit' to exit): ").strip()

        # Handle exit condition
        if user_input.lower() == "quit":    #allows upper case 'QUIT'
            break

        # 4. Handle invalid input using .isdigit()
        if not user_input.isdigit():        #returns False if the string contains any non-digit characters, including negative signs or decimal points
            if user_input.startswith("-") and user_input[1:].isdigit():     #checks if the input is a negative number

                # 5. Enforce business rule: Reject negative numbers
                print("Stock quantity cannot be negative. Please enter a positive whole number.")
            else:
                print("Error: Invalid entry. Please enter a positive whole number.")

            failed_entries += 1
            continue  # Move to the next iteration

        # 3. Accept stock values as integers
        quantity = int(user_input)

        # 6. Manage State: Keep a running total
        total_inventory += quantity
        print(f"Accepted: +{quantity} units. Current Total: {total_inventory}")

        # 7. Trigger Overstock Alert (> 500 units)
        if total_inventory > 500:
            print("OVERSTOCK ALERT: Total inventory has exceeded 500 units!")
            break



if __name__ == "__main__":
    process_stock_deliveries();
    