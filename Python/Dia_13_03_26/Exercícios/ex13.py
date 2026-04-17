# Escreva um programa que calcule a raiz quadrada de um número. Utilize o método de Newton para obter um resultado aproximado. Sendo n o número a obter a raiz quadrada, considere a base b=2. Calcule p usando a fórmula p=(b+(n/b))/2. Agora, calcule o quadrado de p. A cada passo, faça b=p e recalcular p usando a fórmula apresentada. Pare quando a diferença absoluta entre n e o quadrado de p for menor que 0,0001.

# Aqui eu solicito ao usuário o número que deseja calcular a raiz quadrada.
n = float(input("Digite um número para calcular a raiz quadrada: "))

# Aqui eu declaro o valor inicial da base (b = 2.0).
b = 2.0

# Aqui eu inicio o loop infinito que buscará a raiz aproximada.
while True:
    # Aqui eu aplico a fórmula de Newton para encontrar um p inicial.
    p = (b + (n / b)) / 2
    # Aqui eu calculo o quadrado do valor aproximado p.
    quadrado_p = p * p
    
    # Aqui eu calculo a diferença absoluta entre o número n e o quadrado de p.
    diferenca = n - quadrado_p
    # Se a diferença for negativa, transformamos em positiva (manual de abs).
    if diferenca < 0:
        diferenca = -diferenca
    
    # Aqui eu verifico se a diferença é menor que 0.0001 (nível de precisão).
    if diferenca < 0.0001:
        # Se for menor, atingimos o objetivo de precisão e paramos.
        break
        
    # Caso precise de mais iterações, trocamos o valor da base pelo p encontrado.
    b = p

# Aqui eu imprimo para o usuário o valor final da raiz aproximada.
print(f"A raiz quadrada aproximada de {n} é {p:.4f}")
