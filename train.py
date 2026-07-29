import csv

mileages = []
prices = []

with open('data.csv', mode='r') as file:
    reader = csv.reader(file)
    
    next(reader)
    
    for row in reader:
        mileages.append(float(row[0]))
        prices.append(float(row[1]))
        

print("Kms importados: ", mileages)
print("Precos importados: ", prices)

norm_mileages = []
norm_prices = []

min_mileage = min(mileages)
max_mileage = max(mileages)

min_price = min(prices)
max_price = max(prices)

for km in mileages:
    norm_km = (km - min_mileage) / (max_mileage - min_mileage)
    norm_mileages.append(norm_km)
    
for pc in prices:
    norm_pc = (pc - min_price) / (max_price - min_price)
    norm_prices.append(norm_pc)
    
print("\nDados normalizados:\n")
print("kms normalizados: ", norm_mileages)
print()
print("Precos normalizados: ", norm_prices)