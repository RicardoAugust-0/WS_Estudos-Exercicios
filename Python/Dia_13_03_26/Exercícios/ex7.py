# Escreva um programa para controlar uma pequena máquina registradora. Você deve solicitar ao usuário que digite o código do produto e a quantidade comprada. Use a tabela de códigos para obter o preço de cada produto. Seu programa deve exibir o total de compras depois que o usuário digitar 0. Qualquer outro código deve gerar a mensagem de erro “Código inválido”.

# Aqui eu declaro a variável que vai armazenar o valor total da compra.
total = 0.0

# Aqui eu imprimo uma mensagem de boas-vindas para o usuário.
print("Bem-vindo à Máquina Registradora!")
print("Digite o código do produto (1 a 5) ou 0 para encerrar.")

# Aqui eu inicio um loop infinito que só será interrompido quando o código for 0.
while True:
    # Aqui eu solicito ao usuário que digite o código do produto.
    codigo = int(input("Digite o código do produto: "))
    
    # Aqui eu verifico se o usuário deseja encerrar o programa digitando 0.
    if codigo == 0:
        # Aqui eu uso o comando break para sair do loop.
        break
    
    # Aqui eu declaro a variável preco e verifico qual produto corresponde ao código digitado.
    preco = 0
    if codigo == 1:
        preco = 0.50
    elif codigo == 2:
        preco = 1.00
    elif codigo == 3:
        preco = 4.00
    elif codigo == 4:
        preco = 7.00
    elif codigo == 5:
        preco = 8.00
    
    # Aqui eu verifico se o código do produto é válido (se o preço foi atribuído).
    if preco > 0:
        # Aqui eu solicito a quantidade comprada do produto válido.
        quantidade = int(input("Digite a quantidade comprada: "))
        # Aqui eu somo o valor do item ao total da compra.
        total = total + (preco * quantidade)
    else:
        # Aqui eu informo ao usuário que o código digitado não consta na tabela.
        print("Código inválido!")

# Aqui eu imprimo o valor total da compra formatado com duas casas decimais.
print(f"\nO total da compra foi de R$ {total:.2f}")
