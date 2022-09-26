idade = int(input("Digite sua idade: "))

#Estruturas de controle de fluxo(if..else)
if(idade >=18):
    print("Já pode tirar a carteira de motorista")
else:
    print("Ainda não pode tirar a carteira de motorista")

#Estrura de controle de fluxo(elif)
numero_sorteado = 5
numero = int(input("Digite um número entre 1 e 10: "))
if(numero == numero_sorteado):
    print("Você acertou o número sorteado!")
elif(numero> numero_sorteado):
    print("Seu número é maior que o número sorteado.")
else:
    print("Seu número é menor que o número sorteado.")