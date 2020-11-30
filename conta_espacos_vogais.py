# Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

#     quantos espaços em branco existem na frase.
#     quantas vezes aparecem as vogais a, e, i, o, u. 
def contador_vogais_espacos(frase:str):
    frase = frase.lower()
    print(f'''
    FRASE: {frase}
    QUANTIDADE DE VOGAIS (A): {frase.count('a')}
    QUANTIDADE DE VOGAIS (E): {frase.count('e')}
    QUANTIDADE DE VOGAIS (I): {frase.count('i')}
    QUANTIDADE DE VOGAIS (O): {frase.count('o')}
    QUANTIDADE DE VOGAIS (U): {frase.count('u')}
    QUANTIDADE DE ESPAÇOS EM BRANCO: {frase.count(' ')}
    ''')

if __name__ == "__main__":

    frase = str(input('INFORME A FRASE A SER ANALISADA: '))
    contador_vogais_espacos(frase)