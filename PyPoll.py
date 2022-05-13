#Add our dependencies.
import csv
import os
#Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
#create a variable to save a file from a path
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Open the election results and read the file
with open(file_to_load) as election_data:
    # To do: read and analyze the data here
    file_reader = csv.reader(election_data)
    # print the header row
    headers = next(file_reader)
    print(headers)
