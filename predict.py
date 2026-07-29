import os
import json

theta0 = 0.0
theta1 = 0.0
min_price = 0.0
max_price = 1.0
min_km = 0.0
max_km = 1.0

if os.path.exists('modelo.json'):
    with open('modelo.json', 'r') as file:
        modelo = json.load(file)
        theta0 = modelo['theta0']
        theta1 = modelo['theta1']
        min_price = modelo['min_price']
        max_price = modelo['max_price']
        min_km = modelo['min_km']
        max_km = modelo['max_km']

else:
    print("Modelo ainda nao foi treinado")
    
try:
	km_input = float(input("Digite a quilometragem do carro que deseja prever o valor: "))
except ValueError:
    print("Digite um valor valido!")
    
if theta0 == 0.0 and theta1 == 0.0:
    real_price = 0.0

else:
    km_norm = (km_input - min_km) / (max_km - min_km)
    norm_price = theta0 + (theta1 * km_norm)
    real_price = (norm_price * (max_price - min_price)) + min_price
    
print(f"\nO valor estimado para um carro com {km_input} km rodados e de {real_price:.2f}")