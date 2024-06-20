nome= str(input('Digite seu nome: '))
nome= nome.title()
if nome.count(' ')>0:
    palavras = nome.split()
    abre= palavras[2]
    palavras[2]=abre[0:1]+"."
    nome = ' '.join(palavras)
print(nome)