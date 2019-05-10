# Lista

boletim_materia1=[]

# Entrada da disciplina juntamente com a sua média e faltas

for contador in range (0,1):
    notas1= [input("\nDigite a sua disciplina: "),
    int (input("\nDigite a sua média do primeiro semestre: ")),
    int (input("\nDigite a sua média do segundo semestre: ")),
    int (input("\nDigite o seu total de faltas: "))]

boletim_materia1.append(notas1)
if (notas1[1] + notas1[2]) /2 >=6 and notas1[3] <=20:
    print("Aprovado")

elif (notas1[1] + notas1[2]) /2 <4 or notas1[3] >20:
    print("Reprovado")

else:
    print("Exame")

#########################################################################################

# Lista

boletim_materia2=[]

# Entrada da disciplina juntamente com a sua média e faltas

for contador in range (0,1):
    notas2= [input("\nDigite a sua disciplina: "),
    int (input("\nDigite a sua média do primeiro semestre: ")),
    int (input("\nDigite a sua média do segundo semestre: ")),
    int (input("\nDigite o seu total de faltas: "))]

boletim_materia2.append(notas2)
if (notas2[1] + notas2[2]) /2 >=6 and notas2[3] <=20:
    print("Aprovado")

elif (notas2[1] + notas2[2]) /2 <4 or notas2[3] >20:
    print("Reprovado")

else:
    print("Exame")

#########################################################################################

# Lista

boletim_materia3=[]

# Entrada da disciplina juntamente com a sua média e faltas

for contador in range (0,1):
    notas3= [input("\nDigite a sua disciplina: "),
    int (input("\nDigite a sua média do primeiro semestre: ")),
    int (input("\nDigite a sua média do segundo semestre: ")),
    int (input("\nDigite o seu total de faltas: "))]

boletim_materia3.append(notas3)
if (notas3[1] + notas3[2]) /2 >=6 and notas3[3] <=20:
    print("Aprovado")

elif (notas3[1] + notas3[2]) /2 <4 or notas3[3] >20:
    print("Reprovado")

else:
    print("Exame")



