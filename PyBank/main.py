import os
import pandas as pd
#set file
file  = 'budget_data.csv'

#file open in pd dataframe
file_pd = pd.read_csv(file)
#check file_pd use line below
#print(file_pd)

#The total net amount of "Profit/Losses" over the entire period
total = file_pd['Profit/Losses'].sum()

#The greatest increase in profits (date and amount) over the entire period
new_column = file_pd['Profit/Losses'].diff()
max = new_column.max()
min = new_column.min()

#The average change in "Profit/Losses" between months over the entire period
average = new_column.sum()/85 #len("Profit/Losses")


#now let's print those darn months!!!!
file_pd['percent difference'] = new_column
#looping thru rows using iterrows function to count rows and print date
count = 0
for index, row in file_pd.iterrows():
    count = count + 1
    if row[2] == max:
        date1 = row[0]

    elif row[2] == min:
        date2 = row[0]

print('Total Months: ', count)
print('Total: $',total)
print(f'Average  Change: ${average:.2f}')
print('Greatest Increase in Profits: ', date1, '(',max,')')
print('Greatest Decrease in Profits: ', date2, '(',min,')')


#save terminal output as textfile
output_path = os.path.join('summary_text.txt')
with open(output_path, 'w', newline='') as txtfile:

    txtfile.write(f'Total Months: {count} \n')
    txtfile.write(f'Total: $ {total} \n')
    txtfile.write(f'Average  Change: $ {average:.2f} \n')
    txtfile.write(f'Greatest Increase in Profits: {date1} ({max}) \n')
    txtfile.write(f'Greatest Decrease in Profits: {date2} ({min}) \n')
