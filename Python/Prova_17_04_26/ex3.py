# Pesquisa de satisfalçao da turma. Elabore um programa em Python para registrar as respostas de uma pesquisa de satisfação de uma turma. cada aluno deverá informar uma nota de 1 a 5, sendo 1 = pessímo; 2 = ruim; 3 = regular; 4 = bom; 5 = excelente. A entrada de dados termina quando o usuário digitar 0. Ao final, o programa deverá informar: a) quantos alunos responderam a pesquisa; b) quantos deram nota 5; c) quantos deram nota 1; d) a média das notas informadas. Requisitos: não considerar o 0 nos cálculos.

# Variáveis para contagem
total_alunos = 0
notas_pessimo = 0
notas_excelente = 0
soma_notas = 0

mensagem = (
  "Digite uma nota de 1 a 5 sendo elas:\n\n"
  " 1 = pessímo;\n"
  " 2 = ruim;\n"
  " 3 = regular;\n"
  " 4 = bom;\n"
  " 5 = excelente\n\n"
  "Digite 0 para finalizar: "
)

# Estrutura em loop
while True:
  nota_aluno = int(input(mensagem))

  if nota_aluno == 0:
    break

  if nota_aluno < 1 or nota_aluno > 5:
    print("Nota inválida, tente novamente!")
    continue

  total_alunos += 1
  soma_notas += nota_aluno

  if nota_aluno == 1:
    notas_pessimo += 1
  if nota_aluno == 5:
    notas_excelente += 1

if total_alunos > 0:
  media_alunos = soma_notas / total_alunos
  print(
    f"A quantidade de alunos que respondeu a pesquisa foi de: {total_alunos}, "
    f"a quantidade de notas 5 foi de: {notas_excelente}, "
    f"a quantidade de notas 1 foi de: {notas_pessimo} "
    f"e a média foi de: {media_alunos:.2f}"
  )
else:
  print("Nenhum aluno respondeu a pesquisa.")