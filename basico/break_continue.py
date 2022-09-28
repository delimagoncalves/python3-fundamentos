#Instruções internas em laços de repetição

num = 0

while(num<10):
    num+=1
    if(num == 5):
        break#encerra o laço

print(num)

for n in range(1,11):
    if(n == 5):
        continue#pula o laço para próxima iteração
    print(n)
