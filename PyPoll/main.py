import os
import csv
from collections import Counter

# Open and read csv file /Users/feldtmam1/Documents/Data Analytics Bootcamp/repos/python-challenge/PyPoll
csvpath = os.path.join('/Users/feldtmam1/Documents/Data_Analytics_Bootcamp/repos/python-challenge/PyBoss/', 'election_data.csv')
#try:    
with open(csvpath, "r" ) as my_file_handle:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(my_file_handle, delimiter=',')
    
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    number_votes = 0
    candidates = set()
    all_votes = []
    count_votes = {}
    new_list = []
    # Read each row of data after the header
    for row in csvreader:
        # The total number of votes cast
        number_votes += 1
        all_votes.append(row[2])

        # A complete list of candidates who received votes
        candidates.add(row[2])
    
    # The total number of votes each candidate won
    count_votes = Counter(all_votes)
    
    win_value = 0
    # The percentage of votes each candidate won and creating the rows of results
    for my_key in count_votes:
        new_list.append(f"{my_key}: {(count_votes[my_key]/number_votes): .3%} ({count_votes[my_key]})")
        # The winner of the election based on popular vote.
        if (count_votes[my_key]/number_votes) > win_value:
            win_value = (count_votes[my_key]/number_votes)
            winner = f"{my_key}"
  

print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {number_votes}")
print(f"-------------------------")
for item in new_list:
        print(f"{item}")
print(f"-------------------------")
print(f"Winner: {winner}")
print(f"-------------------------")
       
# write the results to a file
output_path = os.path.join("/Users/feldtmam1/Documents/Data_Analytics_Bootcamp/repos/python-challenge/PyPoll/", "results_Pypoll.csv")
# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as resultsfile_PyPoll:

    # Initialize csv.writer
    csvwriter = csv.writer(resultsfile_PyPoll, quoting=csv.QUOTE_NONE)

    # Write the content
    csvwriter.writerow([f"Election Results"])
    csvwriter.writerow([f"-------------------------"])
    csvwriter.writerow([f"Total Votes: {number_votes}"])
    csvwriter.writerow([f"-------------------------"])
    for item in new_list:
        csvwriter.writerow([f"{item}"])
    csvwriter.writerow([f"-------------------------"])
    csvwriter.writerow([f"Winner: {winner}"])
    csvwriter.writerow([f"-------------------------"])
    

# What the output should look like

# Election Results
# -------------------------
# Total Votes: 3521001
# -------------------------
# Khan: 63.000% (2218231)
# Correy: 20.000% (704200)
# Li: 14.000% (492940)
# O'Tooley: 3.000% (105630)
# -------------------------
# Winner: Khan
# -------------------------

