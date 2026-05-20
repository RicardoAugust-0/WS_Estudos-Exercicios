
numero, fatorial = 1, 1

numero = int(input("Digite um número para calcular o fatorial: "))

for i in range(1, numero + 1):  
    fatorial *= i

print(f"O fatorial de {numero} é {fatorial}")