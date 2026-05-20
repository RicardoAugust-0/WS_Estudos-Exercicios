qtd, cont = 0, 0

print("Quantidade: ")
qtd = int(input())
print("")
print("Para = ")
for cont in range(qtd):
  print("*")
cont = 0
print("")
print("Enquanto = ")
while cont < qtd:
  print("*")
  cont += 1
cont = 0
print("")
print("Enquanto = ")
while True:
  print("*")
  cont += 1
  if cont >= qtd:
    print("")
    break