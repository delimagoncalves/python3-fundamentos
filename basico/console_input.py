# Utilizando função input() para capturar entrada no console

print("Hello World!")

#Função input retorna string por padrão
nome = input("Enter your name: ")

print("It is goog to meet you, "+nome)

# Obtendo o tamanho da string nome
tamanho = len(nome)

# Usando str() para converter a saída em string
print("The length of your name is: "+str(tamanho))

age = input("What's your age?")

print("You will be "+str(int(age)+1)+" in a year")