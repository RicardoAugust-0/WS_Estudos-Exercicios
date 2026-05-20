i, num, fat = 0, 0, 0

print("Digite um valor de 1 a 9: ")
num = int(input())
fat = 1
for i in range(1, num + 1):
  fat *= i
print(f"O fatorial de {num} é {fat}")