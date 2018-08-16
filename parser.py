import pandas as pd

# Read in run data
run_data = pd.read_csv('rundata.csv')
print(run_data.head())

# Read in shoe data
shoe_data = pd.read_csv('shoedata.csv')
print(shoe_data.head())