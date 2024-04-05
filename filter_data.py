import pandas as pd

# Load the data
df = pd.read_csv('CAS_Data.csv')

# Filter the data
filtered_df = df[df['tlaName'] == 'Christchurch City']

# Save the filtered data to a new CSV file
filtered_df.to_csv('CHCH_CAS_Data.csv', index=False)