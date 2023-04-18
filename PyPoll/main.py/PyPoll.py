#!/usr/bin/env python
# coding: utf-8

# In[2]:


#import operating system
import os

#import csv file
import csv

#create list of variables for vote counts
candidates = []
num_votes = 0
vote_counts = []

#set path
pypoll_csv = os.path.join('../resources','election_data.csv')

#open the csv
with open(pypoll_csv,newline="") as csvfile:
    csvreader = csv.reader(csvfile)

    #skip the header
    line = next(csvreader,None)

    #line by line counting of votes for each candidate
    for line in csvreader:
        num_votes = num_votes + 1
        candidate = line[2]

        #if candidate has other votes then add to vote count
        if candidate in candidates:
            candidate_index = candidates.index(candidate)
            vote_counts[candidate_index] = vote_counts[candidate_index] + 1
        #else create new spot in list for candidate
        else:
            candidates.append(candidate)
            vote_counts.append(1)

#create list of variables for percentage calculations
percentages = []
max_votes = vote_counts[0]
max_index = 0

#determine the percentage of votes for all cadidates and the winner
for count in range(len(candidates)):
    vote_percentage = vote_counts[count]/num_votes*100
    percentages.append(vote_percentage)
    if vote_counts[count] > max_votes:
        max_votes = vote_counts[count]
        max_index = count
winner = candidates[max_index]

#header and line seperator
print("Election Results")
print("_"*35)

#total votes (add comma) and line seperator
print(f"Total Votes: {num_votes:,d}")
print("_"*35)

#candidate name, vote percentage (change from list to int), and number of votes (add comma) and line seperator
for count in range(len(candidates)):
    print(f"{candidates[count]}: {int(percentages[count])}% {vote_counts[count]:,d}")
print("_"*35)

#winner of the election and line seperator
print(f"Winner: {winner}")
print("_"*35)



# In[3]:




#create and open txt file
with open('readme.txt','w') as f:
    f.write('readme')

#print final analysis to file
    f.write("Election Results\n")
    f.write("__________________________________\n")
    f.write(f"Total Votes: {num_votes:,d}\n")
    for count in range(len(candidates)):
        f.write(f"{candidates[count]}: {int(percentages[count])}% {vote_counts[count]:,d}\n")
        f.write("__________________________________\n")
        f.write(f"Winner: {winner}\n")
        f.write("__________________________________\n")

#close file
#f.write.close()


# In[ ]:





# In[ ]:




