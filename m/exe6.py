nome= str(input('Digite seu nome: '))
nome= nome.title()
nome = nome.split()
sep= nome[1]
misc= sep.lower()
nome= " ".join(nome)
print(nome.replace(sep, misc))