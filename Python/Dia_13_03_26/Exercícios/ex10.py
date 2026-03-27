# O que acontece se digitarmos 0,001 no programa anterior? Caso ele não funcione, altere-o de forma a corrigir o problema.

# Ao digitarmos 0.001 em um programa de contagem que usa floats, o programa pode falhar nos cálculos.
# Isso ocorre devido à imprecisão do ponto flutuante em sistemas de computador. 
# A solução ideal é converter o valor para centavos usando inteiros (int) para garantir exatidão absoluta.

# Aqui eu solicito ao usuário o valor a pagar (incluindo centavos).
valor_pagar = float(input("Digite o valor a ser pago: "))

# Aqui eu converto para centavos como um número inteiro para corrigir as imprecisões de 0.001 e similares.
# Fazemos a multiplicação por 100 e convertemos para inteiro, ignorando frações irrelevantes de centavo.
centavos_pagar = int(valor_pagar * 100)

# Agora eu declaro as variáveis que vou usar para monitorar a contagem.
cedulas_moedas = 0
atual = 10000 # Começamos pela maior nota de cem reais

# Aqui eu verifico se o valor informado foi menor do que 1 centavo (0.01).
if centavos_pagar == 0:
    print("O valor é insuficiente para ser contado ou menor que um centavo.")

# Aqui eu entro no loop que vai percorrer os valores das moedas e notas.
while centavos_pagar > 0:
    # Aqui eu vejo se o valor da moeda cabe no total que falta.
    if atual <= centavos_pagar:
        centavos_pagar = centavos_pagar - atual
        cedulas_moedas = cedulas_moedas + 1
    else:
        # Aqui eu imprimo se eu já entreguei alguma nota/moeda deste valor atual.
        if cedulas_moedas > 0:
            if atual >= 100:
                print(f"{cedulas_moedas} cédula(s) de R${atual / 100:.2f}")
            else:
                print(f"{cedulas_moedas} moeda(s) de R${atual / 100:.2f}")

        # Se não houver mais total a pagar, interrompemos o loop.
        if centavos_pagar == 0:
            break
            
        # Aqui eu uso a estrutura elif para mudar o valor atual para a próxima moeda/nota.
        if atual == 10000: atual = 5000
        elif atual == 5000: atual = 2000
        elif atual == 2000: atual = 1000
        elif atual == 1000: atual = 500
        elif atual == 500: atual = 200
        elif atual == 200: atual = 100
        elif atual == 100: atual = 50
        elif atual == 50: atual = 20
        elif atual == 20: atual = 10
        elif atual == 10: atual = 5
        elif atual == 5: atual = 2
        elif atual == 2: atual = 1
        
        # Aqui eu zero a contagem para iniciarmos com o novo valor de atual.
        cedulas_moedas = 0
