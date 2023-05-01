# leitura do vetor Q
Q = []
for i in range(20):
    while True:
        num = float(input("Digite um número positivo para a posição {}: ".format(i)))
        if num >= 0:
            break
        else:
            print("Número inválido, tente novamente.")
    Q.append(num)

# cálculo do maior e menor elemento e suas posições
maior = Q[0]
posicao_maior = 0
menor = Q[0]
posicao_menor = 0
for i in range(1, 20):
    if Q[i] > maior:
        maior = Q[i]
        posicao_maior = i
    if Q[i] < menor:
        menor = Q[i]
        posicao_menor = i

# impressão dos resultados
print("Maior elemento de Q: {:.2f} (posição {})".format(maior, posicao_maior))
print("Menor elemento de Q: {:.2f} (posição {})".format(menor, posicao_menor))
