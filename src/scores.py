import csv,pandas

def enter_team_score():
    
  team_one = input("Team 1: ")
  team_two = input("Team 2: ")

  team_one_score = int(input("Team 1 score: "))
  team_two_score = int(input("Team 2 score: ")) 

  with open('src/team_results.csv','a') as f:
      writer = csv.writer(f)
      writer.writerow([team_one,team_one_score,team_two_score,team_two])      

  df = pandas.read_csv('src/team_table.csv')

  if team_one_score > team_two_score:
    print(f"{team_one} beat {team_two}. Score: {team_one_score} vs {team_two_score}")
    df.loc[df['Team'] == team_one,'Wins'] += 1
    df.loc[df['Team'] == team_one,'Points'] += 3
    df.loc[df['Team'] == team_two,'Losses'] += 1
  elif team_two_score > team_one_score:
    print(f"{team_two} beat {team_one}. Score: {team_two_score} vs {team_one_score}")
    df.loc[df['Team'] == team_two,'Wins'] += 1
    df.loc[df['Team'] == team_two,'Points'] += 3
    df.loc[df['Team'] == team_one,'Losses'] += 1
  else:
    print(f"{team_one} and {team_two} drew! Score: {team_one_score} vs {team_two_score}")
    df.loc[df['Team'] == team_one,'Draws'] += 1
    df.loc[df['Team'] == team_two,'Draws'] += 1
    df.loc[df['Team'] == team_one,'Points'] += 1
    df.loc[df['Team'] == team_two,'Points'] += 1

  df.to_csv('src/team_table.csv',index=False)

def enter_individual_score():
  
  print("This function hasn't been set up yet!")