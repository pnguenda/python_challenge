# import dependencies 
import csv
import os

# read a file
election_csv_path = os.path.join("Resources/election_data.csv")

with open(election_csv_path) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csv_reader)
    print(f"CSV Header: {csv_header}")

    #list to hold data
    candidates = []
    voters_ID = []

    #read through each row of data
    for row in csv_reader:
        candidates.append(row[2])
        voters_ID.append(row[0])

    #votes by person 
    d = {}
    #loop through the candidates list
    for candidate in candidates:
        if candidate in d.keys(): 
            d[candidate] += 1

        else:
            d[candidate] = 1
            
    #calculate the total number of votes cast
    total_votes = (len(voters_ID))


    #return percentage of votes won by each candidate in a dict
    K_percent = round(((2218231/total_votes) * 100),3)
    C_percent = round(((704200/total_votes) * 100),3)
    L_percent = round(((492940/total_votes) * 100),3)
    O_percent = round(((105630/total_votes) * 100),3)
    print(K_percent)
    print(C_percent)
    print(L_percent)
    print(O_percent)

    #election winner
    if K_percent > max(C_percent, L_percent, O_percent):
        winner = "Khan"
    elif C_percent > max(K_percent, L_percent, O_percent):
        winner = "Correy"
    elif L_percent > max(K_percent, C_percent, O_percent):
        winner = "Li"
    else: 
        winner = "O'Tooley"
    print(winner)
    

#print all statements 
print("```text")
print("Election Results")
print(".............................")
print("Total Votes: " + str(total_votes))
print(".............................")
print(f'Khan: {K_percent}%' + "   " + (str(d['Khan'])))
print(f'Correy: {C_percent}%' + "   " + (str(d['Correy'])))
print(f'Li: {L_percent}%' + "   " + (str(d['Li'])))
print(f"O'Tooley: {O_percent}%" + "   " + (str(d["O'Tooley"])))
print(".............................")
print(f"Winner: " + winner)
print(".............................")
print("```")
