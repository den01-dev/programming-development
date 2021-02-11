import csv

def enter_team_score():

  with open('src/results.csv','r') as f:
    all_results = f.read().splitlines()
    print(all_results)
    
team_1 = input("Team 1: ")
  team_two = input("Team 2: ")

  team_one_score = int(input("Team 1 score: "))
  team_two_score = int(input("Team 2 score: "))

  if team_one_score > team_two_score:
    print(f"{team_one} beat {team_two}. Score: {team_one_score} vs {team_two_score})
  elif team_two_score > team_one_score:
    print(f"{team_two} beat {team_one}. Score: {team_two_score} vs {team_one_score}")
  else:
    print(f"{team_one} and {team_two} drew! Score: {team_one_score} vs {team_two_score}")  

  with open('src/results.csv','a') as f:
      writer = csv.writer(f)
      writer.writerow([team_one,team_one_score,team_two_score,team_two)      

def enter_individual_score():
  print("This function hasn't been set up yet!")
