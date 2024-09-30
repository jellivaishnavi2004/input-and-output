'''
It was in the 1997-98 season that Ranchi saw the rise of the Captain Cool in the interschool trophy between DAV Jawahar Vidhya Mandir and Kendriya School. It was in that match Dhoni convinced Banerjee to be the opener and justified it with a double century.
Write a program to display the details of the match with Team name, Scores of the team and Overs played.
Input and Output Format:  
Refer sample input and output for formatting specifications.
[All text in bold corresponds to input and the rest corresponds to output]
'''

def display_match_details():
    # Input for Team 1
    print("Team 1:")
    team1_name = input("Team Name:\n")
    team1_score = input("Score:\n")
    team1_overs = input("Overs played:\n")
    
    # Input for Team 2
    print("Team 2:")
    team2_name = input("Team name:\n")
    team2_score = input("Score:\n")
    team2_overs = input("Overs played:\n")
    
    # Displaying Match Details
    print("Match Details:")
    print("Team 1:")
    print(f"Name: {team1_name}")
    print(f"Score: {team1_score}")
    print(f"Overs played: {team1_overs}")
    print("Team 2:")
    print(f"Name: {team2_name}")
    print(f"Score: {team2_score}")
    print(f"Overs played: {team2_overs}")

# Call the function to display match details
display_match_details()
