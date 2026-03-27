# Escreva um programa que leia um número e verifique se é ou não um número primo. Para fazer essa verificação, calcule o resto da divisão do número por 2 e depois por todos os números impares até o número lido. Se o resto de uma dessas divisões for igual a zero, o número não é primo. Observe que 0 e 1 não são primos e que 2 é o único número primo que é par.

# Aqui eu solicito ao usuário que digite um número inteiro para teste.
numero = int(input("Digite um número inteiro: "))

# Aqui eu verifico as condições iniciais: se o número é menor que 2.
if numero < 2:
    # Números menores que 2 não são considerados primos.
    print(f"{numero} não é primo.")
# Aqui eu verifico se o número é exatamente 2.
elif numero == 2:
    # 2 é o único número primo que é par.
    print("2 é primo.")
# Aqui eu verifico se o número é par e maior que 2.
elif numero % 2 == 0:
    # Casos como 4, 6, 8, etc., que nunca são primos.
    print(f"{numero} não é primo (é par e não é 2).")
# Aqui eu entro no caso de o número ser ímpar e maior que 2.
else:
    # Aqui eu declaro a variável e_primo para monitorar se achamos divisores.
    e_primo = True
    # Aqui eu declaro o primeiro divisor ímpar que vou testar (3).
    divisor = 3
    
    # Aqui eu entro no loop que vai testar todos os números ímpares até o número digitado.
    while divisor < numero:
        # Aqui eu vejo se o resto da divisão do número pelo divisor atual é zero.
        if numero % divisor == 0:
            # Caso o resto seja zero, o número é divisível por outros e não é primo.
            e_primo = False
            # Aqui eu interrompo o loop porque já sabemos que não é primo.
            break
        # Aqui eu incremento o divisor de dois em dois para manter-se ímpar.
        divisor = divisor + 2
    
    # Aqui eu verifico o resultado final guardado na variável e_primo.
    if e_primo == True:
        # Aqui eu informo ao usuário que o número é primo.
        print(f"{numero} é primo.")
    else:
        # Aqui eu informo ao usuário que o número não é primo.
        print(f"{numero} não é primo.")
