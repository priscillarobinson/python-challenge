import csv, os
from typing import Counter

# Path to collect data from Resources Folder
PyPoll_csv = os.path.join("Resources", "election_data.csv")

voter_id = []
candidate_list = [2]
total_votes = {}

voter_id = [0] + 1
#Open the CSV file
with open (PyPoll_csv) as csv_file:
    PyPoll_reader = csv.reader(csv_file, delimiter = ",")
    next(PyPoll_reader)

print(len(voter_id))
