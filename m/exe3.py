nome= str(input('Digite seu nome: '))
palavras = nome.split()
abre= palavras[1]
palavras[1]=abre[0:1]+"."
nome = ' '.join(palavras)   
print(nome)