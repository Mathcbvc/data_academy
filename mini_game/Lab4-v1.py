# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

	# Método Construtor
    def __init__(self):
        self.word = random.choice(["abacate","vandalo","ombrelone","cortina","jurassico","ampola","obsidiana","troia","unicornio"])
        self.triesLeft = len(board)
	# Método para adivinhar a letra
    def guess(self, attempt):
        if attempt in self.word:
            #substituir _ na palavra se a palavra tiver a letra 
            self.triesLeft -= 1
            pass
        else:
            self.triesLeft -= 1
	# Método para verificar se o jogo terminou
    def isOver(self):
        #testa se na palavra já não possui nenhum '_'
        if self.triesLeft == 0 : 
            print("GAME OVER") 
    # Método para verificar se o jogador venceu
    def isWinner(self):
        if 	'_' not in self.word and self.triesLeft > 0 : 
            print("VOCE GANHOU!")
	# Método para não mostrar a letra no board
    def hideWord(self):
        #imprimir na tela apenas os traços ao invés da palavra. Criar uma lista secundária contendo apenas '_'
        self.temp = ['_' for x in self.word]
	# Método para checar o status do game e imprimir o board na tela
    def boardController(self):
        #controlar o board do game. 
        pass
