import pandas as pd

# Load the CSV file
file_path = 'data.csv'
data = pd.read_csv(file_path)

# Display the first few rows of the DataFrame
print("Data Preview:")
print(data.head())

# Calculate the average age
average_age = data['Age'].mean()
print(f"\nAverage Age: {average_age}")

# Calculate the average salary
average_salary = data['Salary'].mean()
print(f"Average Salary: {average_salary}")

# Find the maximum salary
max_salary = data['Salary'].max()
print(f"Maximum Salary: {max_salary}")

# Find the minimum salary
min_salary = data['Salary'].min()
print(f"Minimum Salary: {min_salary}")

# Count the number of entries
entry_count = data.shape[0]
print(f"Number of Entries: {entry_count}")

# Display basic statistics
print("\nBasic Statistics:")
print(data.describe())