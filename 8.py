vetor = []
for i in range(30):
    num = int(input(f"Digite o {i+1}º número do vetor: "))
    vetor.append(num)

num_procurado = int(input("Digite o número que deseja procurar no vetor: "))
count = 0
for i in vetor:
    if i == num_procurado:
        count += 1

print(f"O número {num_procurado} aparece {count} vezes no vetor.")
