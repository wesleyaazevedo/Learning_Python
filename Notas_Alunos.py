#-*-coding: utf-8 -*-

#Código escrito por Wesley Azevedo, durante perido de aprendizado de Python.
#Entendendo comandos iniciais: print, if, else.

nome = input("Nome do Aluno: ")
nota1 = float(input("Nota da 1ª avaliação: "))
nota2 = float(input("Nota da 2ª avaliação: "))
media = (nota1*4+nota2*6)/10
aluno = dict(nome=nome,nota1=nota1,nota2=nota2,media=media)

print('-'*40) #Insere linhas acima da exibição do nome do aluno

print("Aluno: {nome}".format(nome=aluno['nome']))

print('-'*40) #Insere linhas acima da exibição do nome do aluno

print("Nota da 1ª avaliação:{nota1}".format(nota1=aluno['nota1']))

print("Nota da 2ª avaliação:{nota2}".format(nota2=aluno['nota2']))

print("Média:{media}".format(media=aluno['media']))
print("\n")

print('-'*40) #Insere linhas acima da exibição da situação do aluno (reprovado ou aprovado)

if media>=6:
	print("Voçê está aprovado.")

else:
	print("Você está reprovado")
	

#Programa desenvolvido por Wesley Azevedo durante o aprendizado de Python	
