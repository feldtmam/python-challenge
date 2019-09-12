import os
import csv
import datetime as dt

# Open and read csv file /Users/feldtmam1/Documents/Data Analytics Bootcamp/repos/python-challenge/PyPoll
csvpath = os.path.join('/Users/feldtmam1/Documents/Data_Analytics_Bootcamp/repos/python-challenge/PyBoss/', ,'employee_data.csv')
#try:    
with open(csvpath, "r" ) as my_file_handle:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(my_file_handle, delimiter=',')
    #csvreader = enumerate(csv.reader(my_file_handle))

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    
    # Convert and export the data to a different format
    my_employee_data = {}
    for rows in csvreader:
        emp_id = rows[0].split()
        full_name = rows[1].split(' ') #split the full name into its two parts
        first_name = full_name[0].strip() # first name strip extra spaces
        last_name = full_name[1].strip() #last name strip extra spaces
        dob = dt.datetime.strptime(rows[2], "%Y-%m-%d").strftime("%m/%d/%Y")
        ssn_split = rows[3].split('-')
        print(ssn_split)
        #ssn = ssn_split[0].str.replace[, "*"] + ssn_split[1].str.replace["*"] + ssn_split[2]
        #ssn = rows[3].str.replace([:5], "*")
        print(emp_id, first_name, last_name, dob)
        

# Then convert and export the data to use the following format instead:
# Emp ID,First Name,Last Name,DOB,SSN,State
# 214,Sarah,Simpson,12/04/1985,***-**-8166,FL
# 15,Samantha,Lara,09/08/1993,***-**-7526,CO
# 411,Stacy,Charles,12/20/1957,***-**-8526,PA
# In summary, the required conversions are as follows:

# The Name column should be split into separate First Name and Last Name columns.

# The DOB data should be re-written into MM/DD/YYYY format.

# The SSN data should be re-written such that the first five numbers are hidden from view.

# The State data should be re-written as simple two-letter abbreviations.



   