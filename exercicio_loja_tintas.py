######################################################################################################

# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

#     Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#     comprar apenas latas de 18 litros;
#     comprar apenas galões de 3,6 litros;
#     misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
# 

####################################################################################################### 

metragem = float(input('INFORME QUANTOS MT² POSSUI A ÁREA A SER PINTADA: '))


#cálculo para latas necessárias e valor de custo utilizando latas de 18 litros
litros_necessários = metragem / 6

latas = (litros_necessários // 18)

if litros_necessários % 18 == 0:
    latas = latas
else:
    latas = latas + 1
valor = latas * 80

print(f'''
METRAGEM: {metragem} mt²
LITROS NECESSÁRIOS: {litros_necessários:.2f} litros
LATAS: {int(latas)} un
VALOR TOTAL: R$ {valor:.2f}
''')



#cálculo para latas necessárias e valor de custo utilizando latas de 18 litros
litros_necessários = metragem / 6
latas = (litros_necessários // 3.6) + 1
if litros_necessários % 3.6 == 0:
    latas = latas
valor = latas * 25

print(f'''
METRAGEM: {metragem} mt²
LITROS NECESSÁRIOS: {litros_necessários:.2f} litros
LATAS: {int(latas)} un
VALOR TOTAL: R$ {valor:.2f}
''')
