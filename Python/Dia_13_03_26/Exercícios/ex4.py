# Escreva um programa que leia dois números. Imprima a divisão inteira do primeiro pelo segundo, assim como o resto da divisão. Utilize apenas os operadores de soma e subtração para calcular o resultado. Lembre-se de que podemos entender a quociente da divisão de dois números como a quantidade de vezes que podemos retirar o divisor do dividendo.

n1 = int(input("Insira o primeiro número: "))
n2 = int(input("Insira o segundo número: "))

quociente = 0

while n1 >= n2:
  n1 -= n2
  quociente += 1
print(f"Quociente: {quociente}")
print(f"Resto: {n1}")
