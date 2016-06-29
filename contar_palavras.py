import string


arq = open('alice.txt')
texto = arq.read()
texto = texto.lower()
for c in string.punctuation:
    texto = texto.replace(c,' ')
texto = texto.split()

dic ={}
for p in texto:
    if p not in dic:
        dic[p] = 1
    else:
        dic[p] += 1

palavra=str(input("Digite a palava a ser contada: "))
contar = dic[palavra]
print("\nA palavra %s aparece: %d vezes" %(palavra,contar))

arq.close()
