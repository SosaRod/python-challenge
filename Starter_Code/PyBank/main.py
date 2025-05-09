import os
import csv

# Paths
csv_path = os.path.join("Resources", "budget_data.csv")
output_path = os.path.join("analysis", "bank_analysis.txt")

# Initialize variables
total_months = 0
net_total    = 0
prev_profit  = None
changes      = []
months       = []

# Read the CSV
with open(csv_path, newline="") as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)  # skip header

    for row in reader:
        date, profit = row[0], int(row[1])
        total_months += 1
        net_total    += profit

        # track month-to-month changes
        if prev_profit is not None:
            change = profit - prev_profit
            changes.append(change)
            months.append(date)
        prev_profit = profit

# Compute metrics
average_change = sum(changes) / len(changes)
greatest_inc   = max(changes)
greatest_dec   = min(changes)
inc_month      = months[changes.index(greatest_inc)]
dec_month      = months[changes.index(greatest_dec)]

# Prepare output
lines = [
    "Financial Analysis",
    "----------------------------",
    f"Total Months: {total_months}",
    f"Total: ${net_total}",
    f"Average Change: ${average_change:.2f}",
    f"Greatest Increase in Profits: {inc_month} (${greatest_inc})",
    f"Greatest Decrease in Profits: {dec_month} (${greatest_dec})",
]

# Print to terminal
for line in lines:
    print(line)

# Export to text file
with open(output_path, "w") as txtfile:
    txtfile.write("\n".join(lines))
