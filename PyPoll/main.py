# Author: Pablo Crespo Carrillo
# Data Analytics Boot Camp
# The University of Western Australia
# Third assignment: Python Homework - Py Me Up, Charlie

import os
import csv

# -----------------------------------------------------------------------
# Opening the csv file and storing the data in 'csv_list'
csv_path = os.path.join("Resources", "election_data.csv")

with open(csv_path) as csv_file:

    csv_reader = csv.reader(csv_file, delimiter = ",")

    #print(f"File correctly read: {csv_reader}")
    csv_header = next(csv_reader)       #Storing the header row

    csv_list = list(csv_reader)
# -------------------------------------------------------------------------    

# Looping through the list to store data in individual lists with the correct data type ///////////
list_voter = [int(i[0]) for i in csv_list]
list_county = [i[1] for i in csv_list]
list_candidate = [i[2] for i in csv_list]
# /////////////////////////////////////////////////////////////////////////////////////////////////

total_votes = len(list_voter)

candidates = list(set(list_candidate))  # Creating a list of unique candidates with 'set'

# Loop to count votes ..............................................................................
candidates_votes = [0, 0, 0, 0]
for row in csv_list:
    if row[2] == candidates[0]:
        candidates_votes[0] += 1
    elif row[2] == candidates[1]:
        candidates_votes[1] += 1
    elif row[2] == candidates[2]:
        candidates_votes[2] += 1
    elif row[2] == candidates[3]:
        candidates_votes[3] += 1
# .....................................................................................................


for i in range(4):
    if candidates_votes[i] == max(candidates_votes):
        winner = candidates[i]

output_message = str(f"""
Election Results
--------------------------------------------
Total Votes: {total_votes}
--------------------------------------------
{candidates[0]}: {candidates_votes[0]*100/total_votes:.3f}% ({candidates_votes[0]})
{candidates[1]}: {candidates_votes[1]*100/total_votes:.3f}% ({candidates_votes[1]})
{candidates[2]}: {candidates_votes[2]*100/total_votes:.3f}% ({candidates_votes[2]})
{candidates[3]}: {candidates_votes[3]*100/total_votes:.3f}% ({candidates_votes[3]})
--------------------------------------------
Winner: {winner}
--------------------------------------------
""")

print(output_message)

output_path = os.path.join("analysis", "Poll_Analysis.txt")

with open(output_path, 'w') as txtfile:

    txtfile.write(output_message)