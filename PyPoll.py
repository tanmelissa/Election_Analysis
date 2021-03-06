#Add our dependencies.
import csv
import os
#Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
#create a variable to save a file from a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize a total vote counter
total_votes = 0

#Make a list of candidates
candidate_options = []

#Make a dictionary of candidates and votes
candidate_votes = {}

#winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0 

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # read the header row
    headers = next(file_reader)

    #Print each row in the csv file
    for row in file_reader:
        #add to the total vote count
        total_votes += 1

        #get candidate name from each row
        candidate_name = row[2]

        #add the candidate name to the candidate list
        if candidate_name not in candidate_options:

            #add to the list of candidates
            candidate_options.append(candidate_name)

            #Begins tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
        

        #add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

    #save the results to  our text file
    with open(file_to_save, "w") as txt_file:
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n")
        print(election_results, end ="")
        #save the final vote count to the text file
        txt_file.write(election_results)

        #iterate through the candidate list
        for candidate_name in candidate_votes:
            #retrieve vote count of a candidate
            votes = candidate_votes[candidate_name]
            #calculate the percentage of votes
            vote_percentage = (float(votes) /float(total_votes))*100
            #print the candidate name and percentage of votes
            #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

            #determine winning vote count and candidate
            # determine if the votes are greater than the winning count
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                #if true then set winning_count = cotes and winning_percentage = vote_percentage
                winning_count = votes
                winning_candidate = candidate_name
                winning_percentage = vote_percentage

            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            #print each candidate, their voter count, and a percentage to the terminal
            print(candidate_results)
            #save the results to our text file
            txt_file.write(candidate_results)

        winning_candidate_summary = (
            f"--------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"---------------------------\n")
        print (winning_candidate_summary)
        #save winning_candidate_summary to text file
        txt_file.write(winning_candidate_summary)
