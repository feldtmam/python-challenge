# Open and read csv file
try:
    with open("budget_data.csv", mode = "r" ) as my_file_handle:
except IOError:
    print("File not found or path is incorrect")
finally:
    print("exit")

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

# Save the results in a file