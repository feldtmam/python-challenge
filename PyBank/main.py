import os
import csv

# Open and read csv file /Users/feldtmam1/Documents/Data Analytics Bootcamp/repos/python-challenge/PyBank
csvpath = os.path.join('/Users/feldtmam1/Documents/Data_Analytics_Bootcamp/repos/python-challenge/PyBank/', 'budget_data.csv')
#try:    
with open(csvpath, "r" ) as my_file_handle:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(my_file_handle, delimiter=',')
    
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    my_unique_months = set()
    values = []
    all_months = []
    net_total_amount = 0
    for rows in csvreader:
        # identify the number of months by reading the values into a set for unique values 
        my_unique_months.add(rows[0])
        all_months.append(rows[0])
        values.append(rows[1])
        # Calculate the net total amount of profit/loss over the entire period
        net_total_amount += int(rows[1])
    total_months = len(my_unique_months)

    # Calculate the average of the changes in profit/loss over the period   
    values_change = [int(values[i + 1]) - int(values[i]) for i in range(len(values)- 1)]
    sum_changed_values = 0
    for i in values_change:
        sum_changed_values += int(i)
    average_change = sum_changed_values / len(values_change)

    # Identify the greatest increase in profits (date and amount) over the entire period
    highest_profit_value = max(values_change)
    highest_profit_value_index = values_change.index(highest_profit_value)
    highest_profit_month = all_months[highest_profit_value_index + 1]
    
    # The greatest decrease in losses (date and amount) over the entire period
    lowest_profit_value = min(values_change)
    lowest_profit_value_index = values_change.index(lowest_profit_value)
    lowest_profit_month = all_months[lowest_profit_value_index + 1]    
    
    # Print results to the terminal
    print(f"Financial Analysis")
    print(f"--------------------------------")
    print(f"Total months: {total_months}")
    print(f"Total: ${net_total_amount: .2f}")
    print(f"Average Change:  ${average_change: .2f}")
    print(f"Greatest Increase in Profits: {highest_profit_month} (${highest_profit_value})")
    print(f"Greatest Decrease in Profits: {lowest_profit_month} (${lowest_profit_value})")

# write the results to a file
output_path = os.path.join("/Users/feldtmam1/Documents/Data_Analytics_Bootcamp/repos/python-challenge/PyBank/", "results.csv")
# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as resultsfile:

    # Initialize csv.writer
    csvwriter = csv.writer(resultsfile, quoting=csv.QUOTE_NONE)

    # Write the content
    csvwriter.writerow([f"Financial Analysis"])
    csvwriter.writerow([f"--------------------------------"])
    csvwriter.writerow([f"Total months: {total_months}"])
    csvwriter.writerow([f"Total:${net_total_amount: .2f}"])
    csvwriter.writerow([f"Average Change: ${average_change: .2f}"])
    csvwriter.writerow([f"Greatest Increase in Profits: {highest_profit_month} (${highest_profit_value})"])
    csvwriter.writerow([f"Greatest Decrease in Profits: {lowest_profit_month} (${lowest_profit_value})"])

"required output"

# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $38382578
# Average  Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)

# Save the results
