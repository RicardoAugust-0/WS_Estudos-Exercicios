# Será necessário escrever um programa o qual aprove o empréstimo bancário para a compra de uma casa. O programa deve perguntar o valor da casa a comprar, o salário do usuário e a quantidade de anos a pagar. O valor da prestação mensal não pode ser superior a 30% do salário. Necessário calcular o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.

valor_casa = int(input("\nQual será o valor do imóvel a ser financiado: "))
salario = int(input("Qual a sua renda bruta: "))

# Máximo de anos é 35 anos
prazo_pagamento = int(input("Em quantos anos será realizado o financiamento: "))

# Divide os anos em meses
prestacoes_mensais = prazo_pagamento * 12

# Calcula o valor de cada prestação com base na quantidade de meses e do imóvel
valor_prestacao = valor_casa / prestacoes_mensais

# O salário não pode ser comprometido mais do que 30%
renda = salario * 0.30

# Se as prestações ultrapassarem os 35 anos, não é possível financiar o imóvel
if prestacoes_mensais > 420:
    print("O prazo de quitação do imóvel não pode ultrapassar os 35 anos de financiamento.")
else:
    if valor_prestacao > renda:
        print("Não será possível a aprovação do emprestímo, sua renda teve comprometimento superior à um valor do que 30%.")
    else:
        print("O valor do empréstimo para o seu imóvel foi aprovado com sucesso.")

