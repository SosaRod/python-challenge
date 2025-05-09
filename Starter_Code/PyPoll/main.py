import os
import csv

# Paths
csv_path = os.path.join("Resources", "election_data.csv")
output_path = os.path.join("analysis", "poll_analysis.txt")

# Initialize
total_votes = 0
candidates  = {}

# Read the CSV
with open(csv_path, newline="") as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)  # skip header

    for row in reader:
        total_votes += 1
        candidate = row[2]
        candidates[candidate] = candidates.get(candidate, 0) + 1

# Compute results
results = []
results.append("Election Results")
results.append("-------------------------")
results.append(f"Total Votes: {total_votes}")
results.append("-------------------------")

winner = None
max_votes = 0
for cand, votes in candidates.items():
    pct = votes / total_votes * 100
    results.append(f"{cand}: {pct:.3f}% ({votes})")
    if votes > max_votes:
        max_votes = votes
        winner = cand

results.append("-------------------------")
results.append(f"Winner: {winner}")
results.append("-------------------------")
    
# Print to terminal
for line in results:
    print(line)

# Export to text file
with open(output_path, "w") as txtfile:
    txtfile.write("\n".join(results))
