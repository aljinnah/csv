Readme:

Script contains a function to convert unstructured key value datafile into a structured python key value object.
  
Use case: This function works on mostly unstructured data file with a lots of key value pairs, same keys multiple values.
    it returns a dict object which can be converted to csv with some tweaks.
    
    Author: Mohammad Abu Al Jinnah

Script run: In the CLI issue the following command:
python db2exportcsv.py example_key_value_text_file.txt

Script name is db2exportcsv.py
We need to provide the text file path as argument. Its better to keep the script and the text file in the same folder, so we won't have to provide the full path of the files.

Example text file might contain key value pair like below:

k1=m1
k2=m2
k3 = m3 z1=n1
k4=m4
k5=m5 

k1=v1
k2=v2
k3=v3
k4=v4

k1=v11
k2=v22
k3=v33
k4=v44

This will export a CSV with column k1, k2, k3, k4, k5
Note , in the script K1 or the first key is the delimiter to separate rows of data. So when prompted by the script to select primary key index: select 0.
It can be changed to other keys but it might address bug which need to be addressed later.    


