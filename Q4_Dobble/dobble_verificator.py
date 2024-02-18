# Cassandre Hamel, 20210863
# Viviane Binet, 20244728


# cette classe sert a verifier la validite de l'ensemble des cartes du jeu dans le fichier cartes.txt
# this class is used to check the validity  of the game cards set in the cartes.txt file

# doit retourner 0 si tout est correct, 1 si le jeu n'est pas optimal selon l'ordre et 2 si le jeu n'est pas valide
# should return 0 if everything is correct, 1 if the game set is not optimal according to the order and 2 if the game set is invalid

#import os.path

class Verificator():
    def __init__(self):
        pass

    def verify(self, cards_file = "cartes.txt", verbose = False):
        if verbose :
            print("***Verification des cartes***")

        #file reading
        file = open(cards_file,"r")
        lines = file.readlines()
        file.close()   

        cards = []


        for line in lines:                   # one card
            l = line.removesuffix("\n")
            numbers = l.split()  

            for i in range(len(numbers)):
                numbers[i] = int(numbers[i])
            cards.append(numbers)
        
        

        order = len(cards[0]) -1           # supposed order based on the fisrt card

        maxSymbol = 1                      # number of symbols in total, should be n^2 + n + 1

        for i in range(len(cards)):
            if len(cards[i]) != (order + 1):
                return 2                        # game is not valid, number of symbols is not the same on all cards

            
            # pair of symbols
            # for symbol in cards[i]:
            for j in range(i):                  # card 0 to i-1

                corr = 0                   # no correspondance
                for symbol0 in cards[i]:

                    if symbol0 > maxSymbol:
                        maxSymbol = symbol0     # update maxSymbol


                    for symbol1 in cards[j]:
                        corr += (symbol0 == symbol1)
                        

                if corr != 1:               # no correspondance was found or more than one
                    return 2


            for j in range(i+1, len(cards)):    # card i+1 to end
                corr = 0                   # no correspondance
                for symbol0 in cards[i]:
                    if symbol0 > maxSymbol:
                        maxSymbol = symbol0     # update maxSymbol

                    for symbol1 in cards[j]:
                        corr += (symbol0 == symbol1)
                
                if corr != 1:               # no correspondance was found or more than one
                    return 2


        if maxSymbol != order*order + order +1:
            return 1

        if len(cards) != (order*order + order + 1): 
            return 1                            # game is not optimal, not n^2 + n + 1 cards
            
        # test: the number of cards should be optimal
        # test: the number of symbols per card is the same for each card
        # test: each pair of cards always shares one and only one symbol in common
        # test: the total number of symbols should be optimal



        # succes (0) si le jeu est valide et optimal
        # avertissement (1) si le jeu de carte n'est pas optimal
        # erreur (2) si le jeu de carte n'est pas valide
            
        # success (0) if the game is valid and optimal
        # warning (1) if the card game is not optimal
        # error (2) if the card set is invalid
        return 0

        
