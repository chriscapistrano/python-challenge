import os #just in case
import pandas as pd

#open using pd environment
file = 'election_data.csv'
file_pd = pd.read_csv(file)

#total votes
votes = file_pd['Voter ID'].count()

#unique candidate list
candidates = file_pd['Candidate'].unique()

#code below to check counts for each candidate and just get quick overview
can_count = file_pd['Candidate'].value_counts()

#comibine kha and Khan and save that new column as Clean Candidate
file_pd['Clean Candidate'] = file_pd['Candidate'].replace({'Kha': 'Khan', 'Khan': 'Khan'})

#compute candidate votes and percentage of votes
count_votes = file_pd['Clean Candidate'].value_counts()
percent_votes = (count_votes/votes)*100

#create new data frame to save computer variables above
new_table = pd.DataFrame({'Total Votes': count_votes,
                        'Vote Percentage': percent_votes})

#Vote percentage convert to only have 2 decimal places and inlcude percentage symbol
new_table['Vote Percentage'] = new_table['Vote Percentage'].map('{:,.2f}%'.format)

khan_perc = new_table.loc['Khan', 'Vote Percentage']
khan_vote = new_table.loc['Khan', 'Total Votes']
cor_perc = new_table.loc['Correy', 'Vote Percentage']
cor_vote = new_table.loc['Correy', 'Total Votes']
li_perc = new_table.loc['Li', 'Vote Percentage']
li_vote = new_table.loc['Li', 'Total Votes']
o_perc = new_table.loc["O'Tooley", 'Vote Percentage']
o_vote = new_table.loc["O'Tooley", 'Total Votes']

#look for highest percentage vote to determine winner
max = new_table['Vote Percentage'].max()

#look for the Winner
for index, row in new_table.iterrows():
    if row[1] == max:
        winner = index


print('Election Results')
print('--------------------------------')
print('Total Votes: ', votes)
print('--------------------------------')
print('Khan: ', khan_perc, khan_vote)
print('Correy: ', cor_perc, cor_vote)
print("Li: ", li_perc, li_vote)
print("O'Tooley: ", o_perc, o_vote)
print('--------------------------------')
print('Winner:', winner)
print('--------------------------------')

#save terminal out as a textfile 
output_path = os.path.join('poll_summary_text.txt')
with open(output_path, 'w', newline='') as txtfile:

    txtfile.write(f'Election Results \n')
    txtfile.write(f'-------------------------------- \n')
    txtfile.write(f'Total Votes: {votes} \n')
    txtfile.write(f'-------------------------------- \n')
    txtfile.write(f'Khan: {khan_perc} {khan_vote} \n')
    txtfile.write(f'Correy: {cor_perc} {cor_vote} \n')
    txtfile.write(f'Li: {li_perc} {li_vote} \n')
    txtfile.write(f"O'Tooley: {o_perc} {o_vote} \n")
    txtfile.write(f'-------------------------------- \n')
    txtfile.write(f"Winner: {winner} \n")
    txtfile.write(f'-------------------------------- \n')
