'''
    velocidade_maxima = 100
    multa_leve = 180
    multa_grave = 550
    multa_gravissima = 1500
'''

# CamelCase
class Radar:
  def __init__(self, vel_max, mul_leve, mul_grave, mul_gravi):
    self.vel_max = vel_max
    self.mul_leve = mul_leve
    self.mul_grave = mul_grave
    self.mul_gravi = mul_gravi
  # A função deve exibir o valor da multa que será aplicada, de acordo com o nível da multa
  def obter_valor_multa(self, nivel_multa):
    if nivel_multa == 'multa leve':
      print(f'O valor da multa leve é R${self.mul_leve}')
    elif nivel_multa == 'multa grave':
      print(f'O valor da multa grave é R${self.mul_grave}')
    else:
      print(f'O valor da multa gravissima é R${self.mul_gravi}')
  # A função deve exibir qual multa que será aplicada, de acordo com a velocidade
  def calcular_multa(self, velocidade):
    if velocidade <= self.vel_max:
        print('Nao levou multa')
    elif velocidade > self.vel_max and velocidade <= self.vel_max + 10:
        print('Levou multa leve')
    elif velocidade >= self.vel_max + 11 and velocidade <= self.vel_max + 20:
        print('Levou multa grave')
    elif velocidade > self.vel_max + 20:
        print('Levou multa gravissima')
  # A função deve exibir qual penalidade na carteira, de acordo com a velocidade
  def aplicar_penalizacao_carteira(self, nivel_multa):
    if nivel_multa == 'Multa leve':
      print('Perdeu 3 pontos na carteira')
    elif nivel_multa == 'Multa grave':
      print('Perdeu 5 pontos na carteira')
    else:
      print('Perdeu 7 pontos na carteira')
      
radar1 = Radar(vel_max=100, mul_leve=180, mul_grave=550, mul_gravi=1500)

#ou assim ->   radar1 = Radar(100, 180, 550, 1500)
# print(radar1.vel_max)
#radar1.obter_valor_multa('multa leve')
#radar1.obter_valor_multa('multa grave')
#radar1.obter_valor_multa('')
#radar1.calcular_multa(320)

radar1.aplicar_penalizacao_carteira('Multa leve')