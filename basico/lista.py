# Trabalhando com Listas em python

# Lista em python, semelhante ao array em java
numeros = [1,2,3,4,5]

# Exibindo valor da lista através do índice
print("Valor na posição [0]: "+str(numeros[0]))

# Exibindo valor através de índice negativo
print("Valor na posição [-1]: "+str(numeros[-1]))# Pega o último elemento da lista

# ALterando valor na lista através do índice
numeros[0]=10

print(str(numeros[0]))

# Obtendo nova lista através do operador de slice
subLista = numeros[0:3]#obtem os valores da lista até o último índice -1
print(subLista)

# Concatenação de Listas
frutas = ['laranja','abacate']
bebidas = ['leite','água']
listaMercado = frutas + bebidas
print(listaMercado)

# Multiplicando Listas
multLista = frutas * 3
print(multLista)

# Percorrendo listas com for.. in.. range
mercado = ['abacate','feijão','arroz','alface','café']
print("Itens da lista de compras:")
for item in range(len(mercado)):
    print(str(item)+"-"+mercado[item])

# Utilizando oepradores (int) e (not)
itemMercado = input("Digite o nome do item: ")
encontrado = itemMercado in mercado
if encontrado:
    print("Item está na lista")
else:
    print("Item não esá na lista")