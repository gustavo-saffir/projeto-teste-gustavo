# Projeto - Medido de Velocidade
'''
Levando em consideração a velocidade máxima permitida de 80km em uma detereminada rua. Crie um programa que recebe do usuário um valor que representa a velocidade e com base nessa velocidade diga se ela tomou uma multa leve, grave ou gravissima. Levando em consideração que se a pessoa estiver abaixo da velocidade máxima, seu programa deve exibir: "não houve multa", caso esteja até 10km acima, exibir: "levou multa leve", caso esteja entre 11 a 20km acima da velocidade máxima, exibir: "levou multa grave" e caso esteja acima de 20km acima da velocidade máxima, exiba: levou multa gravíssima"


'''

# Método 5Q's para montar um algoritimo:
'''
(Tente explicar este problema para voce mesmo em voz alta e peça mais informações/investigue mais até você compreender completamente o problema.)

1. Quais são os dados de entrada necessários?
- velocidade_maxima = 80km
- input com velocidade do usuario

2. O que devo fazer com estes dados?
- comparar se ele levou uma multa, e caso seja sim, de qual natureza leve, grave ou gravissima.

3. Quais são as restrições deste problema?
- tem q ser numero inteiro
- tem q ser maior do que zero

4. Qual é o resultado esperado?
- apontar diante das porcentagens qual ocorrencia aconteceu

5. Qual é sequência de passos a ser feitas para chegar ao resultado esperado?
- velocidade_max = 80
- condutor = int(input('Qual a sua velocidade?    '))
- if condutor < velocidade_max:
-   print('Não houve multa')
- elif condutor >= velocidade_max + 10
-   print('levou multa leve')
- elif condutor >= velocidade_max + 11 e condutor <= velocidade_max + 11
-   print('levou multa grave')
- elif condutor > velocidade_max + 20
-   print('levou multa gravissima')
'''

velocidade_max = 80
condutor = int(input('Qual a sua velocidade?    '))
if condutor <= velocidade_max:
    print('Não houve multa')
elif condutor > velocidade_max and condutor <= velocidade_max + 10:
    print('levou multa leve')
elif condutor >= velocidade_max + 11 and condutor <= velocidade_max + 11:
    print('levou multa grave')
elif condutor > velocidade_max + 20:
    print('levou multa gravissima')