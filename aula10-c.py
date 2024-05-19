# Estrutura básica de uma função

# Exemplo de função que processa, e tem parametro:
def eh_maior_de_idade(possui_cnh):
    idade = int(input('Digite a sua idade:  '))
    if idade >= 18 and possui_cnh == True:
        print('Você é maior de idade e pode dirigir')
    else:
        print('Você não pode dirigir')

eh_maior_de_idade(possui_cnh=True)