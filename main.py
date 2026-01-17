#=========================
# Expense Report Generator
#=========================


# Import the CSV module to work with CSV files
import csv

# List to store all expense records
expenses_list = []

try:

    with open('expenses.csv', mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)

        for row in reader:
            expense = {
                'date': row[0],
                'description': row[1],
                'category': row[2],
                'amount': float(row[3])
            }

            # Add the expense to the list
            expenses_list.append(expense)


except FileNotFoundError:
    print("Error: file not found")

except ValueError:
    print("Error: invalid value found in the file")

except Exception as error:
    print("Unexpected error while reading the file:", error)
    exit()

# Display loaded data (debug)
print(expenses_list)

# Calculate total expenses
total_expenses = 0

for expense in expenses_list:
    total_expenses += expense['amount']

print("Total expenses:", total_expenses)

# Calculate total by category
total_by_category = {}

for expense in expenses_list:
    category = expense['category']
    amount = expense['amount']

    if category in total_by_category:
        total_by_category[category] += amount
    else:
        total_by_category[category] = amount

print(total_by_category)

# Generate expense report
with open('report.txt', mode='w', encoding='utf-8') as report:
    report.write("EXPENSE REPORT\n")
    report.write("-----------------------------\n\n")

    report.write(f"Total expenses: $ {total_expenses:.2f}\n\n")
    report.write("Expenses by category:\n")

    for category, amount in total_by_category.items():
        report.write(f"- {category}: $ {amount:.2f}\n")
