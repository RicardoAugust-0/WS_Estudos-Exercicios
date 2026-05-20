base, altura = 0, 0
op = ""

while True:
  base = float(input("Digite a base: "))
  altura = float(input("Digite a altura: "))
  print(f"A área é: {base * altura}")
  print("Deseja repetir(s/n): ")
  op = input()
  if op == "n":
    break
