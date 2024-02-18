# Cassandre Hamel, 20210863
# Viviane Binet, 20244728


# cette classe sert a créer les cartes du jeu dans le fichier cartes.txt
# this class is used to create the game cards in the cartes.txt file

import random # pour le melange des symboles sur chaque carte # for mixing symbols on each card
import math

class Generator():
    def __init__(self, order = 7):
        self.order = order

    def generate(self, cards_file = "cartes.txt", verbose = False):
        if verbose :
            print("***Generation des cartes***")

        # Assigner les bons symboles aux cartes
        n = self.order
    

        # initialiser la matrice
        matrixNN = [[] for _ in range(n*n)]
        matrixNN1 = [[]]*(n*n)
        dir = [[] for _ in range(n+1)]
        symbol = 1      #represente une image

        for k in range(n):        #les n*n premieres directions

            for s in range(n):           #une case sur chaque ligne  
                

                for i in range (n):     #chaque symbole dans une meme direction 
                    
                    matrixNN[i*n+ (s+((i*k)%n))%(n) ].append(symbol)


                dir[k].append(symbol)
                symbol +=1

        #directions horizontales
        for k in range(n):      
            for s in range(n):
                matrixNN[k*n+s].append(symbol)
            dir[n].append(symbol)
            symbol +=1

        #tableau n+1
        for s in dir:
            s.append(symbol)
        

        

        cards = matrixNN + dir
        print(cards)


        # Randomization
        # https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle
        # Fisher-Yates shuffle
        temp = 0

        for card in cards:
            for i in range (len(card)):
                r = math.floor(i*random.random())
                temp = card[i]
                card[i]=card[r]
                card[r]=temp
        print(cards)        






        # ecrire fichier
        towrite = ""
        for line in cards:
            for number in line:
                towrite += str(number) + " "
            towrite += "\n"

        
        
        file = open(cards_file, "w")
        file.write(towrite)
        file.close()  

    


