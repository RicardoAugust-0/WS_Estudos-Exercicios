# Crescimento populacional. Elabore um programa que calcule em quantos anos a população de uma cidade A ultrapassará ou igualará a população de uma cidade B. Considere que: a cidade A começa com 80.000 habitantes e cresce 4% ao ano; a cidade B começa com 200.000 habitantes e cresce 1,5% ao ano. O programa deve mostrar: a) quantos anos serão necessário; b) a população aproximada de cada cidade no momento em que A alcançar ou ultrapassar B.

# Variáveis para contagem
populacao_a = 80000
populacao_b = 200000
anos = 0

# Estrutura em loop
while populacao_a < populacao_b:
  populacao_a += populacao_a * 0.04
  populacao_b += populacao_b * 0.015
  anos += 1

# Resultado
print(f"A cidade A ultrapassará ou igualará a cidade B em {anos} anos.\n A população aproximada da cidade A será de {int(populacao_a)} habitantes e da cidade B será de {int(populacao_b)} habitantes.")