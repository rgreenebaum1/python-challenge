import os
import csv

# for file_count in range(2):
#     file_name = "election_data_" + str(file_count + 1) + ".csv"

# from collections import Counter

csvpath = os.path.join("election_data.csv")
file_to_output = os.path.join("election_data.txt")

# Candidates = []

total_votes = 0

candidate_options = []
candidate_votes = {}


winner_votes = 0
Candidate = {}

winning_candidate = ""
winning_count = 0


with open(csvpath, newline="") as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=",")

    for row in csvreader:

        total_votes = total_votes + 1

        candidate_name = row["Candidate"]

        if candidate_name not in candidate_options:

            candidate_options.append(candidate_name)

            candidate_votes[candidate_name] = 0

            candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

with open(file_to_output, "w") as txt_file:

    election_results = (
        f"\n\nElection Results\n"
        f"------------------------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"------------------------------------------\n"
    )
    print(election_results, end="")

    txt_file.write(election_results)

    Candidates = list(candidate_votes.keys())
    for c in Candidates:
        votes = candidate_votes[c]
        vote_percentage = float(votes / total_votes) * 100

        if votes > winning_count:
            winning_count = votes
            winning_candidate = c

        voter_output = f"{c}: {vote_percentage:.3f}% ({candidate_votes[c]})\n"
        print(voter_output)

    # txt_file.write(voter_output)

winning_summary = (
    f"------------------------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"------------------------------------------"
)

print(winning_summary)

txt_file.write(winning_summary)

