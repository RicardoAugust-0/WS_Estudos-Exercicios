# Programa que pergunta a distância que o usuário deseja percorrer em km. Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200 km e R$0,45 para viagens mais longas.

distancia = float(input("Digite a distância que deseja percorrer em km: "))

if distancia <= 200:
    km = 0.50
    valor_total = distancia * km
    print(f"O valor total da corrida ficou em torno de R${valor_total:.2f} reais.")
else:
    km = 0.45
    valor_total = distancia * km
    print(f"O valor total da corrida ficou em torno de R${valor_total:.2f} reais.")
