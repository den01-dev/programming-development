from entries import enter_team, enter_individual
from results import view_results

def main():
  print("What would you like to do?\n\n[1] Enter a team\n\n[2] Enter an individual\n\n[3] View results\n\n")

  run_type = int(input("Enter selection: "))

  if run_type == 1:
    enter_team()
  elif run_type == 2:
    enter_individual()
  else:
    view_results() 

if __name__ == '__main__':
  main()