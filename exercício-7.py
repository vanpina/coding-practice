#07 - Ler o nome de uma pessoa na forma “nome” seguido por “sobrenome” e
#escrever na forma “sobrenome” seguido por “nome”. Exemplo:
#entrada: “Fulano”, “de Tal”
#saída: “de Tal”, “Fulano”

continuar = True
while continuar:
    nome = str(input('Digite seu nome e sobrenome: ')).strip()
    nome_completo = nome.split(" ", 1)
    primeiro_nome = False
    sobrenomes = False
    if len(nome_completo) > 1:
        primeiro_nome, sobrenomes = nome_completo
    else:
        primeiro_nome = nome_completo[0]
    if sobrenomes:
        print(f'Seu ultimo nome é {sobrenomes}')
    if primeiro_nome:
        print(f'Seu primeiro nome é {primeiro_nome}')
        continuar = False

