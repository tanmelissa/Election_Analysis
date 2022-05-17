# Election_Analysis
## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a reent local congressional election.

1. Calculate the toal nuber of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.6.1, Visual Studio Code, 1.38.1

## Election-Audit Results
The analysis of the election show that:
- There were 369,711 votes cast in the election
- The counties were:
    - Jefferson
    - Denver
    - Arapahow
- The number of votes per county were:
    - 10.5% of the votes (38,855 votes) came from Jefferson County
    - 82.8% of the votes (306,055 votes) came from Denver County
    - 6.7% of the votes (24,801 votes) came from Arapahoe County
- The county with the largest turnout:
    - Denver with 82.8% of the votes and 306,055 votes 
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham received 23.0% of the votes and 85,213 votes
  - Diana DeGette received 73.8% of the votes and 272,892 votes
  - Raymon Anthony Doane received 3.1% of the votes and 11,606 votes
- The winner of the election was:
  - Diana DeGette who received 73.8% of the votes and 272,892 votes

## Election-Audit Summary
This script can be used for any county election by changing the following items:
- The path to load the file with election data

<img width="377" alt="image" src="https://user-images.githubusercontent.com/102273449/168702698-cc3fcc66-e103-401f-b76a-5f4ab4d26339.png">

- The path to save the file that you will write the election results 

<img width="383" alt="image" src="https://user-images.githubusercontent.com/102273449/168702771-30b9cefa-e092-4c8e-a885-66d2d5ed8778.png">

This script could be used for larger elections (e.g. a presidencial election) as well by changing the following items in addition to the changes mentioned previously:
- Change the name of the county lists and dictionaries to be called state_list and state_votes

<img width="319" alt="image" src="https://user-images.githubusercontent.com/102273449/168703076-8b15c338-a73e-4365-b1ed-f4576d915fdc.png">

- Changing the variables for largest turnout to be called state instead of county

<img width="338" alt="image" src="https://user-images.githubusercontent.com/102273449/168703159-1d05df5a-b2c0-488b-8d19-fdc06ebad9b3.png">

- Changing the largest_county_results to say "Largest State Turnout"

<img width="347" alt="image" src="https://user-images.githubusercontent.com/102273449/168703296-d9e763df-64be-45aa-be66-3c56f010b2c3.png">

- Adding a section that would could electoral votes and could calculate the winner based on that and compare it to the winner based on popular vote
