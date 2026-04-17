# Modifique novamente o programa para aceitar valores decimais, ou seja, contar moedas de 0,01; 0,02; 0,05; 0,10 e 0,50.

# Aqui eu solicito ao usuário o valor que ele deseja pagar (aceita decimais).
valor_pagar = float(input("Digite o valor a ser pago: "))

# Aqui eu declaro as variáveis iniciais e converto para centavos (números inteiros).
# Fazemos isso multiplicando por 100 para evitar erros do Python com pontos flutuantes.
centavos_pagar = int(valor_pagar * 100 + 0.5)

# Aqui eu declaro as variáveis para a contagem.
cedulas_moedas = 0
atual = 10000 # R$ 100,00 em centavos

# Aqui eu inicio o loop principal para calcular a contagem.
while True:
    # Aqui eu verifico se o valor atual da moeda/cédula cabe no total que falta.
    if atual <= centavos_pagar:
        # Aqui eu subtraio o valor atual do total que falta.
        centavos_pagar = centavos_pagar - atual
        # Aqui eu incremento a contagem de moedas/cédulas entregues.
        cedulas_moedas = cedulas_moedas + 1
    else:
        # Aqui eu verifico se houve alguma unidade do valor atual entregue.
        if cedulas_moedas > 0:
            # Aqui eu imprimo o resultado formatado de volta para Reais.
            if atual >= 100:
                print(f"{cedulas_moedas} cédula(s) de R${atual / 100:.2f}")
            else:
                print(f"{cedulas_moedas} moeda(s) de R${atual / 100:.2f}")

        # Aqui eu verifico se já pagamos tudo.
        if centavos_pagar == 0:
            # Aqui eu encerro o loop.
            break
            
        # Aqui eu troco o valor atual da cédula/moeda usando a estrutura if/elif.
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
        
        # Aqui eu zero o contador para o novo valor selecionado.
        cedulas_moedas = 0
