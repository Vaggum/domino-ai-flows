import os
import pandas as pd

# Read the location of the csv from the task input blob

input_name = "data_path"
input_location = f"/workflow/inputs/{input_name}"
print(f"input location@@@@@@ {input_location}")
try:
    with open(input_location, "r") as file:
        input_csv = file.read()
    print("it is in Try block")
except:
    print("it is in exception")
    with open("/mnt/code/data/datasetA.csv", "r") as file:
        input_csv = file.read()
# Read input csv to dataframe
print("this is input_csv",input_csv)
df = pd.read_csv(input_csv) 


# Write to Flow output
df.to_csv('/workflow/outputs/datasetA.csv', index=False)

