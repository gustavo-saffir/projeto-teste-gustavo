# Projeto - Fatorial

# Método 5Q's para montar um algoritimo:

'''
Analise criticamente o problema e descubra:
(Tente explicar este problema para voce mesmo em voz alta e peça mais informações/investigue mais até você compreender completamente o problema.)

1. Quais são os dados de entrada necessários?
- numero

2. O que devo fazer com estes dados?
- eu devo calcular o fatorial do numero que for passado para o meu programa e exibir na tela.

3. Quais são as restrições deste problema?
- o numero deve ser um valor positivo
- o numero deve ser um valor inteiro

4. Qual é o resultado esperado?
- o resultado neste caso é que o fatorial do numero providenciado seja exibido.

5. Qual é sequência de passos a ser feitas para chegar ao resultado esperado?
- input numero
- if numero > 0
- if numero = inteiro
- fatorial = 1
- loop de 1 ate o numero
--- fatorial = fatorial * numero
- print(fatorial) 
'''

numero = int(input('Digite um número?  '))
if numero > 0:
    fatorial = 1
    for item in range(1, numero + 1):
        fatorial = fatorial * item
    print(fatorial)



