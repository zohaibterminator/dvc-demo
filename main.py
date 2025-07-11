import pandas as pd
import os

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}

df = pd.DataFrame(data)

new_row_data = {"Name": "Emily", "Age": 22, "City": 'Newark'}
df.loc[len(df)] = new_row_data

another_new_row_data = {"Name": "Emma", "Age": 19, "City": "Lalukhet"}
df.loc[len(df)] = another_new_row_data

output_file = "output.csv"
dir_path = os.getcwd() + '/data'

if not os.path.exists(dir_path):
    print("Creating 'data' directory")
    os.makedirs(dir_path)

df.to_csv(dir_path + '/' + output_file, index=False)

if os.path.exists(dir_path + '/' + output_file):
    print(f"File '{output_file}' created successfully.")