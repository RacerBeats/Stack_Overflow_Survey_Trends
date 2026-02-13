import pandas as pd

data = pd.read_csv("developer_dataset.csv")
print(data.columns)
print(data.count())
print(data.describe())

'''
Initial analysis of data so far:

we have a total of 111209 slots of data. There's some missing
data after running data.count() and data.describe(). 

some slots like org size or new job hunt columns are missing a LOT
of people. Unlikely that stat analysis using these would be good.
Can safely remove columns with ~60% + worth of missing data
'''

maxRows = data['RespondentID'].count()
print('% missing data:')
print((1- data.count() / maxRows) * 100)

#NEWJobHunt, NEWJobHuntResearch, and NEWLearn are above 60% missing
data.drop(['NEWJobHunt','NEWJobHuntResearch', 'NEWLearn'],
    axis=1,
    inplace=True)

print(f'\nafter drop: \n{data.columns}')