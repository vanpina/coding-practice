#23 - Ler dois valores e escrever o maior deles.
#24 - Ler três valores e escrever o menor deles.



a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))
#VERIFICANDO QUEM É O MENOR
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
#VERIFICANDO QUEM É O MAIOR
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print(f"O menor valor digitado é {menor}\nO maior valor digitado é {maior}")


