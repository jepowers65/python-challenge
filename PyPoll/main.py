import os
import csv

#Set path for csv file
csvpath = os.path.join('.', 'Resources', 'election_data.csv')

#Declare variables and empty lists
voter_ids = []
counties = []
candidates = []
unique_candidates = []
votes_per_candidate = []
total_votes = 0


#Open csv in read mode
with open(csvpath, newline='') as csvfile:
    #Store contents of election_data in the variable csvreader
    csvreader = csv.reader(csvfile, delimiter=",")

    #skip the header lables
    header = next(csvreader)

    #Iterate through each row and append 
    for row in csvreader:
        voter_ids.append(row[0])
        counties.append(row[1])
        candidates.append(row[2])
        total_votes += 1


    #Calculate the total numbr of votes each candidate received and store in list
    for candidate in set(candidates):
        unique_candidates.append(candidate)
        votes = candidates.count(candidate)
        votes_per_candidate.append(votes)
        unique_candidates.sort()

    #Calculate the percentage of votes each candidate received
    percentages = [(votes / total_votes) * 100 for votes in votes_per_candidate]

    #Find the candidate with the most votes to find the winner
    winner_index = votes_per_candidate.index(max(votes_per_candidate))
    winner = unique_candidates[winner_index]

#Print the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for i in range(len(unique_candidates)):
    print(f"{unique_candidates[i]}: {percentages[i]:.3f}% ({votes_per_candidate[i]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")


#export results to a text file
election_file = os.path.join('analysis', 'election_summary.txt')
with open(election_file, "w") as file:

#Write to file
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
    for i in range(len(unique_candidates)):
        file.write(f"{unique_candidates[i]}: {percentages[i]:.3f}% ({votes_per_candidate[i]})\n")        
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")