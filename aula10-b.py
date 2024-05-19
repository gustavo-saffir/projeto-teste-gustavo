# Estrutura básica de uma função


# Crie um algoritimo que permite que maiores de idade entrem na festa

# Exemplo de função que processa e retorna algo
def pode_entrar_na_festa():
    idade = int(input('Digite a sua idade:  '))
    if idade >= 18:
        return True
    else:
        return False

if pode_entrar_na_festa() == True:
    print('Bem-Vindo a festa')
else:
    print('Você não pode entrar')  