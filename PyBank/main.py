import os
import csv

#set path for file
csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

#set variables

count = 0
total_months = 0
total_revenue = 0
previous_revenue = 0
change_month = 0
revenue_change = 0
greatest_decrease = ['',9999999]
greatest_increase = ["", 0]
revenue_change_list = [1]
revenue_average = 0

#open csv file
with open(csvpath) as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_file)  

  
    for row in csv_reader:
        total_months += 1
        total_revenue += int(row[1])
        
        

        #Calculate average change in revenue between months over the entire period
       
        revenue_change = int(row[1])- previous_revenue
        previous_revenue = int(row[1])
        #revenue_change_list = revenue_change_list + [revenue_change]
        change_month = [change_month] + [row[0]]
        

        #The greatest increase in revenue over the entire period
        if revenue_change > greatest_increase[1]:
            greatest_increase[1] = revenue_change
            greatest_increase[0] = row[0]

        #The greates decrease in revenue over the entire period
        if revenue_change < greatest_decrease[1]:
            greatest_decrease[1] = revenue_change
            greatest_decrease[0] = row[0]
    revenue_average = sum(revenue_change_list)/len(revenue_change_list)


#Print values
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_revenue}")
#print(f"Average Change: ${revenue_average}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")


