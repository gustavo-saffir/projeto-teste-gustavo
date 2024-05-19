velocidade_maxima = 100
multa_leve = 180
multa_grave = 550
multa_gravissima = 1500

def calcular_multa(velocidade,velocidade_maxima):
  if velocidade <= velocidade_maxima:
      print('Nao levou multa')

  elif velocidade > velocidade_maxima and velocidade <= velocidade_maxima + 10:
      print('Levou multa leve')

  elif velocidade >= velocidade_maxima + 11 and velocidade <= velocidade_maxima + 20:
      print('Levou multa grave')

  elif velocidade > velocidade_maxima + 20:
      print('Levou multa gravissima')


def aplicar_penalizacao_carteira(nivel_multa):
  if nivel_multa == 'Multa leve':
    print('Perdeu 3 pontos na carteira')
    
  elif nivel_multa == 'Multa grave':
    print('Perdeu 5 pontos na carteira')
    
  else:
    print('Perdeu 7 pontos na carteira')

'''
# CamelCase - a primeira letra maiuscula
class Radar:
    pass

# Para usar uma classe, é necessário "instanciar ela" - Exemplo
rada1 = Radar(60) //e aqui eu posso parametrizar de acordo com a minha vontade, ex 60km por hora
rada2 = Radar(80) //e aqui eu posso parametrizar de acordo com a minha vontade, ex 80km por hora
rada3 = Radar(100) //e aqui eu posso parametrizar de acordo com a minha vontade, ex 100km por 
'''

