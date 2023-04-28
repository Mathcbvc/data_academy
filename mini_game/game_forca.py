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
    
    pontilhado = ["_" for letra in palavra]
    tentativas = 6
    digitadas = []

    while tentativas > 0:
        limpaTela()# chama a função criada para limpar a tela antes do jogo começar
        print("\nBem-vindo(a) ao jogo da forca!")
        print("Adivinhe a palavra abaixo:\n")# imprime na tela e quebra a linha logo em após
        print(" ".join(pontilhado)) # faz um 'join' que retorna uma string a partir de um iteravel de string adicionando o espaço em branco
        print("\nChances restantes: {}".format(tentativas))# utilização de placeholders para gravar
        print("Letras erradas:"," ".join(digitadas))# mesmma lógica do join anterior. Dessa vez para imprimir na tela as letras que estão sendo digitadas

        tentativa = input("\nDigite uma letra: ").lower()#para facilitar tratamento, colocamos em lowercase

        if tentativa in palavra:#verifica se a letra digitada consta dentro da string
            
            #index = 0 # controla o indice da palavra
            for indice,letra in enumerate(palavra):
                pontilhado[indice] = letra #substitui o traço pontilhado pela letra digitada
        
            #index += 1 # passa para o próximo  indice
        else:
            tentativas -= 1 # diminui as tentativas
            digitadas.append(tentativa) #adiciona a tentativa errada na lista de digitadas
            print("Letra incorreta!")

        if "_" not in pontilhado: # testa se existe pontilhado dentro da palavra oculta, se não tiver o jogo acabou
            print("Você venceu!A palavra era: {}".format(palavra))
            break
    
    if "_" in pontilhado:
        print("Você perdeu! A palavra era: {}".format(palavra))


#bloco main -> É usado para informar ao interpretador que isso aqui é um programa, é um módulo Python.

if __name__  == "__main__":
    game()# chama a funcao game criada.
   


