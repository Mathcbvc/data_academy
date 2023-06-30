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
    def guess(self, x):
        return x in self.word
	# Método para verificar se o jogo terminou
    def isOver(self):
        pass
    # Método para verificar se o jogador venceu
    def isWinner(self):
        pass	
	# Método para não mostrar a letra no board
    def hideStatus(self):
         pass
	# Método para checar o status do game e imprimir o board na tela
    def showStatus(self):
         pass

