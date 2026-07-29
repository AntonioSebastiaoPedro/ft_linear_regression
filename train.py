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
    
print("\n--- Dados Normalizados ---")
print("Primeiras 3 Quilometragens:", norm_mileages[:5])
print("Primeiros 3 Preços:", norm_prices[:5])


# --- Inicio da descida do gradiente ---
learning_rate = 0.1
epochs = 1000
theta0 = 0.0
theta1 = 0.0
m = len(norm_mileages)

print("\nIniciando o treinamento...")

for time in range(epochs):
    sum_error_theta0 = 0
    sum_error_theta1 = 0
    
    for i in range(m):
        estimate_price = theta0 + (theta1 * norm_mileages[i])
        error = estimate_price - norm_prices[i]
        sum_error_theta0 += error
        sum_error_theta1 += error * norm_mileages[i]
        
    temp_theta0 = learning_rate * (1/m) * sum_error_theta0
    temp_theta1 = learning_rate * (1/m) * sum_error_theta1
    
    theta0 = theta0 - temp_theta0
    theta1 = theta1 - temp_theta1
    
# --- FIM DO TREINAMENTO ---

print("Treinamento concluido com sucesso")
print(f"Theta0 final (normalizado): {theta0}")
print(f"Theta1 final (normalizado): {theta1}")