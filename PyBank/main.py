# Author: Pablo Crespo Carrillo
# Data Analytics Boot Camp
# The University of Western Australia
# Third assignment: Python Homework - Py Me Up, Charlie

import os
import csv

# -----------------------------------------------------------------------
# Opening the csv file and storing the data in 'csv_list'
csv_path = os.path.join("Resources", "budget_data.csv")

with open(csv_path) as csv_file:

    csv_reader = csv.reader(csv_file, delimiter = ",")
    # print(f"File correctly read: {csv_reader}")

    csv_header = next(csv_reader)       #Storing the header row
    # print(f"The header is: {csv_header}")

    csv_list = list(csv_reader)
# ---------------------------------------------------------------------------

# ***************************************************************************
# Looping through the list to store dates and profits/losses in two separate lists with correct data type
list_date = [i[0] for i in csv_list]
list_value = [int(i[1]) for i in csv_list]
# ***************************************************************************

months_total = len(list_date)
net_total = sum(list_value)

# //////// calculating the Average of the Changes in Profit/Losses using a for loop ///////
profit_change = list()
for i in range(months_total-1):
    profit_change.append(list_value[i+1] - list_value[i])
    average_change = sum(profit_change)/(months_total-1)
# /////////////////////////////////////////////////////////////////////////////////////////

greatest_inc_value = max(profit_change)
greatest_dec_value = min(profit_change)

# +++++++++ Finding the date associated with the greatest increase and decrease in profit ++++++++++++++++++
profit_change.insert(0,0) #List started with zero because there was no change in profit in the first month

for index, row in enumerate(profit_change):
    if row == greatest_inc_value:
        greatest_inc_date = list_date[index]
    elif row == greatest_dec_value:
        greatest_dec_date = list_date[index]
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Output message and writing the output file    
output_message = str(f"""
Financial Analysis
---------------------------------
Total Months: {months_total}
Total: ${net_total}
Average Change: ${average_change:.2f}
Greatest Increase in Profits: {greatest_inc_date} (${greatest_inc_value})
Greatest Decrease in Profits: {greatest_dec_date} (${greatest_dec_value})
""")
print(output_message)   # printing the output message in the screen

# storing the output message in a text file
output_path = os.path.join("analysis", "Financial_Analysis.txt")

with open(output_path, 'w') as txtfile:

    txtfile.write(output_message)
