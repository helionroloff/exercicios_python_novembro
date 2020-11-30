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


def folha_salarial(salario_por_hora:float,horas_trabalhadas_mes:float):
    salario_bruto = (salario_por_hora * horas_trabalhadas_mes)

    print(f'''
    {"-"*50}
    {"-"*50}
    Salário Bruto: R$ {salario_bruto}
    {"-"*50}
    {"-"*50}
    DESCONTO IR (11%): R$ {salario_bruto - salario_bruto * 0.11:.2f}
    DESCONTO INSS (8%): R$ {salario_bruto - salario_bruto * 0.08:.2f}
    DESCONTO SINDICATO (5%): R$ {salario_bruto - salario_bruto * 0.05:.2f}
    SALÁRIO LÍQUIDO : R$ {salario_bruto - salario_bruto * 0.24:.2f}
    {"-"*50}
    ''')

if __name__ == "__main__":
    
    
    
    while True:
        try:
            salario_por_hora = float(input('informe quanto você ganha por hora: '))
            break
        except ValueError as erro:
            print(erro)
            print('valor inválido, tente novamente')
    while True:    
        try:    
            horas_trabalhadas_mes = int(input('informe a quantidade de horas trabalhadas por mês: '))
            break
        except:
            print('valor inválido, tente novamente')

    folha_salarial(salario_por_hora,horas_trabalhadas_mes)