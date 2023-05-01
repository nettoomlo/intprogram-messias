A = []
M = []

for i in range(10):
    num = int(input("Digite um número para a posição %d do vetor A: " % (i+1)))
    A.append(num)

x = int(input("Digite um número para multiplicar o vetor A: "))

for i in range(10):
    M.append(A[i]*x)

print("Vetor A:", A)
print("Valor de X:", x)
print("Vetor M:", M)
