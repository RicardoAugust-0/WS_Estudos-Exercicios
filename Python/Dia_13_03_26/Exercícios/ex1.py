# Programa que escreve uma contagem regressiva do lançamento de um foguete. O programa irá imprimir 10, 9, ..., 1, 0 e Fogo! na tela.
import time


contador = 10

while contador >= 0:
    print(contador)
    contador = contador - 1
    time.sleep(1)
print("Fogo!")