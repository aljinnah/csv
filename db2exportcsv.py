import sys
import csv

def build_dict_from_db2_file(file_path):
    '''
    Use case: This function works on mostly unstructured data file with a lots of key value pairs, same keys multiple values.
    it returns a dict object which can be converted to csv with some tweaks.
    
    Author: Mohammad Abu Al Jinnah
    '''
    result_dict = {}
    with open(file_path, 'r') as file:
        iter=0  # assuming the key found first as delimeter for row identification and before any row written, variable iter is 0.
        for line in file:
            line = line.strip()  # Remove leading/trailing whitespace
            if line and '=' in line: #splitting a line with delimeter "="
                keyy, val = line.split('=', 1)
                key=keyy.strip()     #stripping leading and trailing whitespace rom key
                value=val.lstrip().split(" ")[0]  #stripping leading whitespace and the splitting based on delimeter " ", taking the first part as value 

                if key in result_dict.keys():     # if key is already in the dict then appending value, in correct rows as indicated by iter value. 
                    while len(result_dict[key]) < iter:
                        result_dict[key].append("na")                        
                    result_dict[key].append(value)
                    iter=max(iter,(len(result_dict[key])-1))
                else:
                    result_dict[key] = [value]      #if key is virgin, then add key value in the dict and add trailing "na" values if necessary
                    while len(result_dict[key]) <= iter:
                        result_dict[key].insert(0,"na")

    return result_dict

def main():
    if not len(sys.argv) == 2 :
        print("Missing or inappropriate argument, exiting ...")
        sys.exit(1)

    file_path = sys.argv[1]  # Add file path as argument or Replace with hardcoded file path
    my_dict = build_dict_from_db2_file(file_path)
    print("Available column or keys from the data file:")
    for index, key in enumerate(my_dict):
        print(f"Index: {index}, Key: {key}")

    pk=input("\nChoose primary key index: ") 
    padl=len(my_dict[list(my_dict.keys())[int(pk)]])  # padding "na" is necessary to make sure [value] length same for all keys
    for k in my_dict.keys():
        while len(my_dict[k])<padl:
            my_dict[k].append("na")

    #print(my_dict)     # comment if dict is two big
    # Specify the output CSV file name
    csv_file = "db2dictoutput.csv"

    # Open the CSV file in write mode
    with open(csv_file, 'w', newline='') as file:
        # Create a CSV writer object
        writer = csv.writer(file)
        print("\nExporting datafile to CSV ...")
        # Write the header row (keys of the dictionary)
        writer.writerow(my_dict.keys())
        # Write the data rows (values of the dictionary)
        writer.writerows(zip(*my_dict.values()))
        print("Done, output file db2dictoutput.csv generated in current directory")

if __name__== "__main__":
    main()