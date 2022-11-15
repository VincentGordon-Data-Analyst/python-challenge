import os 
import csv

csvpath = os.path.join('PyBank','Resources', 'budget_data.csv')

with open(csvpath, newline='') as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',')   
    # Skip first row as it contains just the headings 
    header = next(csvreader)

    # Contains the data for analysis
    dataset = [row for row in csvreader]
    
    print('Financial Analysis')
    print('-----------------------------')
    
    # Find the total number of months in dataset
    date = []
    months = []
    for row in dataset:
        date.append(row[0])
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
        for i in range(1,len(profit_loss)):
            change_list.append(int(profit_loss[i]) - int(profit_loss[i-1]))
            
    # Average of "Profit/Loss" changes
    change_total = sum(change_list)
    change_length = len(change_list)
    average_change = round((change_total / change_length), 2)    
    print(f'Average Change: ${average_change}')

    
    # Find the greatest increase in profits
    max_value = change_list[0]
    for number in change_list[1:]:
        if number > max_value:
            max_value = number
            
    # Find the greatest decrease in profits
    min_value = change_list[0]
    for number in change_list[1:]:
        if number < min_value:
            min_value = number
    
    # Find the month that caused the greatest increase in profits 
    for i in range(len(profit_loss)):
        if int(profit_loss[i]) - int(profit_loss[i - 1]) == max_value:
            great_increase = date[i]
            print(f"Greatest Increase in Profits: {great_increase} (${max_value})")
    
    # Find the month that caused the greatest decrease in profits 
    for i in range(len(profit_loss)):     
        if int(profit_loss[i]) - int(profit_loss[i - 1]) == min_value:
            great_decrease = date[i] 
            print(f"Greatest Decrease in Profits: {great_decrease} (${min_value})")
        
output = os.path.join('PyBank','analysis', 'PyBank.txt')  
with open(output,'w') as f:
    f.write(
        f"""
        Financial Analysis
        ------------------------
        Total Months: {total_months}
        Total: {net_amount}
        Average Change: {average_change}
        Greatest Increase in Profits: {great_increase} (${max_value})
        Greatest Decrease in Profits: {great_decrease} (${min_value})
        """
    )
    