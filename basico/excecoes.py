# Tratando exceções em python
# Utilizando o bloco try..except

# Exemplo simples com divisão por zero
def div(numero,divisor):
    try:
        print(str(numero / divisor))
    except ZeroDivisionError:
        print("Argumento inválido!")

div(10,2)
div(10,0)
div(5,0)
div(10,5)
        