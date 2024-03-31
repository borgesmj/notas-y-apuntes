import csv 

with open("Day54Totals.csv") as file: 
  reader = csv.DictReader(file) 
  netTotal = 0
  for row in reader: 
    sellTotal = float(row['Cost']) * int(row['Quantity'])
    netTotal += sellTotal

print(f"""
🌟Shop $$ Tracker🌟 

Your shop took £{round(netTotal, 2)} pounds today.
""")