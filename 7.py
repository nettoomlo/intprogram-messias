v1 = []
v2 = []

for i in range(10):
    num1 = int(input(f"Digite o {i+1}º número do vetor V1: "))
    num2 = int(input(f"Digite o {i+1}º número do vetor V2: "))
    v1.append(num1)
    v2.append(num2)

count = 0
for i in range(10):
    if v1[i] == v2[i]:
        count += 1

print(f"V1 e V2 possuem {count} números iguais na mesma posição.")
