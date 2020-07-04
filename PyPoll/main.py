# import dependencies 
import pandas as pd

# read a file
data_file = pd.read_csv("Resources/election_data.csv")

#print(data_file)

# calculate the total number of votes cast
total_votes = len(data_file)
#total_votes

# create the complete list of candidates who received votes
candidates_count = data_file["Candidate"].value_counts()
#candidates_count

# percentage of votes won by each candidates 
percentage_votes = (candidates_count/total_votes) *100
#percentage_votes

# winner of the election
winner = candidates_count.idxmax()
#winner

# print all the results
print("```text")
print("Election results")
print("...........................")
print("Total votes: " + str(total_votes))
print("...........................")
print("Khan:" + " " + str(round(percentage_votes[0],3)) + "%" + "("+str(candidates_count[0])+")")
print("Correy:" + " " + str(round(percentage_votes[1],3)) + "%" + "("+str(candidates_count[1])+")")    
print("Li:" + " " + str(round(percentage_votes[2],3)) + "%" + "("+str(candidates_count[2])+")")    
print("O'Tooley:" + " " + str(round(percentage_votes[3],3)) + "%" + "("+str(candidates_count[3])+")")
print("............................")
print("winner: " + winner)
print("............................")
print("```")

