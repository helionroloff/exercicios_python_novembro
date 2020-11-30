# Faça um Programa que peça os 3 lados de um triângulo.
# O programa deverá informar se os valores podem ser um triângulo.
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno. 
def formacao_triangulo():
    while True:
        try:
            lado_a = int(input('informe o tamanho do lado 1 do triangulo: '))
            break
        except ValueError as erro:
            print(erro)
            print('digite um valor valido')
    while True:
        try:    
            lado_b = int(input('informe o tamanho do lado 2 do triangulo: '))
            break
        except ValueError as erro:
            print(erro)
            print('digite um valor valido')
    while True:        
        try:
            lado_c = int(input('informe o tamanho do lado 3 do triangulo: '))
            break
        except ValueError as erro:
            print(erro)
            print('digite um valor valido')

    if lado_a < lado_b + lado_c and lado_b < lado_a + lado_c and lado_c <lado_a + lado_b:
        print('TRIANGULO É POSSÍVEL')
        if lado_a == lado_b and lado_b == lado_c:
            print('TRIANGULO EQUILÁTERO')
        elif lado_a != lado_b and lado_b != lado_c and lado_c != lado_a:
            print('TRIANGULO ESCALENO')
        else:
            print('TRIANGULO ISÓCELES')
    else:
        print('TRIANGULO NÃO POSSÍVEL')

if __name__ == "__main__":
    
    formacao_triangulo()