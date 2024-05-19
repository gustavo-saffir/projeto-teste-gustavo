# Desafio - Transforme o código abaixo em uma função
'''
velocidade = int(input('Digite sua velocidade:  '))

velocidade_maxima = 80

if velocidade <= velocidade_maxima:
    print('Nao levou multa')

elif velocidade > velocidade_maxima and velocidade <= velocidade_maxima + 10:
    print('Levou multa leve')

elif velocidade >= velocidade_maxima + 11 and velocidade <= velocidade_maxima + 20:
    print('Levou multa grave')

elif velocidade > velocidade_maxima + 20:
    print('Levou multa gravissima')
'''   

# Resolvendo:

def controle_de_velocidade(velocidade_maxima):
    velocidade = int(input('Digite sua velocidade:  '))

    if velocidade <= velocidade_maxima:
        print('Nao levou multa')
    elif velocidade > velocidade_maxima and velocidade <= velocidade_maxima + 10:
        print('Levou multa leve')
    elif velocidade >= velocidade_maxima + 11 and velocidade <= velocidade_maxima + 20:
        print('Levou multa grave')
    elif velocidade > velocidade_maxima + 20:
        print('Levou multa gravissima')

controle_de_velocidade(80)