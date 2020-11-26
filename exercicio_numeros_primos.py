#Faça um programa que gera uma lista dos números primos existentes entre 1 e 
# um número inteiro informado pelo usuário. 

numero = int(input('informe o número desejado: '))
numeros_primos = []
for i in range(1,numero + 1):
    cont = 0
    for x in range(1, i + 1):
        if i%x == 0:
            cont = cont+1
    if cont == 2:
        numeros_primos.append(x)

print(numeros_primos)


