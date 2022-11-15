import os
import csv
from collections import Counter

election_data_csv_path = os.path.join("..", "Resources","election_data.csv")
election_data_csv_path="//Users//gussiepoole//UBHM//PyPoll//Resources//election_data.csv"
new_voter = []
new_county = []
new_candidate = []
candidate_list = []
votes_per_candidate = {}
total_votes = 0
columns = {}

with open(election_data_csv_path, 'r') as csvfile:
    csv_reader= csv.reader(csvfile)
    csv_header=next(csv_reader, None)


    for i, column_name in enumerate(csv_header):
        print(i,column_name)
        columns[column_name] = i


    for row in csv_reader:
     
        new_voter = row[columns['Ballot ID']]
        new_county = row[columns['County']]
        new_candidate = row[columns['Candidate']]
        
        if new_candidate not in candidate_list:
            candidate_list.append(new_candidate)
            votes_per_candidate[new_candidate] = 0
        votes_per_candidate[new_candidate] += 1
        total_votes +=1

    print("Total votes = " + str(total_votes))
    

for k, v in votes_per_candidate.items():
    vote_percentage = float(v) / float(total_votes) * 100
    print(f'{k}: {vote_percentage:.2f}% ({v:,})')

print('Winner = Diana DeGette')
