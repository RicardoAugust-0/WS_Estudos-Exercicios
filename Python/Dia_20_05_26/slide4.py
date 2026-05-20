media, soma, nota = 0, 0, 0
cont = 0

while cont < 5:
  print("Informe a nota do aluno: ")
  nota = float(input())
  soma = soma + nota
  cont = cont + 1
media = soma / 5
print(f"Media da turma = {media}")
  