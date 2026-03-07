# Escreva um programa para calcular o preço a pagar pelo fornecimento de energia elétrica. Será necessária a quantidade de kWh consumido e o tipo de instalação: R para residências, I para industrias e C para comércios. Calcule o preço a pagar de acordo com a table a seguir

quantidade_kWh = float(input("\nQual a quantidade de kWh consumida: "))

tipo_instalacao = str(input("Qual o tipo de instalação \n\n --- R para residências --- \n --- I para industrias --- \n --- C para comércios --- \n"))

if tipo_instalacao == "r":
    if quantidade_kWh <= 500:
        preco = 0.40
        quantidade_kWh = quantidade_kWh * preco
        print(f"O preço necessário a se pagar é de: R${quantidade_kWh:.2f} reais")

    elif quantidade_kWh > 500:
        preco = 0.65
        quantidade_kWh = quantidade_kWh * preco
        print(f"O preço necessário a se pagar é de: R${quantidade_kWh:.2f} reais")

elif tipo_instalacao == "i":
    if quantidade_kWh <= 1000:
        preco = 0.55
        quantidade_kWh = quantidade_kWh * preco
        print(f"O preço necessário a se pagar é de: R${quantidade_kWh:.2f} reais")

    elif quantidade_kWh > 1000:
        preco = 0.60
        quantidade_kWh = quantidade_kWh * preco
        print(f"O preço necessário a se pagar é de: R${quantidade_kWh:.2f} reais")

elif tipo_instalacao == "c":
    if quantidade_kWh <= 5000:
        preco = 0.55
        quantidade_kWh = quantidade_kWh * preco
        print(f"O preço necessário a se pagar é de: R${quantidade_kWh:.2f} reais")

    elif quantidade_kWh > 5000:
        preco = 0.60
        quantidade_kWh = quantidade_kWh * preco
        print(f"O preço necessário a se pagar é de: R${quantidade_kWh:.2f} reais")
else:
    print("O carácter digitado é inválido. Estamos encerrando...")