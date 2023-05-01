
clubes = []
for i in range(10):
    clube = input("Digite o nome do clube: ")
    clubes.append(clube)

# leitura do nome do clube a ser pesquisado
nome_clube = input("Digite o nome do clube a ser pesquisado: ")

# verificação se o nome do clube está no vetor
if nome_clube in clubes:
    print("ACHEI")
else:
    print("NÃO ACHEI")
