# Função em python
def imprime():
    print("Hello!")

# Função com argumentos
def soma(n1,n2):
    print(str(n1+n2))

# Função com retorno de valor
def sub(n1,n2):
    return n1-n2
# Podemos omitir a palavra return caso haja apenas um valor de retorno
def sub2(n1,n2):
        n1-n2

# Executando as funções
imprime()
soma(4,8)
resultado = sub(10,5)
resultado2 = sub(15,5)
print(str(resultado))
print(str(resultado2))