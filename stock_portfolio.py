print("------ Stock Portfolio Tracker ------")

stocks = {
    "TCS": 3500,
    "INFY": 1600,
    "RELIANCE": 2900,
    "HDFC": 1700,
    "WIPRO": 270
}

total_amount = 0

while True:
    stock_name = input("Enter stock name (or type 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name in stocks:
        quantity = int(input("Enter quantity: "))
        value = stocks[stock_name] * quantity
        total_amount += value
        print(stock_name, "Value = ₹", value)
    else:
        print("Stock not available.")

print("\nTotal Investment Value = ₹", total_amount)

choice = input("Do you want to save the result? (yes/no): ").lower()

if choice == "yes":
    file = open("portfolio.txt", "w")
    file.write("Total Investment Value = ₹" + str(total_amount))
    file.close()
    print("Portfolio saved successfully.")
else:
    print("Thank you for using Stock Portfolio Tracker.")
