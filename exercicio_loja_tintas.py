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

# seria legal dar uma separada nas tarefas em funções
# outra ponto seria colocar os valores fixos, como quantidade de litros de uma lata ou galão, tal como seu preço, em variáveis já no início do programa
# assim se o valor ou a capacidade sofresse alguma alteração você só precisaria alterar em um lugar


#cálculo para latas necessárias e valor de custo utilizando latas de 18 litros
litros_necessários = metragem / 6

latas = (litros_necessários // 18)

# aqui ao invés de usar if else, você poderia ter usado apenas if not litros_necessários % 18 == 0: latas += 1, mas é isso ai ;)
if litros_necessários % 18 == 0:
    latas = latas
else:
    latas = latas + 1
valor = latas * 80

print(f'''
ORÇAMENTO PARA LATAS DE 10L
METRAGEM: {metragem} mt²
LITROS NECESSÁRIOS: {litros_necessários:.2f} litros
LATAS: {int(latas)} un
VALOR TOTAL: R$ {valor:.2f}
''')

# note que o processo para calcular o orçamentos para latas e galões é o mesmo e o print essencialmente também
# então, você poderia fazer uma função para calcular orçamento, que recebe por ex, 
# os litros necessários, a quantidade de litros da lata ou galão (3.6 ou 18) e o seu respectivo valor


#cálculo para latas necessárias e valor de custo utilizando latas de 3.6 litros
litros_necessários = metragem / 6

galao = (litros_necessários // 3.6) + 1

if litros_necessários % 3.6 == 0:
    galao = galao
    valor = galao * 25
else:
    galao = galao + 1
    valor = galao * 25
print(f'''
ORÇAMENTO PARA LATAS DE 3.6L
METRAGEM: {metragem} mt²
LITROS NECESSÁRIOS: {litros_necessários:.2f} litros
LATAS: {int(galao)} un
VALOR TOTAL: R$ {valor:.2f}
''')

#cálculo para latas necessárias e valor de custo utilizando latas mistas
latas_18 = metragem // 108
metragem_restante = metragem%108
galao_3_6 = metragem_restante // 21.6
if metragem_restante % 21.6 != 0:
    galao_3_6 = galao_3_6 + 1



print(f'''
METRAGEM: {metragem} mt²
QUANTIDADE DE LATAS DE 18L: {latas_18} un
QUANTIDADE DE LATAS DE 3.6L: {galao_3_6} un
VALOR: {(latas_18 * 80) + (galao_3_6 * 25)}

''')