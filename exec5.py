preco = int(input("Insira o preço de alguma mercadoria: "))
desconto = int(input("Insira um percentual de desconto: "))

valor_desconto = preco - (preco * desconto / 100)

print(f"O valor a se pagar é de: R${valor_desconto} reais")
print(f"O valor do desconto é de: R${preco - valor_desconto} reais")