# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast
row_count = 0 #Tracking rows


# Define lists and dictionaries to track candidate names and vote counts
candidate_list = []

# Winning Candidate and Winning Count Tracker
winner = ""
winning_count = 0

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        row_count = row_count + 1

        # Get the candidate's name from the row
        candidate_name = row[2]
        
        # If the candidate is not already in the candidate list, add them
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
            candidate_list.append(1)
                   

        # Add a vote to the candidate's count
        elif candidate_name == "Charles Casper Stockham":
            candidate_list[1] += 1
        elif candidate_name == "Diana DeGette":
            candidate_list[3] += 1 
        elif candidate_name == "Raymon Anthony Doane":
            candidate_list[5] += 1      


# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    total_vote_count = f"{candidate_list[0]}: {candidate_list[1]}, \n{candidate_list[2]}: {candidate_list[3]}, \n{candidate_list[4]}: {candidate_list[5]}"
    print(total_vote_count)

    # Write the total vote count to the text file
    total_votes = row_count

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate in candidate_list:

        # Get the vote count and calculate the percentage
        ccs_percent = (candidate_list[1] / total_votes) * 100
        rounded_ccs_percent = round(ccs_percent,2)
        ddg_percent = (candidate_list[3] / total_votes) * 100
        rounded_ddg_percent = round(ddg_percent,2)
        rad_percent = (candidate_list[5] / total_votes) * 100
        rounded_rad_percent = round(rad_percent,2)
        # Update the winning candidate if this one has more votes
        if ccs_percent > ddg_percent and ccs_percent > rad_percent:
            winner = candidate_list[0]
        elif ddg_percent > rad_percent:
            winner = candidate_list[2]
        else: winner = candidate_list[4]

        # Print and save each candidate's vote count and percentage
        vote_and_percent = f"{candidate_list[0]}: {rounded_ccs_percent}%, \n{candidate_list[2]}: {rounded_ddg_percent}%, \n{candidate_list[4]}: {rounded_rad_percent}%"
        print(vote_and_percent)

    # Generate and print the winning candidate summary
    divider = "-----------------------------------------------"
    output = f"Election Results \n{divider} \nTotal Votes: {total_votes} \n{divider} \n{vote_and_percent} \n{divider} \nWinner: {winner} \n{divider}"
    print(output)
    
    # Save the winning candidate summary to the text file
    txt_file.write(output)