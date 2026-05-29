# Exercício. Ordenação de preços em ordem decrescente

# precos = [25.90, 10.50, 99.90, 45.00, 12.75]
# fim = len(precos)

# while fim > 1:
#     trocou = False
#     x = 0

#     while x < (fim - 1):
#         if precos[x] < precos[x + 1]:
#             trocou = True
#             temp = precos[x]
#             precos[x] = precos[x + 1]
#             precos[x + 1] = temp

#         x += 1
#     if not trocou:
#         break
#     fim -= 1

# print("Preços ordenados em ordem decrescente:")

# for preco in precos:
#     print(f"R$ {preco:.2f}")


# Exercicio. O que acontece quando a lista já esta ordenada? (Rastreie o programa 4, mas com a lista L = [1,2,3,4,5]).

# precos = [1, 2, 3, 4, 5]
# fim = len(precos)

# while fim > 1:
#     trocou = False
#     x = 0

#     while x < (fim - 1):
#         if precos[x] > precos[x + 1]:
#             trocou = True
#             temp = precos[x]
#             precos[x] = precos[x + 1]
#             precos[x + 1] = temp

#         x += 1
#     if not trocou:
#         break
#     fim -= 1

# print("Preços ordenados em ordem crescente:")

# for preco in precos:
#     print(f"R$ {preco:.2f}")

# Exercicio. O que acontece quando os dois valores são iguais? (Rastreie o programa 4, mas com a lista L = [3,3,1,5,4]).

# precos = [3, 3, 1, 5, 4]
# fim = len(precos)

# while fim > 1:
#     trocou = False
#     x = 0

#     while x < (fim - 1):
#         if precos[x] > precos[x + 1]:
#             trocou = True
#             temp = precos[x]
#             precos[x] = precos[x + 1]
#             precos[x + 1] = temp

#         x += 1
#     if not trocou:
#         break
#     fim -= 1

# print("Preços ordenados em ordem crescente:")

# for preco in precos:
#     print(f"R$ {preco:.2f}")

"""Exercício 5. Uma escola possui uma lista com os nomes de alunos:
alunos = ["Carlos", "Ana", "Bruno", "Daniela", "Eduardo"]
Elabore um programa em Python que ordene esses nomes em ordem
alfabética, utilizando o método de bolhas.
Ao final, o programa deve imprimir os nomes ordenados.
"""

alunos = ["Carlos", "Ana", "Bruno", "Daniela", "Eduardo"]

fim = len(alunos)

while fim > 1:
    trocou = False
    x = 0

    while x < (fim - 1):
        if alunos[x] > alunos[x + 1]:
            trocou = True
            temp = alunos[x]
            alunos[x] = alunos[x + 1]
            alunos[x + 1] = temp

        x += 1
    if not trocou:
        break
    fim -= 1
print("Nomes ordenados em ordem alfabética:")
for aluno in alunos:
    print(aluno)
