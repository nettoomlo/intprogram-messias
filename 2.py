
notas = []
for i in range(20):
    nota = float(input("Digite a nota do aluno {}: ".format(i+1)))
    notas.append(nota)

# cálculo da média da turma
media = sum(notas) / len(notas)

# contagem de alunos com nota acima da média
acima_media = 0
for nota in notas:
    if nota > media:
        acima_media += 1

# impressão dos resultados
print("Média da turma: {:.2f}".format(media))
print("Alunos com nota acima da média: {}".format(acima_media))
