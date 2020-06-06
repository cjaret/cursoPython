import random 
import os

#declaramos una constante con las diferentes posiciones del ahorcado

IMAGES = [
'''

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
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
'''

]


WORDS = [ 'secadora','moto','mariposa','computadora' ]   

def random_word():
    word = WORDS[random.randrange(len(WORDS))]
    return word

def display_board(hidden_word,tries):
    print(IMAGES[tries])
    print (hidden_word)

def run():
    word = random_word()
    hidden_word=[' __ ']*len(word)
    tries = 0

    while True:
        display_board(hidden_word,tries)
        current_letter = str(input('ingresa la letra : '))

        index =[]
        for idx in range(len(word)):
            if current_letter == word[idx]:
                index.append(idx) 
                # print(index) => Muestra los index donde estan las letras

        if len(index)==0 or hidden_word[index[0]]!=' __ ':
            tries+=1
            if tries == 7:
                display_board(hidden_word,tries)
                print('\n')
                print('¡Perdiste! La palabra escondida es {}'.format(word))
                break

        else:
            for i in range(len(index)):
                hidden_word[index[i]]=current_letter
           
        try:
            hidden_word.index(' __ ')
        except ValueError:
            display_board(hidden_word,tries)
            print('\n')
            print('¡Felicidades!!! ganaste')
            break

        os.system('cls')
       
        
if __name__=='__main__':

    print(''' 

  ____  _                           _     _       
 |  _ \(_)                         (_)   | |      
 | |_) |_  ___ _ ____   _____ _ __  _  __| | ___  
 |  _ <| |/ _ \ '_ \ \ / / _ \ '_ \| |/ _` |/ _ \ 
 | |_) | |  __/ | | \ V /  __/ | | | | (_| | (_) |
 |____/|_|\___|_| |_|\_/ \___|_| |_|_|\__,_|\___/ 
                                                  
               +---+
           |   |
           o
          /|\  |
           |   |
          / \  |
          =========                                         
*************************************************
\n \n \n
 ''')
  
    run()