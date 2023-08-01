import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV files
csv_file1 = 'path\\2y_usage.csv'
csv_file2 = 'path\\2y_generation.csv'

df1 = pd.read_csv(csv_file1)
df2 = pd.read_csv(csv_file2)

# Convert the 'Period' column to datetime format
df1['Period'] = pd.to_datetime(df1['Period'], format='%b-%y')
df2['Period'] = pd.to_datetime(df2['Period'], format='%b-%y')

# Sort the dataframes based on the 'Period' column
df1 = df1.sort_values(by='Period')
df2 = df2.sort_values(by='Period')

# Plot the data
plt.style.use('dark_background')  # Set the background to dark
plt.figure(figsize=(10, 6))  # Set the figure size

# Plot the data from the first CSV file as a red line
plt.plot(df1['Period'], df1['Usage_kwh'], color='red', label='Usage_kwh')

# Plot the data from the second CSV file as a yellow line
plt.plot(df2['Period'], df2['Generated_kwh'], color='yellow', label='Generated_kwh')

# Set the labels color to white
plt.xlabel('Period', color='white')
plt.ylabel('kWh', color='white')
plt.title('Comparison of Usage_kwh and Generated_kwh', color='white')

# Set the legend text color to white
plt.legend(loc='upper left', frameon=False, labels=['Usage_kwh', 'Generated_kwh'])

# Show the plot
plt.show()
