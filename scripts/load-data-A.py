import os
import pandas as pd

# Read the location of the csv from the task input blob

input_name = "data_path"
input_location = f"/workflow/inputs/{input_name}"
print(f"input location@@@@@@ {input_location}")
try:

    with open(input_location, "r") as file:
        input_csv = file.read()
    print("it is in try block")
    # Read input csv to dataframe
    df = pd.read_csv(input_csv) 
except:
    with open("/mnt/code/data/datasetA.csv", "r") as file:
       df = pd.read_csv(file) 
    print("it is in except block")
    


# Write to Flow output
df.to_csv('/workflow/outputs/datasetA.csv', index=False)

