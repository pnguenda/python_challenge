# import dependencies
import cvs
import os

# declaring file location
budget_cvs_path = os.path.join("Resources", "budget_data.csv")


with open(budget_csv_path, "\n") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    print(f"CSV Header: {csv_header}")

# Lists to iterate through specific rows
Pro_Los = []
months = []
M_P_C = []

# read through each row of data after the header
for row in csvreader:
    Pro_Los.append(int(rows[1]))
    months.append(rows[0])

# Determining the change in profit/losses 
for i in range (1, len(Pro_Los)):
    M_P_C.append((int(Pro_Los[i]) - int(Pro_Los[i-1])))

# Calculate the average revenue change 
M_P_C = {round(sum(M_P_C)/ len(M_P_C),2)}

# find the total length of months
total_months = len(months)


# determing the greater increase and decrease in revenue
greatest_increase = max(M_P_C)  
greatest_decrease = min(M_P_C)  

Print all results
print("Financial Analysis")

print("......................................")
print ("total months: " str(total_months))
print(f"total: ${sum(Pro_Los)}")
print("Average Change: " + "$" + str(M_P_C))
print("Greatest Increase in Profits: " + str(months[M_P_C.index(max(M_P_C))+1]) + " " + "$" + str(greatest_increase))
print("Greatest Decrease in Profits: " + str(months[M_P_C.index(min(M_P_C))+1]) + " " + "$" + str(greatest_decrease))

# output to text file

file = open("output.txt","w")
file.write("Financial Analysis" + "\n")
file.write("................................." + "\n")
file.write("total months: " + str(total_months) + "\n")
file.write("Total: " + "$" + str(sum(Pro_Los)) + "\n")
file.write("Average change: " + "$" + str(M_P_C) + "\n")
file.write("Greatest Increase in Profits: " + str(months[M_P_C.index(max(M_P_C))+1]) + " " + "$" + str(greatest_increase) + "\n")
file.write("Greatest Decrease in Profits: " + str(months[M_P_C.index(min(M_P_C))+1]) + " " + "$" + str(greatest_decrease) + "\n")

file.close()