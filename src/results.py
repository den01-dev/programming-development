def view_team_results():

  with open('src/team_results.csv','r') as f:
    team_results = f.read().splitlines()
    print(team_results)

def view_team_table():

  with open('src/team_table.csv','r') as f:
    team_table = f.read().splitlines()
    print(team_table)    

def view_individual_results():

  print("This function hasn't been set up yet!")

def view_individual_table():

  print("This function hasn't been set up yet!")