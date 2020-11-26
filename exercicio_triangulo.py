# Faça um Programa que peça os 3 lados de um triângulo.
# O programa deverá informar se os valores podem ser um triângulo.
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno. 

lado_a = int(input('informe o tamanho do lado  do triangulo: '))
lado_b = int(input('informe o tamanho do lado  do triangulo: '))
lado_c = int(input('informe o tamanho do lado  do triangulo: '))

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