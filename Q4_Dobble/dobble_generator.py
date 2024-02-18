#Nom, Matricule
#Nom, Matricule

# cette classe sert a créer les cartes du jeu dans le fichier cartes.txt
# this class is used to create the game cards in the cartes.txt file

import random # pour le melange des symboles sur chaque carte # for mixing symbols on each card

class Generator():
    def __init__(self, order = 7):
        self.order = order

    def generate(self, cards_file = "cartes.txt", verbose = False):
        if verbose :
            print("***Generation des cartes***")

        # Assigner les bons symboles aux cartes
        n = self.order
        #length = n*n+n+1

        # initialize matrix
        matrixNN = [[] for _ in range(n*n)]
        matrixNN1 = [[]]*(n*n)
        dir = [[] for _ in range(n+1)]
        symbol = 1      #represente une image

        for k in range(n):        #les n*n premieres directions

            for s in range(n):           #une case sur chaque ligne  
                #print("s=", s)

                for i in range (n):     #chaque symbole dans une meme direction 
                    #print("i=",i)
                    #print(i*n+ (s+((i*k)%n))%(n))
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
        

        print(matrixNN)
        print(dir)



        # Randomization
        #TODO : trouver algo pour randomizer


        # ecrire fichier
        towrite = ""
        for line in matrixNN:
            for number in line:
                towrite += str(number) + " "
            towrite += "\n"



    def write(fileName, content):
    #écrire la sortie dans un fichier/write output in file
        file = open(fileName, "w")
        file.write(content)
        file.close()    



        # TODO
        # a completer

        # melange aleatoire des symboles sur les cartes,
        # pour ne pas avoir des répétitions de symboles sur les mêmes endroits des cartes
        # random mixing of symbols on the cards,
        # so as not to have repetitions of symbols on the same places on the cards
            
        # TODO
        # a completer


        # ecriture des cartes dans le fichier cards_file
        # writing cards in the cards_file file
            
        # TODO
        # a completer
