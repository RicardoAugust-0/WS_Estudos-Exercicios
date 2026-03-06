# Programa que calcula o preço a se pagar pela quantidade de Km percorridos e a quantidade de dias pelos quais o carro foi alugado (o carro custa R$60,00 por dia e R$0,15 centavos por Km rodado).

dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos Km foram rodados? '))

total = (dias * 60) + (km * 0.15)

print(f'O total a pagar é de R${total} reais.')