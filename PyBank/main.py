# import dependencies
import csv
import os

# declaring file location
budget_csv_path = os.path.join("Resources /budget_data.csv")


with open(budget_csv_path) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csv_reader)
    print(f"CSV Header: {csv_header}")

    # Lists to iterate through specific rows
    Pro_Los = []
    months = []
    M_P_C = []


    # read through each row of data after the header
    for row in csv_reader:
        Pro_Los.append(int(row[1]))
        months.append(row[0])

    # Determining the change in profit/losses 
    for i in range (1, len(Pro_Los)):
        M_P_C.append((int(Pro_Los[i]) - int(Pro_Los[i-1])))

    # Calculate the average revenue change 
    average_change = [round(sum(M_P_C)/ len(M_P_C),2)]

    # find the total length of months
    total_months = len(months)


    # determing the greater increase and decrease in revenue
    greatest_increase = max(M_P_C)  
    greatest_decrease = min(M_P_C)  
    greatest_increase_months = months[M_P_C.index(max(M_P_C))+1]
    greatest_decrease_months = months[M_P_C.index(min(M_P_C))+1]

#Print all results
print("```text")
print("Financial Analysis")
print(greatest_increase_months)
print("......................................")
print ("total months: " +  str(total_months))
print(f"total: ${sum(Pro_Los)}")
print("Average Change: " + "$" + str(average_change))
print("Greatest Increase in Profits: " + greatest_increase_months + " " + "$" + str(greatest_increase))
print("Greatest Decrease in Profits: " + greatest_decrease_months + " " + "$" + str(greatest_decrease))
print("```")