# csv
This repository contains python program to deal with CSV files. 
Comparing csv files using compare_pandas_csv1_csv2.py required pandas installed in workstation.

pip install pandas

compare_pandas_csv1_csv2.py require four commandline argument to compare two csv files.
Lets assume we have a target.csv file with information in column 0 which need to be compared with a result.csv file with information in column 2.
Then the program should run in the approach outlined below:

 compare_pandas_csv1_csv2.py target.csv 0 result.csv 2

Running this command will produce two output files.

missing_in_result_comparing_target.csv will contain information which is found in target.csv but not in result.csv in their respective columns.

matching_in_result_comparing_target.csv will contain information which is found both in target.csv and result.csv in their respective columns.




