#Ler uma temperatura em graus Fahrenheit, calcular e escrever o valor
#equivalente em graus Celsius. A conversão é dada por:
#Onde:
#oC: temperatura em graus Celsius
#oF: temperatura em graus Fahrenheit


fahrenheit = float(input('Temperatura em °F: '))
celsius = ((5 * (fahrenheit - 32)) / 9)
print(f'A temperatura em °C é de: {celsius:.2f}')
