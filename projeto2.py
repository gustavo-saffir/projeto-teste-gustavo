# Projeto - Chute o número
'''
Escreva um programa que, ao iniciar gera um valor aleatório de 1 a 10 e permite que o usuario chute um número até que o valor aleatório gerado no inicio do programa seja chutado corretamente.

O programa deve informar se o chute foi acima, abaixo ou igual ao valor aleatorio gerado no inicio do progama.
'''

# Método 5Q's para montar um algoritimo:
'''
(Tente explicar este problema para voce mesmo em voz alta e peça mais informações/investigue mais até você compreender completamente o problema.)

1. Quais são os dados de entrada necessários?
- valor aleatório de 1 a 10
- chute do usuario

2. O que devo fazer com estes dados?
- eu devo comparar o chute do usuario com o valor aleatorio que foi gerado no inico do programa e dizer se o chute foi maior, menor ou igual ao valor que foi gerado no inicio do programa.

3. Quais são as restrições deste problema?
- nao pode ser maior que 10
- maior que 0

4. Qual é o resultado esperado?
- o resultado esperado é que o programa deve informar se o chute foi acima, abaixo ou igual ao valor aleatorio gerado no inicio do progama.

5. Qual é sequência de passos a ser feitas para chegar ao resultado esperado?
- input valor_aleatorio de 1 a 10
- input chute 
- if chute > valor_aleatorio:
-   print('O chute foi maior que o valor gerado.') 
- elif chute < valor_aleatorio:
-   print('O chute foi menor que o valor gerado.')
- else:
-   print('Você acertou!')
'''
import random

valor_aleatorio = random.randint(1,10)
acertou = False
while acertou == False:
    chute = int(input('Chute um valor de 1 a 10:    '))
    if chute > valor_aleatorio:
        print('O chute foi maior que o valor gerado.') 
    elif chute < valor_aleatorio:
        print('O chute foi menor que o valor gerado.')
    else:
        acertou = True
        print('Você acertou!')





