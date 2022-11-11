import os
import csv

csvpath = os.path.join('PyPoll', 'Resources', 'election_data.csv')

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
    vote_per_candidate = []    
    for name in each_name:
        vote_per_candidate.append(name_list.count(name))
    
    # The percentage of votes each candidate won
    percentage = []
    for i in range(len(vote_per_candidate)):
        each_can_percent = (vote_per_candidate[i] / total_vote) * 100
        percentage.append(round(each_can_percent,3))
        

    # Print candidate name, percentage and vote count
    for i in range(len(each_name)):
            print(f"{each_name[i]}: {percentage[i]}% ({vote_per_candidate[i]})")
            
    print("------------------------------")         
    # Print the winner of the election based on high percentage  
    for i in range(len(percentage)):
        
        # Find highest percentage
        max_percent = percentage[0]
        for percent in percentage:
            if percent > max_percent:
                max_percent = percent
                
        # Print winner's name if max_percent matches a value in percentage list
        if max_percent == percentage[i]:
            print(f"Winner: {each_name[i]}")

with open('PyPoll.txt',"w") as f:
    f.write(
        'Election Results\n'
        '-------------------\n'
        'Total Votes: 369711\n'
        '-------------------\n'
        'Charles Casper Stockham: 23.048% (85212)\n'
        'Diana DeGetter: 73.812% (272892)\n'
        'Raymon Anthony Doane: 3.139% (11606)\n'
        '-------------------\n'
        'Winner: Diana DeGette\n'
        '-------------------\n'
        
    )
    
    