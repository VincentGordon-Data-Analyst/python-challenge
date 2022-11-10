import os
import csv

csvpath = os.path.join('..','PyPoll', 'Resources', 'election_data.csv')

with open(csvpath, newline='') as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip first row as it contains only the headers
    header = next(csvreader)
    
    # Contains the data for analysis
    dataset = [row for row in csvreader]
    
    print("Election Results")
    print("------------------------------")    
    
    # Create a list that contains all the votes
    vote_list = []    
    for row in dataset:
        vote_list.append(row[0])
    
    # Get total vote count
    total_vote = len(vote_list)
    print(f"Total Votes: {total_vote}")
    print("------------------------------")    
    
    # Create a list that contains all names
    name_list = []
    for row in dataset:
        name_list.append(row[2])
    
    # Get name of each candidate
    each_name = []
    for i in name_list:
        if i not in each_name:
            each_name.append(i)
    
    # Find total votes for each candidate
    each_vote_count = 0
    first_name = name_list[0]
    candidate_vote_count = []

    for i in range(1,len(name_list)):
        if name_list[i] != name_list[i - 1]:
            each_vote_count += int(row[0])
            candidate_vote_count.append(each_vote_count)
    print(candidate_vote_count)
    