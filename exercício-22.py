#22 - Ler um valor e escrever se é par ou ímpar.


numero = int(input("Digite seu número aqui: "))
par = numero % 2
if par == 0:
    print('Esse número é par!')
else:
    print('Esse número é impar!')
