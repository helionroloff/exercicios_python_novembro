from random import randint
# Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor . Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados. 
numeros = []

for i in range (1,101):
    i = randint(1,6)
    numeros.append(i)

# seria interessante colocar o print dentro de um for i in range(1, 7), assim você não precisaria escrever tantos prints
# mas isso é questão de gosto também  ;)
print(numeros)
print(f'numero 1: {numeros.count(1)} x')
print(f'numero 2: {numeros.count(2)} x')
print(f'numero 3: {numeros.count(3)} x')
print(f'numero 4: {numeros.count(4)} x')
print(f'numero 5: {numeros.count(5)} x')
print(f'numero 6: {numeros.count(6)} x')