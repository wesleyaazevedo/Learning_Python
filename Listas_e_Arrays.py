nome=[]
salario=[]
x=int(input("Quantos nomes irá digitar? "))

for x in range(x):
    rcbNome = str(input("Digite o Nome: "))
    rcbSalario= str(input("Digite o Salario: "))
    nome.append(rcbNome)
    salario.append(rcbSalario)
    

#Metodo/Função que imprime conteudo da lista ATÉ o valor i informado.
def listas (i):
	global nome,salario
	tnome,tsalario=len(nome),len(salario)
	if i<=tnome and i<=tsalario:
		for i in range(i):
			print('Nome: %s | Salario: %s' %(nome[i],salario[i]))
	else: #tenta tratar os erros quando valores estão inconsistentes.
		if i != tnome and i != tsalario:
			print("Valor informado diferente de total de itens cadastrados")
		if tnome != tsalario:
			print("Dados inconsistentes")
			print("Quantidades de registros em Nome: %d <> Salarios: %d" %(tnome,tsalario))

#Metodo/Função que imprime conteudo da lista APENAS o valor i informado.
def individual (i):
	global nome,salario
	tnome,tsalario=len(nome),len(salario)
	
	if i<=tnome and i<=tsalario:
		print('Nome: %s | Salario: %s' %(nome[i-1],salario[i-1]))
	else:
		if i != tnome and i != tsalario:
			print("Valor informado diferente de total de itens cadastrados")
		if tnome != tsalario:
			print("Dados inconsistentes")
			print("Quantidades de registros em Nome: %d <> Salarios: %d" %(tnome,tsalario))

#Retirado do curso Python para Zumbis
