from random import randint
# Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor . Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados. 

def lancador_dados():
    numeros = []

    for i in range (1,101):
        n = randint(1,6)
        numeros.append(n)
        print(f'jogada {i}: número {n}')

    print(f'''
numero 1: {numeros.count(1)} x
numero 2: {numeros.count(2)} x
numero 3: {numeros.count(3)} x
numero 4: {numeros.count(4)} x
numero 5: {numeros.count(5)} x
numero 6: {numeros.count(6)} x
    ''')

if __name__ == "__main__":

    lancador_dados()        
    