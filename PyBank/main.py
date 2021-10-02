import os
import csv

csv_path = os.path.join("Resources", "budget_data.csv")

with open(csv_path) as csv_file:

    csv_reader = csv.reader(csv_file, delimiter = ",")

    print(f"File correctly read: {csv_reader}")
    csv_header = next(csv_reader)
    # print(f"The header is: {csv_header}")

    # creating tuples to store the columns and work easier with the data
    tuple_date = tuple()
    tuple_value = tuple()

    # storing the rows in the csv file into two different tuples
    for row in csv_reader:
        tuple_date += (row[0],)
        tuple_value += (int(row[1]),)
    
months_total = len(tuple_date)
net_total = sum(tuple_value)

# calculating the Average Change using a for loop
average_change = 0
for i in range(months_total-1):
    average_change += tuple_value[i]-tuple_value[i+1]
    average_change = average_change/months_total

# zipping the tuples to find the Greatest Increase and Decrease Values and Dates
csv_data = zip(tuple_date, tuple_value)

# looping throughthe zipped tuples to find the Greatest Increase and Decrease Values and Dates
for row in csv_data:
    if int(row[1]) == max(tuple_value):
        # print(row)
        greatest_inc_value = int(row[1])
        greatest_inc_date = row[0]
    elif int(row[1]) == min(tuple_value):
        # print(row)
        greatest_dec_value = int(row[1])
        greatest_dec_date = row[0]
    
output_message = str(f"""
Financial Analysis
---------------------------------
Total Months: {months_total}
Total: ${net_total}
Average Change: ${average_change:.{7}}
Greatest Increase in Profits: {greatest_inc_date} {greatest_inc_value}
Greatest Decrease in Profits: {greatest_dec_date} {greatest_dec_value}
""")
print(output_message)   # printing the output message in the screen

# storing the output message in a text file
output_path = os.path.join("analysis", "Financial_Analysis.txt")

with open(output_path, 'w') as txtfile:

    txtfile.write(output_message)
