# Condicionais
# If, elif e else

'''
2º Problema: Ei , voce consegue me ajudar a mover essas caixas lá para fora hoje a tarde?
Se eu estiver livre, sim. Mas, se nao der pede meu irmao para te ajudar
'''
estou_livre = False
if estou_livre == True:
  print('Ok, posso ajudar hoje sim!')
else:
  print('Peça meu irmao para te ajudar!')
  
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