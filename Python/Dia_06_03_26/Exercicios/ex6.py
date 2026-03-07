''' Escreva um programa que leia dois números do usuário e pergunte qual é a operação que o mesmo deseja realizar. É necessário calcular soma, subtração, multiplicação e divisão.'''


print("\n --- Digite 1 para Somar os 2 números. --- \n --- Digite 2 para Subtrair o primeiro número pelo segundo. --- \n --- Digite 3 para Multiplicar o primeiro número pelo segundo. --- \n --- Digite 4 para Dividir o primeiro número pelo segundo. --- \n")

categoria = int(input("Selecione a operação digitando de 1 a 4: "))

if categoria == 1:
    numero1 = int(input("Digite o primeiro número da sua soma: "))
    numero2 = int(input("Digite o segundo número da sua soma: "))
    resultado = numero1 + numero2
    print(f"O resultado da sua soma é de: {resultado}.\n")
elif categoria == 2:
    numero1 = int(input("Digite o primeiro número da sua subtração: "))
    numero2 = int(input("Digite o segundo número da sua subtração: "))
    resultado = numero1 - numero2
    print(f"O resultado da sua subtração é de: {resultado}.\n")
elif categoria == 3:
    numero1 = int(input("Digite o primeiro número da sua multiplicação: "))
    numero2 = int(input("Digite o segundo número da sua multiplicação: "))
    resultado = numero1 * numero2
    print(f"O resultado da sua multiplicação é de: {resultado}.\n")
elif categoria == 4:
    numero1 = float(input("Digite o primeiro número da sua divisão: "))
    numero2 = float(input("Digite o segundo número da sua divisão: "))
    resultado = numero1 / numero2
    print(f"O resultado da sua divisão é de: {resultado:.2f}.\n")
else:
    print("Número ou caractere não está incluso nas categorias. Aperte ENTER para finalizar...")
