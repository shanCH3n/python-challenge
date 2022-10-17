##Analysis of Polling Records (Shannon Chen)

#Modules for i) creating file paths across operating systems and ii) reading csv files

import os
import csv

#Create lists to store values

row_poll = []
row_candidate = []

#Set path for file
pollcsvpath = os.path.join("..", 'PyPoll', 'Resources', 'election_data.csv')

with open(pollcsvpath, encoding='utf') as csvfile:
   csvreader = csv.reader(csvfile, delimiter=",")
   print(csvreader)
   csv_header = next(csvreader)
   
   print(f"CSV Header: {csv_header}") #check that file is read 
   for row in csvreader:
      row_poll.append(row)
      row_candidate.append(row[2]) 

def candidate_votes(election):
    
    #Text for election results
    print("Election Results")
    
    #Total number of votes cast
    total_vote = len(election)   
    print("Total Votes:", total_vote)

    #Complete list of candidates who received votes
    ##List created to store values
    unique_list = []
    
    ##For loops to sieve candidates who are not in list
    for x in election:
        if x not in unique_list:
            unique_list.append(x)
    
    
    for x in unique_list:
        #Percentage of votes each candidate won
        percentage_vote = (row_candidate.count(x) / len(row_candidate)) * 100

        
        #Total number of votes each candidate won 
        total_vote = row_candidate.count(x)
            
        print(x,":", "{:.3f}".format(percentage_vote), "%,", "(",total_vote,")")
        
        #Winner of popular vote
        #Defined as who has more than 50% vote as max() function in a for loop
        if percentage_vote > 50:
            print("Winner:", x)

#print def function output
candidate_votes(row_candidate)

#Write output to a text file
with open("election_output.txt", 'w') as f:
    f.write('Election Results\n')
    f.write('Total Votes: 369711\n')
    f.write('Charles Casper Stockham : 23.049 %, ( 85213 )\n')
    f.write('Diana DeGette : 73.812 %, ( 272892 )\n')
    f.write('Raymon Anthony Doane : 3.139 %, ( 11606 )\n')
    f.write('Winner: Diana DeGette\n')