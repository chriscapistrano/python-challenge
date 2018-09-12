

import pandas as pd

file = 'employee_data.csv'
file_pd = pd.read_csv(file)
file_pd.head()
file_pd.dtypes

#change State to state abbreviations (e.g., Florida to FL)
State = file_pd['State'].replace({
                                      'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',})

file_pd['State'] = State
#del file_pd['State']
file_pd.head()

#The Name column should be split into separate First Name and Last Name columns.
file_pd['First Name'], file_pd['Last Name'] = file_pd['Name'].str.split(' ', 1).str
del file_pd['Name']
file_pd.head()

#The DOB data should be re-written into MM/DD/YYYY format
file_pd['DOB'] = pd.to_datetime(file_pd.DOB)
file_pd['DOB'] = file_pd['DOB'].dt.strftime('%m/%d/%Y')
#del file_pd['DOB']
file_pd.head()

#The SSN data should be re-written such that the first five numbers are hidden from view

file_pd['SSN'] = file_pd['SSN'].astype(str)
file_pd.dtypes

file_pd['SSN'] = file_pd['SSN'].str[7:]
file_pd['SSN'] = str('***-**-') + file_pd['SSN']
file_pd.head()

#reorder to this Emp ID,First Name,Last Name,DOB,SSN,State
file_pd = file_pd[['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State']]
file_pd.head()

file_pd.to_csv('clean_file.csv')
