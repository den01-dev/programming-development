from entries import enter_team, enter_individual
from scores import enter_team_score, enter_individual_score
from results import view_results

def main():
  print("What would you like to do?\n\n[1] Enter a team\n\n[2] Enter an individual\n\n[3] Enter a team score\n\n[4] Enter an individual score\n\n[5] View results\n\n")

  run_type = int(input("Enter selection: "))

  if run_type == 1:
    enter_team()
  elif run_type == 2:
    enter_individual()
  elif run_type == 3:
    enter_team_score()
  elif run_type == 4:
    enter_individual_score()
  elif run_type == 5:
    view_results() 
  else:
    print("Sorry, I didn't quite catch that!")

if __name__ == '__main__':
  main()
