#Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição e no qual a soma das linhas, colunas e diagonais é a mesma. Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:

#     8  3  4 
#     1  5  9
#     6  7  2

#     Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima. Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado. Usar um vetor de 1 a 9 parece ser mais simples que usar uma matriz 3x3. 


from itertools import permutations
#importei a função permutations para fazer o cálculo de todas as possibilidades possiveis 
#dentro de uma lista de números pré-definidos.




listas_possiveis = list(permutations([1,2,3,4,5,6,7,8,9]))
quadrados_magicos = 0
#se for um quadrado mágico será acrescentado pelo contador
print(len(listas_possiveis))
for quadrado in listas_possiveis:
    soma = quadrado[0] + quadrado[1] + quadrado[2]
    contador = 0
    
    for i in range(0,7,3):
#o range irá da posição 0 a 7, pulando de 3 em 3, passando pela posição 0, 3, 6
        if (quadrado[i] + quadrado[i+1] + quadrado[i+2]) == soma:
            contador = contador + 1
        else:
            break
    
    if contador < 3:
        continue
    
    for i in range(3):
#o range irá passar 3x, passando pela posição 3, 6, 9
        if (quadrado[i] + quadrado[i+3] + quadrado[i+6]) == soma:
            contador = contador + 1
        else:
            break 
            
    if contador < 6:
        continue
    
    for i in range(0,3,2):
#o range irá da posição 0 a 3, pulando de 2 em 2, passando pela posição 0 e 3
        if (quadrado[0+i] + quadrado[4] + quadrado[8-i]) == soma:
            contador = contador + 1

    if contador < 8:
        continue

#ao final de cada for será impresso caso o contador seja menor que 8
#o contador vai até 8 porque pelas pesquisas são 8 possibilidades de quadrado mágico possíveis.
    else:
        quadrados_magicos +=1
        print(f'''Quadrado Mágico Número {quadrados_magicos}
        {quadrado[0]} {quadrado[1]} {quadrado[2]}
        {quadrado[3]} {quadrado[4]} {quadrado[5]}
        {quadrado[6]} {quadrado[7]} {quadrado[8]}''')

