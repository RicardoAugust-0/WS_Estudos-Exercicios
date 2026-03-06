# Programa que converta temperatura digitada em Celsius para Fahrenheit

# Solicita ao usuário a temperatura em Celsius.
celsius = float(input("Digite a temperatura em graus Celsius: "))

fahrenheit = celsius * 9 / 5 + 32

# Exibe o resultado.
print(f"{celsius} graus Celsius equivale a {fahrenheit} graus Fahrenheit.")