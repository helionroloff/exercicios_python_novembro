#Faça um programa que gera uma lista dos números primos existentes entre 1 e 
# um número inteiro informado pelo usuário. 
def numeros_primos(intervalo):
    numeros_primos = []
    for i in range(1,numero + 1):
        cont = 0
        for x in range(1, i + 1):
            if i%x == 0:
                cont = cont+1
        if cont == 2:
            numeros_primos.append(x)
    return numeros_primos


if __name__ == "__main__":
    
    while True:
        numero = int(input('números primos no intervalo de 1 a: '))
        resultado = numeros_primos(numero)
        print(*resultado)
        nova_consulta = input('DESEJA FAZER OUTRA CONSULTA? S - N').upper()
        if nova_consulta == 'N':
            print('OBRIGADO')
            break
    


