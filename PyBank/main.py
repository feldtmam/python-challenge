import os
import csv

# Open and read csv file /Users/feldtmam1/Documents/Data Analytics Bootcamp/repos/python-challenge/PyBank
csvpath = os.path.join('/Users/feldtmam1/Documents/Data Analytics Bootcamp/repos/python-challenge/PyBank/', 'budget_data.csv')
#try:    
with open(csvpath, "r" ) as my_file_handle:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(my_file_handle, delimiter=',')
    
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)
#except IOError:
    #print("File not found or path is incorrect")
#finally:
    #print("exit")

# Identify the total number of months

# Calculate the net total amount of profit/loss over the entire period

# Calculate the average of the changes in profit/loss over the period

# Identify the greatest increase in profits (date and amount) over the entire period

# The greatest decrease in losses (date and amount) over the entire period

# Print results to the terminal
# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $38382578
# Average  Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)

# Save the results
