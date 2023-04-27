import random
from os import system, name

def limpaTela():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def game(): 
    limpaTela()

    palavras = ['abacaxi', 'holofote', 'giroscopio', 'belzebu', 'bicicleta', 'tomada', 'carro','girafa', 'lotus', 'cumaru']
    
    palavra = random.choice(palavras)
    
    pontilhado = ["-" for letra in palavra]
    tentativas = 6
    digitadas = []

    while tentativas > 0:
        limpaTela()
        print("\nBem-vindo(a) ao jogo da forca!")
        print("Adivinhe a palavra abaixo:\n")
        print(" ".join(pontilhado))
        print("\nChances restantes: {}".format(tentativas))
        print("Letras erradas:"," ".join(digitadas))

        tentativa = input("\nDigite uma letra: ").lower()

        if tentativa in palavra:
            index = 0
            for letra in palavra:
                pontilhado[index] = letra
            index += 1
        else:
            tentativas -+ 1
            digitadas.append(tentativa) 