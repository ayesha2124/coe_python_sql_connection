import pandas as pd

# Define column names and an empty DataFrame
columns = ['cnum', 'name', 'age','gender']
df = pd.DataFrame(columns=columns)

# Save as a CSV file
df.to_csv('customer_data1.csv', index=False)
# New rows to insert
new_data = [
    {'cnum': 2001, 'name': 'Bob', 'age': 30, 'gender': 'male'},
    {'cnum': 2002, 'name': 'Charlie', 'age': 28, 'gender': 'male'},
    {'cnum': 2003, 'name': 'Diana', 'age': 24, 'gender': 'female'},
    {'cnum': 2004, 'name': 'Eve', 'age': 29, 'gender': 'female'},
    {'cnum': 2006, 'name': 'Frank', 'age': 35, 'gender': 'male'}
]
# Convert new data to a DataFrame
df_new = pd.DataFrame(new_data)

# Append to existing CSV file
df_new.to_csv('customer_data1.csv', mode='a', index=False, header=False)

print("Rows inserted into 'customer_data1.csv' successfully!")

print("CSV file 'customer_data1.csv' created successfully!")
