import pandas as pd
url = 'https://raw.githubusercontent.com/dtandev/coronavirus/master/data/CoronavirusPL%20-%20Timeseries.csv'
df = pd.read_csv(url, error_bad_lines=False)

# All infections
numOfRows = df.shape[0]
print('Number of people infected: ', numOfRows)

# Check how many people infected in Lodz

count = df['City'].value_counts()
print(count)
