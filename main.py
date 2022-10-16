##Analysis of Financial Records (Shannon Chen)

#Modules for i) creating file paths across operating systems and ii) reading csv files

import os
import csv

#Create lists to store values

row_date = []
row_pl = []

#Set path for file
bankcsvpath = os.path.join("..", 'PyBank', 'Resources', 'budget_data.csv')

with open(bankcsvpath, encoding='utf') as csvfile:
   csvreader = csv.reader(csvfile, delimiter=",")
   print(csvreader)
   csv_header = next(csvreader)
   
   print(f"CSV Header: {csv_header}") #check that file is read 
   for row in csvreader:
        row_date.append(row[0])
        row_pl.append(int(row[1])) #values in profit/losses column defined as integer values
        #print (row) ##Activate to check that data has been read


#Total number of months included in dataset
total_months = len(row_pl)
print("Total number of months: ", total_months)

#Net total amount of "Profit/Losses" over the entire period
net_total = sum(row_pl)
print("Total: ", "${:.2f}".format(net_total))

#Changes in "Profit/Losses" over entire period, and average of those changes
def average_change(x):
    length = len(x) - 1  #For number of rows minus the first row (the diff for that would be 0)
    diff = [x[i+1] - x[i] for i in range(len(x) - 1)] #this is a list comprehension
    for row in diff:
        total = sum(diff) #Sum up the differences
    return total / length

print("Average Change: ", "${:.2f}".format(average_change(row_pl)))


##Remove first element from the list as it is zero. 
##Combine the two lists to create a dictionary
##Note every time the code is run - the first element is removed (e.g., remove Jan-10, Feb-10 is next)

row_date.pop(0)

##print(row_date) Another check ## Activate to see entire period considered

#Greatest increase in profits

def max_change(x, y):

    diff = [x[i+1] - x[i] for i in range(len(x) - 1)] #this is a list comprehension
    append_dict = {y[i]: diff[i] for i in range(len(y))} #    to convert lists to dictionary
    return ((max(append_dict, key=append_dict.get)), max(append_dict.values())) ##first one is to return the max month-year value, 2nd one is the max value

print("Greatest Increase in Profits: ", max_change(row_pl, row_date))

#Greatest decrease in profit
def min_change(x, y):

    diff = [x[i+1] - x[i] for i in range(len(x) - 1)] #this is a list comprehension
    append_dict = {y[i]: diff[i] for i in range(len(y))} #to convert lists to dictionary
    return ((min(append_dict, key=append_dict.get)), min(append_dict.values())) ##first one is to return the min month-year value, 2nd one is the min value

print("Greatest Decrease in Profits: ", min_change(row_pl, row_date))

## Save results of analysis to text file
## "a" is used to add text to existing text in file.
## Note: If you rerun the script with the same text file name, it just accummulates the output text in the same file.

####PLEASE IGNORE: Initial code for writting analysis results into file
##with open("output_budget.txt", 'a') as f:
    ##f.write("Financial Analysis,")
    ##f.write("Total number of months: 86,")
    ##f.write("Total: 22564198,")
    ##f.write("Average Change: -8311.105882352942,")
    ##f.write("Greatest Increase in Profits: ('Aug-16', 1862002),")
    ##f.write("Greatest Decrease in Profits: ('Feb-14', -1825558)")

with open("pybank_output.txt", 'w', encoding = 'utf-8') as f:
    f.write("Financial Analysis \n")
    f.write("Total number of months: 86 \n")
    f.write("Total: $22564198.00 \n")
    f.write("Average Change: $-8311.11 \n")
    f.write("Greatest Increase in Profits: ('Aug-16', $1862002)\n")
    f.write("Greatest Decrease in Profits: ('Feb-14', $-1825558)\n")