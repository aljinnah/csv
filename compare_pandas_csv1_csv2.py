
import pandas as pd
import sys

print(sys.argv[1])
print(sys.argv[2])
print(sys.argv[3])
print(sys.argv[4])

# Load the CSV files
file1 = pd.read_csv(sys.argv[1])
file2 = pd.read_csv(sys.argv[3])

# Extract the relevant columns
column1_file1 = file1.iloc[:, int(sys.argv[2])].str.upper()  # Column 1 from file1
column3_file2 = file2.iloc[:, int(sys.argv[4])].str.upper()  # Column 3 from file2

# Find values in column1_file1 that are not in column3_file2
missing_values = column1_file1[~column1_file1.isin(column3_file2)]
matching_values = column1_file1[column1_file1.isin(column3_file2)]

# Print the missing values
if not missing_values.empty:
    print("Values in column 0 of file1 not found in column 2 of file2:")
    print(missing_values.to_string(index=False))
else:
    print("All values in column 1 of file1 are found in column 3 of file2.")

# write the output to a new csv
missing_values.to_csv(r'./missing_in_result_comparing_target.csv', sep='\t', encoding='utf-8')
matching_values.to_csv(r'./matching_in_result_comparing_target.csv', sep='\t', encoding='utf-8')