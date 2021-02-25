def view_results():

  with open('src/results.csv','r') as f:
    all_results = f.read().splitlines()
    print(all_results)

def view_table():

  with open('src/table.csv','r') as f:
    full_table = f.read().splitlines()
    print(full_table)