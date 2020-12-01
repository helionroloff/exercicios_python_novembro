# construa um analisador das 5 principais combinações de mãos do poker.
# Para isso utilize como base as classes descritas em:
# https://penseallen.github.io/PensePython2e/18-heranca.html
# considere como regra o poker fechado, em que a mão do jogador, já tem a combinação de 5 cartas :)

class Card:
    """Representa a classe carta"""
    nome_do_naipe = ["Ouro", "Paus", "Espadas", "Copas"]
    numero_da_carta = [None, "2", "3", "4", "5", "6", "7",
                     "8", "9", "10", "Valete", "Dama", "Rei", "Ás"]


    def __init__(self, naipe = 0, numero = 2):
        '''iniciação da classe'''
        self.naipe = naipe
        self.numero = numero
    
    
    def __str__(self):
        '''descrição da classe'''
        return (f"{Carta.numero_da_carta[self.numero]} "
                f"de {Carta.nome_do_naipe[self.naipe]}")
    
    
    def __lt__(self, other):
        pass
    #eu não entendi o funcionamento pelo link no cabeçalho do exercicio
    


class Baralho():
    '''adicionando cartas no baralho'''
    def __init__(self):
        self.baralho = []
        for naipe in range(4):
            for numero in range(1,14):
                carta = Carta(naipe , numero)
                self.baralho.append(carta)
    

    def  __str__(self):
        '''descrição do baralho'''
        baralho = []
        for carta in self.baralho:
            baralho.append(str(carta))
        return '\n'.join(baralho)


    def retirar_carta(self):
        return self.baralho.pop()


    def adicionar_carta(self, carta):
        self.baralho.append(carta)


    def embaralhar(self):
        random.shuffle(self.baralho)




