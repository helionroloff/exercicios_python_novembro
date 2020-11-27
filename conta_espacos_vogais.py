# Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

#     quantos espaços em branco existem na frase.
#     quantas vezes aparecem as vogais a, e, i, o, u. 
def contador_vogais_espacos(frase):
    # acho que seria interessantante adicionar algum método para ele contar as vogais com acentos, eu usei o modulo inicodedata, 
    # então fica a dica ;)
    # outro ponto é que você esqueceu de colocar as vogais no count() e colocou a, b, c, d,e (acontece com os melhores hahah)
    frase = frase.lower()
    print(f'''
    FRASE: {frase}
    QUANTIDADE DE VOGAIS (A): {frase.count('a')}
    QUANTIDADE DE VOGAIS (E): {frase.count('b')}
    QUANTIDADE DE VOGAIS (I): {frase.count('c')}
    QUANTIDADE DE VOGAIS (O): {frase.count('d')}
    QUANTIDADE DE VOGAIS (U): {frase.count('e')}
    QUANTIDADE DE ESPAÇOS EM BRANCO: {frase.count(' ')}
    ''')

if __name__ == "__main__":

    frase = str(input('INFORME A FRASE A SER ANALISADA: '))
    contador_vogais_espacos(frase)