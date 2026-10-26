
import csv
from pathlib import Path

project_folder = Path(__file__).resolve().parent.parent
csv_file = project_folder / "data" / "transactions.csv"

total_sales = 0
total_expenses = 0
transaction_count = 0

with open(csv_file, "r", newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    for row in reader:
        amount = float(row["amount"])
        transaction_count += 1

        if row["transaction_type"].strip() == "Sales":
            total_sales += amount
        elif row["transaction_type"].strip() == "Expense":
            total_expenses += amount

net_profit = total_sales - total_expenses

print("SME FINANCE ANALYTICS")
print("-" * 30)
print("Total Transactions:", transaction_count)
print("Total Sales: ₹", f"{total_sales:,.2f}")
print("Total Expenses: ₹", f"{total_expenses:,.2f}")
print("Net Profit: ₹", f"{net_profit:,.2f}")
