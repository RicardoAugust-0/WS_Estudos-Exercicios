# Escreva um programa que pergunte o valor inicial de uma dívida e o juro mensal. Pergunte também o valor mensal que será pago. Imprima o número de meses para que a dívida seja paga, o total pago e o total de juros pagos.

print("Bem-vindo ao simulador de dívida!")

divida = float(input("Digite o valor inicial da dívida: "))
taxa_juros = float(input("Digite a taxa de juros mensal (em %): "))
pagamento_mensal = float(input("Digite o valor mensal que será pago: "))

# Verificação se a dívida pode ser paga
if (divida * taxa_juros / 100) >= pagamento_mensal:
    print("\nErro: O pagamento mensal é insuficiente para cobrir os juros. A dívida nunca será paga!")
else:
    saldo = divida
    total_pago = 0
    total_juros = 0
    meses = 0

    while saldo > 0:
        juros_mes = saldo * (taxa_juros / 100)
        total_juros += juros_mes
        saldo += juros_mes
        
        if saldo > pagamento_mensal:
            saldo -= pagamento_mensal
            total_pago += pagamento_mensal
        else:
            # Último pagamento
            total_pago += saldo
            saldo = 0
            
        meses += 1

    print(f"\n--- Resultado da Simulação ---")
    print(f"Total de meses para pagar: {meses}")
    print(f"Total pago: R$ {total_pago:.2f}")
    print(f"Total de juros pagos: R$ {total_juros:.2f}")
