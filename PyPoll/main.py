import csv, os


# Path to collect data from Resources Folder
PyPoll_csv = os.path.join("Resources", "election_data.csv")

# Define variables
candidate_list = []
candidate_votes = {}
total_votes = 0
maxVotes = 0
winner = ""

# Open the CSV file
with open (PyPoll_csv) as csv_file:
    PyPoll_reader = csv.reader(csv_file, delimiter = ",")
    next(PyPoll_reader)

    for row in PyPoll_reader:
        # Total number of votes
        total_votes += 1
        # Get candidate name
        candidate_name = row[2]

        # Count votes for each candidate
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1     

# print(candidate_votes)  

 # For loop to find winner of election
for candidate, votes in candidate_votes.items():
    if maxVotes < votes:
            # found candidate with more votes, update current name
            maxVotes = votes
            winner = candidate


print(f'\n{winner}  {maxVotes}\n')
#percentage of votes each candidate won
#total number of votes each candidate won
#winner of the election based on popular vote

output = f"""
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
Khan: {candidate_votes["Khan"] / total_votes * 100:.3f}% ({candidate_votes["Khan"]})
Correy: {candidate_votes["Correy"] / total_votes * 100:.3f}% ({candidate_votes["Correy"]})
Li: {candidate_votes["Li"] / total_votes * 100:.3f}% ({candidate_votes["Li"]})
O'Tooley: {candidate_votes["O'Tooley"] / total_votes * 100:.3f}% ({candidate_votes["O'Tooley"]})
-------------------------
Winner: {winner}
-------------------------
"""

print(output)

with open ("analysis/poll.txt", 'w') as output_file:
    output_file.write(output)


