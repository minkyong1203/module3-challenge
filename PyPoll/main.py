import os
import csv
import sys

dirname = os.path.dirname(__file__)
csvpath = os.path.join(dirname, 'Resources', 'election_data.csv')

# open analysis file to store results
output_file_path = os.path.join(dirname, 'Analysis', 'analysis.txt')
sys.stdout = open(output_file_path, 'w')
print('-----------Election Results-----------')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    # create empty lists to store each column of data
    names = []
    ballot_ids = []
    vote_count = 0

    # find the total number of votes cast
    for row in csvreader:
        ballot_ids.append(row[0])
        names.append(row[2])
    
    for i in range(len(ballot_ids)):
        if i != i+1:
            vote_count += 1
    print(f"Total vote count: {vote_count}")

    # create empty lists 
    dictionary_of_votes = dict()
    candidate_unique_names = []
    percentage_of_votes = []
    
    
    # loop through 'names list' to get the unique candidate names and put them into a dictionary
    for i in range(len(names)):
        if i <= len(names):
            # check that it is not already in the candidate_unique_names list
            if names[i] not in candidate_unique_names: 
                candidate_unique_names.append(names[i])
                dictionary_of_votes = dict.fromkeys(candidate_unique_names)

    # loop through the dictionary of names
    for key in dictionary_of_votes:
        # reset number of votes before moving onto the next key
        number_of_votes = 0

        # loop through each item in the names list
        for name in names:
            if key == name:

                # add one to number of votes if the names match in names and dictionary list
                number_of_votes += 1
                dictionary_of_votes[key]= number_of_votes
                percentage_of_votes.append((number_of_votes / vote_count) * 100)
    print(dictionary_of_votes)
 
    # go through the list of votes in percentage to find the greatest value
    for i in range(len(percentage_of_votes)):
        if i < (len(percentage_of_votes) - 1):
            if percentage_of_votes[i] > percentage_of_votes[i+1]:
                winner = percentage_of_votes[i]

    # print the name of winner and percentage of their votes
    for key, value in dictionary_of_votes.items():
        if value==winner:
            print (f"The winner is: {key, value}%")

    # close output file
    sys.stdout.close()
    
    