# Estrutura básica de uma função

# Exemplo de função que processa, porém não retorna algo
def eh_maior_de_idade():
    idade = int(input('Digite a sua idade:  '))
    if idade >= 18:
        print('Você é maior de idade')
    else:
        print('Você é menor de idade')

eh_maior_de_idade()