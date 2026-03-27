# Modifique o programa de contagem de cédulas para que ele trabalhe também com notas de R$ 100,00.

# Aqui eu solicito ao usuário o valor que ele deseja pagar.
valor_pagar = int(input("Digite o valor a ser pago: "))

# Aqui eu declaro as variáveis iniciais para a contagem.
cedulas = 0
atual = 100 # Começamos com a nota de 100 reais
faltando = valor_pagar

# Aqui eu inicio o loop principal para calcular a contagem de notas.
while True:
    # Aqui eu verifico se a nota atual cabe no valor que ainda falta pagar.
    if atual <= faltando:
        # Aqui eu subtraio o valor da nota do total que falta.
        faltando = faltando - atual
        # Aqui eu incremento a contagem de cédulas daquele valor.
        cedulas = cedulas + 1
    else:
        # Aqui eu verifico se houve alguma cédula entregue do valor atual.
        if cedulas > 0:
            # Aqui eu imprimo a quantidade de cédulas do valor atual.
            print(f"{cedulas} cédula(s) de R${atual}")
            
        # Aqui eu verifico se já pagamos o valor total.
        if faltando == 0:
            # Aqui eu interrompo o loop porque a conta fechou.
            break
            
        # Aqui eu uso a estrutura if/elif para trocar o valor da nota atual.
        if atual == 100:
            atual = 50
        elif atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
            
        # Aqui eu zero o contador de cédulas para o novo valor de atual.
        cedulas = 0
