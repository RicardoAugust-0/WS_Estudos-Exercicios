# Validação de senha com número limitado de tentativas. Elabore um programa em python que peça ao usuário para digitar uma senha. Considere que a senha correta é 1234. O programa deve permitir no máximo 3 tentativas. Regras: se o usuário acertar a senha, o programa deve exibir: Acesso permitido; se errar, deve exibir: Senha incorreta; após 3 tentativas erradas, o programa deve exibir: Acesso bloqueado. Requisitos: utilizar contador e estrutura condicional if e else.

# Senha correta
senha_correta = 1234

# Digitar uma senha
senha = int(input("Digite uma senha númerica de até 4 dígitos: "))

# Loop contador
contador = 1
while contador < 3:
  if senha == senha_correta:
    print("Acesso Permitido!")
    break
  elif senha != senha_correta:
    print("Senha incorreta!")
    senha = int(input("Tente novamente: "))
    if contador == 2:
      print("Acesso Bloqueado!")
  contador = contador + 1