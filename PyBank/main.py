# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
months = 0
total_net = 0

# Add more variables to track other necessary financial data
net_change_list = []

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    initial_row = next(reader)
    high_net = initial_row
    low_net = initial_row
    high_net_amount = 0
    low_net_amount = 0
    
    # Track the total and net change
    total = 0
    net_change = 0
    prev_row = initial_row

    # Process each row of data
    for row in reader:

        # Track the total
        total += int(row[1])
        grand_total = total + int(initial_row[1])
        months += 1
        total_months = months + 1

        # Track the net change
        net_change = int(row[1]) - int(prev_row[1])
        net_change_list.append(net_change)  
               
              

       
        

        # Calculate the greatest increase in profits (month and amount)
        if net_change > high_net_amount:
            high_net = row
            high_net_amount = net_change


        # Calculate the greatest decrease in losses (month and amount)
        elif net_change < low_net_amount:
            low_net = row
            low_net_amount = net_change

        prev_row = row


# Calculate the average net change across the months
net_ch_count = len(net_change_list)
net_ch_sum = sum(net_change_list)
net_change_average = net_ch_sum / net_ch_count

# Generate the output summary
rounded_net_change_average = round(net_change_average,2)

output = f"1Financial Analysis \n---------------------------------- \nTotal Months: {total_months} \nTotal: {grand_total} \nAverage Change: ${rounded_net_change_average} \nGreatest Increase in Profits: {high_net[0]} (${high_net_amount}) \nGreatest Decrease in Profits: {low_net[0]} (${low_net_amount})"

# Print the output
print(output)


# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)

