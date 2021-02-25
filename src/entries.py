import csv

def enter_team():

  with open('src/teams.csv','r') as f:    
    all_teams = f.read().splitlines()
    if not all_teams:
      print(f"The teams currently entered into the tournament are:\n {all_teams}\n")

  while True:
    team_name = input("What is the team name you would like to enter? ")
    team_size = int(input("How many people are in your team? "))
    team_members = [] # Initialise (set up to be ready) the list
  
    for team_member in range(1,team_size+1): # Add one to top of range
      team_members.append(input("Type the names of the people in your team: ")) # Add these names to a 'list'

    with open('src/teams.csv','a') as f:
      writer = csv.writer(f)
      writer.writerow([team_name,team_members])
    
    with open('src/team_table.csv','a') as f:
      writer = csv.writer(f)
      writer.writerow([team_name,0,0,0,0])

    all_teams.append(team_name)

    another_team = input("Do you want to enter another team? (Y/N) ")
    if another_team != 'Y':
      break
  
  print("The teams now entered into the tournament are:")
  print(all_teams)

def enter_individual():

  print("This function hasn't been set up yet!")
