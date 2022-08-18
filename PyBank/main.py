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
    csvfile.write("Total Months: " + str(months) + '\n')
    print("Total Months: " + str(months))

    csvfile.write("Total: $" + str(total_profit_losses) + '\n')
    print("Total: " + str(total_profit_losses))

    csvfile.write("Average Change: $" + str(average_change) + '\n')
    print("Average Change: " + str(average_change))

    csvfile.write("Greatest Increase in Profits: $" + str(greatest_increase) + '\n')
    print("Greatest Increase in Profits: " + str(greatest_increase))

    csvfile.write("Greatest Decrease in Profits: $" + str(greatest_decrease) + '\n')
    print("Greatest Decrease in Profits: " + str(greatest_decrease))