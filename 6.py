# leitura do vetor de 20 números
vetor = []
for i in range(20):
    numero = int(input(f"Digite o {i+1}º número: "))
    vetor.append(numero)

# leitura do número a ser removido
numero_remover = int(input("Digite um número para remover: "))

# verificação se o número existe no vetor
if numero_remover in vetor:
    # criação do novo vetor sem o número informado
    novo_vetor = []
    for i in range(20):
        if vetor[i] != numero_remover:
            novo_vetor.append(vetor[i])
    print(f"O número {numero_remover} foi removido do vetor.")
    print("Novo vetor:", novo_vetor)
else:
    print(f"O número {numero_remover} não existe no vetor.")
