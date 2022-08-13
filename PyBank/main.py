# PyBank/Resources/budget_data.csv

# total_profit_losses = 0
# current = 0
# last = 0

# total_change
# months = 0

# # loop through all of the rows in the csv
# for row in reader:
      
# if current cell ticker <> over in our summary table based on summaryrow

#   total_profit_losses = total_profit_losses + int(row[1])

#   months = months + 1

#   current = int(row[1])

#   if months > 1:
#     change = current - last

#     total_change = total_change + change

#   last = int(row[1])


#   average_change = total_change / (months - 1) 




# ....__annotations__



# names = []
# for _ in range(5):
#     name = input("Please enter the name of someone you know. ")
#     names.append(name)

# lowercased = [name.lower() for name in names]
# title_cased = [name.title() for name in lowercased]
# invitations = [
#     f"Dear {name}, please come to the wedding this Saturday!" for name in title_cased]

# for invitation in invitations:
#     print(invitation)

import os
import csv

pybank_csv = os.path.join("Resources", "budget_data.csv")

total_profit_losses = 0
current = 0
last = 0

total_change = 0
months = 0

greatest_increase = 0
greatest_increase_name = ""

greatest_decrease = 9999999
greatest_decrease_name = ""

with open(pybank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

    # loop through all of the rows in the csv
    for row in csvreader:

        total_profit_losses = total_profit_losses + int(row[1])

        months = months + 1

        current = int(row[1])

        if months > 1:
            change = current - last

            total_change += change

            if change > greatest_increase:
                greatest_increase = change
            
            if change < greatest_decrease:
                greatest_decrease = change
        last = int(row[1]) 
    average_change = total_change / (months - 1)

output_file = os.path.join("analysis", "Financial_Analysis.csv")

with open(output_file, "w") as csvfile:
    writer = csv.writer(csvfile)
    
    csvfile.write("Financial Analysis" + '\n')
    #The total number of months included in the dataset
    csvfile.write("Total Months: " + str(months) + '\n')
    print("Total Months: " + str(months))

    #The net total amount of "Profit/Losses" over the entire period
    csvfile.write("Total: $" + str(total_profit_losses) + '\n')
    print("Total: " + str(total_profit_losses))

    #The changes in "Profit/Losses" over the entire period, and then the average of those changes
    csvfile.write("Average Change: $" + str(average_change) + '\n')
    print("Average Change: " + str(average_change))

    #The greatest increase in profits (date and amount) over the entire period
    csvfile.write("Greatest Increase in Profits: $" + str(greatest_increase) + '\n')
    print("Greatest Increase in Profits: " + str(greatest_increase))

    #The greatest decrease in profits (date and amount) over the entire period
    csvfile.write("Greatest Decrease in Profits: $" + str(greatest_decrease) + '\n')
    print("Greatest Decrease in Profits: " + str(greatest_decrease))

#with open(output_file, 'w') as csvfile:
    #csvwriter = csv.writer(csvfile)
    #csv.writer.writerow("Total Months: " + str(months))