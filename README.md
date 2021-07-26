# Election_Analysis

## Project Overview
A Colorado Board Elections employee has given the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes that were cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code 1.58.1

## Summary
The analysis of the election show that:
- There were **369,711** votes cast in the election.
- County Turnout:
  - Jefferson county had **10.5%** of the vote and **38,855** number of votes.
  - Denver county had **82.8%** of the vote and **306,055** number of votes.
  - Arapahoe county had **6.7%** of the vote and **24,801** number of votes.
- Largest County Turnout:
  - Denver county had the largest number of votes with **306,055** votes.
- Candidates:
  - Diana DeGette
  - Charles Casper Stockham
  - Raymon Anthony Doane
- Candidate's Results:
  - Diana Degette received **73.8%** of the vote and **272,892** number of votes.
  - Charles Casper Stockham received **23.0%** of the vote and **85,213** number of votes.
  - Raymon Anthony Doane received **3.1%** of the vote and **11,606** number of votes.
- Winner of the Election:
  - Candidate Diana Degette, who received **73.8%** of the vote and **272,892** number of votes.

## Election Audit Summary
This script has the ability to be used for any election. One option to modify the script so it can better serve other elections is that it can also pull the largest county vote percentage and vote count. This can be useful in the situation with a long list of counties where it can be difficult to locate the county with the largest turnout. Another option to modify the script is to include a breakdown of the different voting methods, mail-in ballots, voting machines, paper ballots etc. We can do a similar breakdown as with the other categories, include a percentage and vote count for each method. This script is flexible and can be modified for any election.
