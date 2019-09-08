import os
import csv
from collections import Counter

# Open and read csv file /Users/feldtmam1/Documents/Data Analytics Bootcamp/repos/python-challenge/PyPoll
csvpath = os.path.join('/Users/feldtmam1/Documents/Data Analytics Bootcamp/repos/python-challenge/PyPoll/', 'election_data.csv')
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
    #print(count_votes)
    for my_key in count_votes:
        new_list.append([my_key, round(100*(count_votes[my_key]/number_votes), 3), count_votes[my_key]])
        #new_dict.update({'Candidate' : my_key, 'Percentage votes': round(100*(count_votes[my_key]/number_votes), 3), 'Total votes': count_votes[my_key] })
        #print(new_list)
        #print(my_key, ': ', count_votes[my_key])


print("Election Results")
print("-------------------------")
print("Total Votes:", number_votes)
for item in new_list:
    print(item)


# The percentage of votes each candidate won



# The winner of the election based on popular vote.

# As an example, your analysis should look similar to the one below:

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
# Save the results
