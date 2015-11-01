#Tentei criar um algoritmo de Chave Simétrica ou Chave Única

import random, math

#Vetor com o alfabeto/dicionário, utilizo indice de cada letra para realizar a pesquisa
alfa=[' ','a', 'b', 'c', 'd', 'e', 'f', 'g' ,'h' ,'i' ,'j' ,'l' ,'m' ,'n' ,'o' ,'p' ,'q', 'r', 's', 't', 'u', 'v', 'x', 'z',
      'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Z', '!','?', '.','#','@']

#indice=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]

#Variáveis

mtexto=[];msg=[];mchave=[];cifra=[];decifra=[]; mensagem=''

#Recebendo a mensagem
texto=input("Digite a mensagem a ser cifrada: ")

#Instruções de utilização
print("\nSua mensagem foi atribuida a variavel 'texto'.\nPara cifrar/decifrar sua mensagem:\n- cifrar(texto)\n- decifrar(cifra)\n")


#Função que cifra a mensagem baseado no metódo de hill
def cifrar(texto):
    global cifra;mtexto;msg;mchave;

    #Quebrando a mensagem em letras e convertendo para o respectivo indice
    for letra in texto:
        mtexto.append(letra)
        msg.append(alfa.index(letra))
        mchave.append(random.randint(1,9))


    #Realiza a multiplicação o vetor mensagem e a chave
    for i in range(len(msg)):
        cifra.append(msg[i]*mchave[i])

    print("Mensagem cifrada: \n",cifra,"\nChave: \n ",mchave)


#Função que decifra a mensagem baseada na chave fornecida.
def decifrar(cifra):
    global mensagem;decifra;

    #Calcula a matriz com a mensagem decifrada
    for i in range(len(cifra)):
        decifra.append(int(cifra[i]/mchave[i]))

    #Concatena os elementos da matriz decifrada para texto plano
    for i in decifra:
        mensagem = mensagem + alfa[i]
            
    print("Mensagem decifrada: \n\n\t'%s'" %mensagem)

###################################
##                               ##
##   Criado por Wesley Azevedo   ##
##                               ##
###################################
