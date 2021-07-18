# Add our dependencies
import csv
import os

# Assing a variable for the fiel to load and the path.
file_to_save = 'analysis/election_analysis.txt'

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Set total votes to zero
total_votes = 0

# Create a list for the different candidates
candidate_options = []

# Create an empty dictionary for the candidate votes
candidate_votes = {}

# Winning Candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    
    # Print the header row.
    headers = next(file_reader)

    # The total number of votes cast
    for row in file_reader:
        total_votes = total_votes + 1
        # A compelete list of candidates who received votes.
        candidate_name = row[2]
        # If candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            # Add it to the list of candidates
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
    # Determine the percentage of votes for each candidate by looping through them.
    # Iterate through the candidate list
    for candidate_name in candidate_votes:        
        # Retrieve the vote count of the candidate
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100  
        # Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # Set the winning count = votes
            winning_count = votes
            # Set the winning percentage = vote percentage
            winning_percentage = vote_percentage
            # Set the winning candidate = candidate
            winning_candidate = candidate_name
        # Print the candiate name and percentage of votes
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    print(winning_candidate_summary)
