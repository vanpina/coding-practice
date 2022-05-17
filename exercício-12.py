#Ler o salário mensal de uma pessoa e o percentual de reajuste, calcular e
#escrever o valor do salário reajustado.


salario_mensal = float(input('Digite seu salário mensal: R$'))
percentual = float(input("Digite seu percentual de reajuste: "))
novo_salario= salario_mensal + (salario_mensal * percentual / 100)
print(f'O preço com desconto será: R${(novo_salario):.2f}')

