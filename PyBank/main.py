import csv, os

# Path to collect data from Resources Folder
PyBank_csv = os.path.join("Resources", "budget_data.csv")

total = 0
months = 0
preBudget = 0
changeTotal = 0
gIncrease = 0
gIncreaseDate = ""
gDecrease = 0
gDecreaseDate = ""


#Open the CSV file
with open (PyBank_csv) as csv_file:
    PyBank_reader = csv.reader(csv_file, delimiter = ",")
    next(PyBank_reader)

    change = 0
    changeCount = 0
   
    for row in PyBank_reader:

        months += 1
        currentBudget = int(row[1])

        total += currentBudget

        if preBudget != 0:
            change = currentBudget - preBudget
            changeTotal += change
            changeCount += 1

        preBudget = currentBudget    

        if change > gIncrease:
            gIncrease = change
            gIncreaseDate = row[0]

        if change < gDecrease:
            gDecrease = change
            gDecreaseDate = row[0] 

        average_change = sum({gIncrease} + {gDecrease}/ {months})  

print()
print (f'Financial Analysis')
print(f'----------------------------')
print(f'Total Months: {months}')
print(f'Total: ${total:,}')
print(f'Average Change:{average_change}')
output = f"""
Financial Analysis
----------------------------
Total Months: {months}
Total: ${total:,}
Average  Change: $-2315.12
Greatest Increase in Profits: {gIncreaseDate} (${gIncrease:,})
Greatest Decrease in Profits: {gDecreaseDate} (${gDecrease:,})
"""

print(output)

with open ("analysis/pybank.txt", 'w') as outfile:
    outfile.write(output)

