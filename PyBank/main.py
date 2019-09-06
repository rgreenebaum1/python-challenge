import os
import csv

for file_count in range(2):
    file_name = "budget_data_" + str(file_count + 1) + ".csv"

budget_data = "budget_data.csv"

total_months = 0
prev_revenue = 0
month_of_change = []
revenue_change_list = []
greatest_increase = ["", 0]
greatest_decrease = [", 999999999999999999"]
total_revenue = 0
net_change = []
prev_net = []
value = 0
dates = []
profits = []
change = 0
greatest_index = 0
greatest_date = 0
revenue_avg = 0

with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)

    first_row = next(csvreader)
    total_months += 1
    total_revenue += int(first_row[1])
    value = int(first_row[1])

    for row in csvreader:

        # To keep track of the dates
        dates.append(row[0])

        # calculate the change, then add it to list of changes
        change = int(row[1]) - value
        profits.append(change)
        value = int(row[1])

        # The total number of months included in the dataset
        total_months = total_months + 1

        # The net total amount of "Profit/Losses" over the entire period

        total_revenue = total_revenue + int(row[1])

        # The average of the changes in "Profit/Losses" over the entire period
    revenue_avg = round(sum(profits) / len(profits), 2)

    # The greatest increase in profits (date and amount) over the entire period
    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    greatest_date = dates[greatest_index]

    # The greatest decrease in losses (date and amount) over the entire period
    greatest_decrease = min(profits)
    worst_index = profits.index(greatest_decrease)
    worst_date = dates[worst_index]


print("Financial Analysis")
print("-------------------")
print(f"Total Months: {str(total_months)}")
print(f"Revenue: ${total_revenue}")
print(f"Average Change: ${revenue_avg}")
print(f"Greatest Increase in Profits: {greatest_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {worst_date} (${greatest_decrease})")


write_file = f"pybank_results_summary_{file_count+1}.txt"

filewriter = open(write_file, mode="w")
filewriter.write(f"Financial Analysis for {file_name}:\n")
filewriter.write("-------------------------------------------------------\n")
filewriter.write(f"Total Months: {total_months}\n")
filewriter.write(f"Total Revenue: {total_revenue}\n")
filewriter.write(f"Average Revenue Change: {revenue_avg}\n")
filewriter.write(f"Greatest Increase in Revenue: {greatest_date} {greatest_increase}\n")
filewriter.write(f"Greatest Decrease in Revenue: {worst_date} {greatest_decrease}\n")
filewriter.write("")

filewriter.close()
