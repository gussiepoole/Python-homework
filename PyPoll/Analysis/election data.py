import os
import csv

election_data_csv_path = os.path.join("..", "Resources","election_data.csv")

new_voter = []
new_county = []
new_candidate = []
columns = {}

with open(election_data_csv_path, 'r') as csvfile:
    csv_reader= csv.reader(csvfile)
    csv_header=next(csv_reader, None)

    print(csv_header)

    for i, column_name in enumerate(csv_header):
        print(i,column_name)
        columns[column_name] = i

    print(columns)

    for row in csv_reader:
     
        new_voter = row[columns['Ballot ID']]
        new_county = row[columns['County']]
        new_candidate = row[columns['Candidate']]
        print(new_candidate, new_county)
        


