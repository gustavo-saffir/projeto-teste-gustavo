#Variaveis

#Números
velocidade_internet = 10
print(velocidade_internet)
nota_do_filme = 8.5 #float

# valores boleanos
esta_aberto = True
esta_fechado = False

# Strings
nome_do_curso = 'Lógica de Programação'

# como variáveis seriam usadas em um programa real?
# Problema 1 - Valor por hora
# Escreva um programa que retorna o valor hora de um funcionário com base no seu salário mensal e horas trabalhadas por mês.
'''
input salario_mensal
input horas_trabalhadas_por_mes
valor_hora = salario_mensal / salario_trabalhadas_por_mes
print valor_hora
'''
salario_mensal = input('Qual é o seu salário mensal? ')
horas_trabalhadas_por_mes = input('Quantas horas trabalha por mês? ')
valor_hora = int(salario_mensal) / int(horas_trabalhadas_por_mes)
print(valor_hora)