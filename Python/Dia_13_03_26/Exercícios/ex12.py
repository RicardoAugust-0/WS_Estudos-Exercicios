# Modifique o programa anterior de forma a ler um número n. Imprima os n primeiros números primos.

# Aqui eu solicito ao usuário quantos números primos deseja imprimir.
qnt_primos = int(input("Digite a quantidade de números primos desejada: "))

# Aqui eu declaro o contador de primos encontrados e o número que será testado.
encontrados = 0
num_teste = 2

# Aqui eu inicio o loop principal que vai durar até acharmos todos os primos.
while encontrados < qnt_primos:
    # Se o número de teste atual for 2, já sabemos que é primo.
    if num_teste == 2:
        # Aqui eu imprimo o único número primo que é par.
        print(num_teste)
        # Aqui eu incremento o contador de primos encontrados.
        encontrados = encontrados + 1
    # Se o número for ímpar, ele tem chances de ser primo.
    elif num_teste % 2 != 0:
        # Aqui eu declaro o primeiro divisor ímpar que vou testar (3).
        e_primo = True
        divisor = 3
        # Aqui eu entro no loop que vai testar se o num_teste atual é divisível.
        while divisor < num_teste:
            # Caso o resto da divisão seja zero, o número não é primo.
            if num_teste % divisor == 0:
                e_primo = False
                break
            # Incrementamos a busca pelo próximo número ímpar.
            divisor = divisor + 2
            
        # Aqui eu vejo se o número de teste passou no teste de ser primo.
        if e_primo == True:
            # Aqui eu imprimo o número primo encontrado.
            print(num_teste)
            # Aqui eu incremento o contador total de primos encontrados.
            encontrados = encontrados + 1
            
    # Aqui eu incremento o número de teste para partirmos para o próximo teste.
    num_teste = num_teste + 1
