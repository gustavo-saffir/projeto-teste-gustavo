# Condicionais
# If, elif e else

 
'''
Eu cheguei atrasado na aula, ainda posso entrar?
Se essa não for sua terceira vez chegando atrado então pode sim, caso contrário irá tomar uma suspensão.
'''
numero_de_atrasos = 0
if numero_de_atrasos >= 3:
    print('Você está suspenso!')
elif numero_de_atrasos == 1:
    print('Pode entrar porem caso tome mais 2 faltas, irá ser suspenso!')
elif numero_de_atrasos == 2:
    print('Pode entrar mas caso toma mais 1 falta, será suspenso!')
else:
    print('Pode entrar')