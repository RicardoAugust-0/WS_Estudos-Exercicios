# Programa que lê 3 números e descreve o maior número e o menor número para o usuário.

numero1 = int(input("Adicione o primeiro número: "))
numero2 = int(input("Adicione o segundo número: "))
numero3 = int(input("Adicione o terceiro número: "))

if (numero1 > numero2):
  if (numero2 < numero3):
    print(f"O maior número é: {numero1} e o menor número é: {numero2}")
elif (numero2 > numero1):
  if (numero1 < numero3):
    print(f"O maior número é: {numero2} e o menor número é: {numero1}")
elif (numero3 > numero1):
  if (numero1 < numero2):
    print(f"O maior número é: {numero3} e o menor número é: {numero1}")
elif (numero1 > numero3):
  if (numero3 < numero2):
    print(f"O maior número é: {numero1} e o menor número é: {numero3}")
elif (numero2 > numero3):
  if (numero3 < numero1):
    print(f"O maior número é: {numero2} e o menor número é: {numero3}")
elif (numero3 > numero2):
  if (numero2 < numero1):
    print(f"O maior número é: {numero3} e o menor número é: {numero2}")
else:
  print("Os números são iguais.")