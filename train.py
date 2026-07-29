import csv

mileages = []
prices = []

with open('data.csv', mode='r') as file:
    reader = csv.reader(file)
    
    next(reader)
    
    for row in reader:
        mileages.append(row[0])
        prices.append(row[1])
        

print("Kms importados: ", mileages)
print("Precos importados: ", prices)