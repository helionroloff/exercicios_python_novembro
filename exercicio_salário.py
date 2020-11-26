# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

#     salário bruto.
#     quanto pagou ao INSS.
#     quanto pagou ao sindicato.
#     o salário líquido.
#     calcule os descontos e o salário líquido, conforme a tabela abaixo: 
#     + Salário Bruto : R$
#     - IR (11%) : R$
#     - INSS (8%) : R$
#     - Sindicato ( 5%) : R$
#     = Salário Liquido : R$


def folha_salarial(salario_por_hora,horas_trabalhadas_mes):
    salario_bruto = (salario_por_hora * horas_trabalhadas_mes)

    print(f'''
    Salário Bruto: R$ {salario_bruto}
    DESCONTO IR (11%): R$ {salario_bruto - salario_bruto * 0.11}
    DESCONTO INSS (8%): R$ {salario_bruto - salario_bruto * 0.08}
    DESCONTO SINDICATO (5%): R$ {salario_bruto - salario_bruto * 0.05}
    SALÁRIO LÍQUIDO : R$ {salario_bruto - salario_bruto * 0.24}
    ''')

if __name__ == "__main__":
    salario_por_hora = float(input('informe quanto você ganha por hora: '))
    horas_trabalhadas_mes = int(input('informe a quantidade de horas trabalhadas por mês: '))

    folha_salarial(salario_por_hora,horas_trabalhadas_mes)