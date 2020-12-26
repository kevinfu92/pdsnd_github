import pandas as pd

df = pd.read_csv('chicago.csv')
df['Start Time'] = pd.to_datetime(df['Start Time'])
df['hour'] = df['Start Time'].dt.hour
df['hour'] = df['Start Time'].dt.hour
df['month'] = df['Start Time'].dt.month
df['day'] = df['Start Time'].dt.dayofweek

for i in df['User Type'].value_counts():
    print(i)


    
