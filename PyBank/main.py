import os 
import csv

csvpath = os.path.join('..','Resources', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')    
    
    # Skip first row as it contains just the headings 
    header = next(csvreader)
    
    # Contains the data for analysis
    dataset = [row for row in csvreader]
    
    # Find the total number of months in dataset
    months = []
    for row in dataset:
        months.append(row[0][0:3])        
        total_months = len(months)
        
    print(f'Total Months: {total_months}')
    
    # Find the net total of "Profit/Losses" over entire period
    net_amount = 0    
    for row in dataset:
        net_amount += int(row[1])
        
    print(f'Total: ${net_amount}')

    # Find changes in "Profit/Losses" over time frame    
    profit_loss = []    
    for row in dataset:               
        # Add "Profit/Loss" values into an empty array
        profit_loss.append(row[1])
    
        # Get difference betwen numbers in profit_loss list
        change_list = []
        for x,y in zip(profit_loss[0::], profit_loss[1::]):
            change_list.append(int(y) - int(x))    
               
    # Average of "Profit/Loss" changes
    change_total = sum(change_list)
    change_length = len(change_list)
    average_change = round((change_total / change_length), 2)
    
    print(f'Average Change: ${average_change}')
        
    # Greatest increase in profits