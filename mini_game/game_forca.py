import random
from os import system, name

def limpaTela():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def game(): 
    limpaTela()

    palavras = ['abacaxi', 'holofote', 'giroscopio', 'belzebu', 'bicicleta', 'tomada', 'carro','girafa', 'lotus', 'cumaru', 'balanço', 'hotel', 'maracutaia', 
                'onibus', 'sofa', 'patins', 'sistema', 'palavra', 'biblioteca', 'corrente', 'portal','pamonha','milho', 'galinha', 'vaca', 'cabrito', 'pedregulho']
    palavra = random.choice(palavras)
    
    pontilhado = ["_" for letra in palavra]
    tentativas = 6
    digitadas = []
    index = 0 # controla o indice da palavra

    while tentativas > 0:
        limpaTela()# chama a função criada para limpar a tela antes do jogo começar
        print("\nBem-vindo(a) ao jogo da forca!")
        print("Adivinhe a palavra abaixo:\n")# imprime na tela e quebra a linha logo em após
        print(" ".join(pontilhado)) # faz um 'join' que retorna uma string a partir de um iteravel de string adicionando o espaço em branco
        print("\nChances restantes: {}".format(tentativas))# utilização de placeholders para gravar
        print("Letras erradas:"," ".join(digitadas))# mesmma lógica do join anterior. Dessa vez para imprimir na tela as letras que estão sendo digitadas

        tentativa = input("\nDigite uma letra: ").lower()#para facilitar tratamento, colocamos em lowercase

        if tentativa not in palavra:
            print('Letra {} não está na palavra {} \n'.format(tentativa,palavra))
            tentativas -=1
            digitadas += tentativa
        elif tentativa in palavra:
            print('Letra {} tem na palavra! \n'.format(tentativa))
            for index,letra in enumerate(palavra):
                if(letra == tentativa):
                    pontilhado[index] = tentativa
        if '_' not in pontilhado:
            print('\n Você acertou! A palavra é {} \n'.format(palavra.upper()))
            break
    
    if '_' in pontilhado:
        print('\n Você perdeu! A palavra era {} \n'.format(palavra.upper()))
    

#bloco main -> É usado para informar ao interpretador que isso aqui é um programa, é um módulo Python.

if __name__  == "__main__":
    game()# chama a funcao game criada.