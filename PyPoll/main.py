import csv, os

# Path to collect data from Resources Folder
PyPoll_csv = os.path.join("Resources", "election_data.csv")

#set variables
votes = 0

#candidate list
candidate_list = []
candidate_votes = {}



#Open the CSV file
with open (PyPoll_csv) as csv_file:
    PyPoll_reader = csv.reader(csv_file, delimiter = ",")
    next(PyPoll_reader)

    for row in PyPoll_reader:
        votes += 1
        
        #read in candidate from column 3
        candidate_name = row[2]
                
        #if statement for unique candidate using append
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
            candidate_votes[candidate_name] = 0
        
        candidate_votes[candidate_name] += 1
        vote_perentage = (candidate_votes/ votes) * 100



output = f"""
Election Results
-------------------------
Total: {votes:,}
vote percentage: {vote_perentage}
-------------------------
[{candidate_list}:{candidate_votes}]
Khan: 63.000% (2218231)
Correy: 20.000% (704200)
Li: 14.000% (492940)
O'Tooley: 3.000% (105630)
-------------------------
Winner: Khan
-------------------------
"""

print(output)

