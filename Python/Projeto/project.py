# Projeto 1B — Sistema de Controle de Estoque de uma Pequena Loja
# Versão simplificada para um estudante iniciante.

# Conteúdos de Python envolvidos:
# • if e else, while, listas, dicionários, funções, menu com opções numéricas.

# A lista `estoque` vai guardar todos os produtos.
# Cada produto na lista é um dicionário.
estoque = []

# Módulo 1 — Cadastro
def cadastrar_produto():
    """Cadastra um novo produto no estoque."""
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: R$ "))
    quantidade = int(input("Digite a quantidade inicial: "))

    novo_produto = {"nome": nome, "preco": preco, "quantidade": quantidade}
    estoque.append(novo_produto)
    
    print(f"Produto '{nome}' cadastrado com sucesso!")

# Módulo 3 — Relatório (Parte 1)
def listar_produtos():
    """Lista todos os produtos cadastrados."""
    if not estoque:
        print("Nenhum produto cadastrado.")
        return

    print("\n--- Lista de Produtos em Estoque ---")
    for produto in estoque:
        # Informa se um produto está com estoque baixo
        if produto['quantidade'] <= 10:
            print(f"Produto: {produto['nome']}, Preço: R${produto['preco']:.2f}, Quantidade: {produto['quantidade']} (ESTOQUE BAIXO!)")
        else:
            print(f"Produto: {produto['nome']}, Preço: R${produto['preco']:.2f}, Quantidade: {produto['quantidade']}")
    print("------------------------------------")

# Módulo 2 — Movimentação
def registrar_entrada():
    """Registra a entrada de mercadorias no estoque."""
    nome = input("Digite o nome do produto para dar entrada: ")
    
    produto_encontrado = None
    for produto in estoque:
        if produto['nome'] == nome:
            produto_encontrado = produto
            break
            
    if produto_encontrado:
        quantidade = int(input("Digite a quantidade de entrada: "))
        produto_encontrado['quantidade'] = produto_encontrado['quantidade'] + quantidade
        print("Entrada registrada com sucesso!")
    else:
        print(f"Produto '{nome}' não encontrado.")

def registrar_saida():
    """Registra a saída de mercadorias do estoque."""
    nome = input("Digite o nome do produto para dar saída: ")

    produto_encontrado = None
    for produto in estoque:
        if produto['nome'] == nome:
            produto_encontrado = produto
            break

    if produto_encontrado:
        quantidade = int(input("Digite a quantidade de saída: "))
        if quantidade <= produto_encontrado['quantidade']:
            produto_encontrado['quantidade'] = produto_encontrado['quantidade'] - quantidade
            print("Saída registrada com sucesso!")
        else:
            print("Não há estoque suficiente para esta saída.")
    else:
        print(f"Produto '{nome}' não encontrado.")

# Módulo 3 — Relatório (Parte 2)
def mostrar_valor_total():
    """Calcula e exibe o valor total de todos os itens em estoque."""
    valor_total = 0.0
    for produto in estoque:
        valor_total = valor_total + (produto['preco'] * produto['quantidade'])
    
    print(f"\nValor total do estoque: R$ {valor_total:.2f}")

# --- Menu Principal ---
def menu():
    """Exibe o menu principal e gerencia as escolhas do usuário."""
    while True:
        print("\n--- Sistema de Controle de Estoque ---")
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Registrar entrada no estoque")
        print("4 - Registrar saída do estoque")
        print("5 - Mostrar valor total do estoque")
        print("6 - Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            cadastrar_produto()
        elif escolha == '2':
            listar_produtos()
        elif escolha == '3':
            registrar_entrada()
        elif escolha == '4':
            registrar_saida()
        elif escolha == '5':
            mostrar_valor_total()
        elif escolha == '6':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executando o programa
menu()