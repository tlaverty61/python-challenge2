import os
import csv

# join Polling Data file
csvFilePath = os.path.join("Resources", "election_data.csv")

# varibales declaration
totalvotes = 0

# initialize lists
candidates = []
candidate_votes = {}


# open the Budget File
with open(csvFilePath, "r", encoding="utf-8") as csvFile:

    # read file and set header
    csvReader = csv.reader(csvFile, delimiter=",")
    csvHeader = next(csvReader)
    
    # analyze each row
    for row in csvReader:
        # count votes
        totalvotes += 1

        # identify the candidate name 
        candidate_name = row[2]
                
        # build list of candidates
        if candidate_name not in candidates:
            candidates.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
    

# Calculate and publish results
# join text file
results = os.path.join("analysis", "results.txt")

# declare variables for individual votes
candidateVotePercent = 0
winnerPercent = 0
winnerCount = 0
winner = ""

# save results to text file
with open(results, "w") as txt_file:

    # print the final results
    results = (f"\n Election Results \n"
                f"----------------------------\n"
                f" Total Votes: {totalvotes:,}\n"
                f"-----------------------------\n")
    print(results, end="")

    txt_file.write(results)

    # Determine the percentage of votes for each candidate.
    for candidate in candidate_votes:
        
        votes_candidate  =  candidate_votes[candidate]
        
        candidateVotePercent = int(votes_candidate) / int(totalvotes) * 100  
        
        candidate_results = (f"{candidate}: {candidateVotePercent:.1f}% ({votes_candidate:,})\n")
        
        # Print each candidate, their voter count, and percentage to the text file
        print(candidate_results)
        
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate
        if (votes_candidate > winnerCount) and (candidateVotePercent > winnerPercent):
            winnerCount = votes_candidate
            candidateVotePercent = candidateVotePercent
            
            winner = candidate  

    # Print the winning candidate, total votes and vote percentage.
    winner = (
        f"----------------------------\n"
        f"Winner: {winner}\n"
        f"----------------------------\n")
    print(winner)
    # Save the winning candidate's name to the text file.
    txt_file.write(winner)



 







 
        