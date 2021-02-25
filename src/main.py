from entries import enter_team
from scores import enter_team_score
from results import view_team_results, view_team_table

def main():
  print("Which version would you like to run?\n\n[1] Team\n\n[2] Individual\n\n")

  run_type = int(input("Enter selection: "))

  if run_type == 1:
    run_team()
  elif run_type == 2:
    run_individual()
  else:
    print("Sorry, I didn't quite catch that!")

def run_team():

  print("What would you like to do?\n\n[1] Make an entry\n\n[2] Enter a score \n\n[3] View results\n\n[4] View table\n\n")

  run_type = int(input("Enter selection: "))

  if run_type == 1:
    enter_team()
  elif run_type == 2:
    enter_team_score()
  elif run_type == 3:
    view_team_results()
  elif run_type == 4:
    view_team_table()
  else:
    print("Sorry, I didn't quite catch that!")

def run_individual():
  
  print("This function isn't set up yet!")

if __name__ == '__main__':
  main()
