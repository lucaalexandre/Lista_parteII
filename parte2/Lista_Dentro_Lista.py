nomes = []


for contador in range (0,3):
    nome =[input("\n Escreva um produto: "), int(input("\n Digite o valor de cada produto: "))]
    nomes.append(nome)
total_produtos =0
for nome in nomes:
    print(nome[0].upper())
    total_produtos+=nome[1]
print("O total de produtos é " + str(total_produtos))
print("O valor total dos pro " + str(total_produtos/len(nomes)))