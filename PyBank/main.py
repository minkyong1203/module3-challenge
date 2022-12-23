import os

# module for reading CSV files
import csv

# to write output to txt file
import sys

# path for this file
dirname = os.path.dirname(__file__)
csvpath = os.path.join(dirname, 'Resources', 'budget_data.csv')

# store output file path and open the file to start storing output
output_file_path = os.path.join(dirname, 'Analysis', 'analysis.txt')
sys.stdout = open(output_file_path, 'w')
print("---------------Financial Analysis--------------")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    # create empty lists to store each column separately
    months = []
    profit_losses = []


    count_months = 0
    profit = 0

    for row in csvreader:
        months.append(row[0])
        profit_losses.append(int(row[1])) #change all list items into int
    
    # calculation for total number of months
    for m in months:
        count_months += 1
    print(f"This is the total number of months: {count_months}")

    # calculation of total profit
    for p in profit_losses:
        profit += p
    print(f"This is the net profit over the period: ${profit}")

    # average of entire profit/losses
    changes = []
    for i in range(len(profit_losses)):
        if i <= 84:
            changes.append(profit_losses[i+1] - profit_losses[i])
    sum_of_changes = sum(changes)
    average_of_changes = sum_of_changes/len(changes)
    print(f"Average change: {average_of_changes}")


    # greatest increase/decrease

    # set the first item in changes list to be the anchor
    greatest_decrease = changes[0]

    # loop through the items in changes list using their index number
    for i in range(len(changes)):
        # if the item value is less than the anchor, update with the lower change value
       if changes[i] < greatest_decrease:
            greatest_decrease = changes[i]
            time_of_decrease = months[i+1]
    # use i+1 for the index to find the month after change had occurred
    print(f"Greatest decrease in profits: {time_of_decrease}, {greatest_decrease}")
    
    # repeat same process as above to find the greatest increase
    greatest_increase = changes[0]

    for i in range(len(changes)):
        if changes[i] > greatest_increase:
            greatest_increase = changes[i]
            time_of_increase = months[i+1]
    
    print(f"Greatest increase in profits: {time_of_increase}, {greatest_increase}")
 
    # close output file
    sys.stdout.close()

