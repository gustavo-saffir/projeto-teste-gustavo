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

radar1 = Radar(100, 180, 550, 1500)
#ou assim ->   radar1 = Radar(vel_max=100, mul_leve=180, mul_grave=550, mul_gravi=1500)
print(radar1.vel_max)
print(radar1.mul_leve)
print(radar1.mul_grave)
print(radar1.mul_gravi)


radar2 = Radar(120, 280, 750, 2500)
#ou assim ->   radar1 = Radar(vel_max=120, mul_leve=280, mul_grave=750, mul_gravi=2500)
print(radar1.vel_max)
print(radar1.mul_leve)
print(radar1.mul_grave)
print(radar1.mul_gravi)