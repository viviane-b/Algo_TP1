#Nom, Matricule
#Nom, Matricule

import math
import sys
INFINITY = math.inf

#Fonctions pour lire/écrire dans les fichier. Vous pouvez les modifier, 
#faire du parsing, rajouter une valeur de retour, mais n'utilisez pas
#d'autres librairies.
#Functions to read/write in files. you can modify them, do some parsing,
#add a return value, but don't use other librairies



def read_problems(input_file):
    # lecture du fichier/file reading
    file = open(input_file,"r")
    lines = file.readlines()
    file.close()

    numberOfGraphs = int(lines[0].replace("\n", ""))
    Graphs = [[0]]*numberOfGraphs
    line = 1
    for i in range(numberOfGraphs):
        
        nbVertices = int(lines[line])
        Vertices = [0]*nbVertices       # initialize array


        for j in range (nbVertices):
            coord = lines[line+1+j].split(" ")

            x = float(coord[0])
            y = float(coord[1].replace("\n", ""))
            Vertices[j] = [x, y]

        line += nbVertices +1
        Graphs[i] = Vertices


    return Graphs

        
    
        


def write(fileName, content):
    #écrire la sortie dans un fichier/write output in file
    file = open(fileName, "w")
    file.write(content)
    file.close()


#Distance entre sommet u et sommet v
def distance(u, v):
    return math.sqrt((u[0]-v[0])**2 + (u[1]-v[1])**2)

#Trouver la distance minimum
def findMin(dist, vertToAdd):
    min = vertToAdd[0]
    for u in vertToAdd:
        d = dist[u]
        if d < dist[min]:
            min = u
    return min


#Fonction main/Main function
def main(args):
    input_file = args[0]
    output_file = args[1]
    Graphs = read_problems(input_file)

    toWrite = ""

    for g in Graphs:

        vertices = g
        dist = [INFINITY]*len(vertices)     # Distances de chaque sommet au graphe en cours
        vertToAdd = list(range(0, len(vertices)))  # Sommets qui restent a ajouter a la solution
        vertToAdd.pop(0)
        
        firstVertex = vertices[0]
        dist[0] = 0
        v = firstVertex
        for u in vertToAdd:
            dist[u] = distance(v, vertices[u])


        totalDist = 0 

        while (len(vertToAdd) > 0 ):
            min = findMin(dist, vertToAdd)

            vertToAdd.remove(min)
            totalDist += dist[min]


            # Mettre a jour les distances
            for u in vertToAdd:
                d = distance(vertices[u], vertices[min])
                if d < dist[u]:
                    dist[u] = d
            
        toWrite += str(totalDist) + "\n"

    write(output_file, toWrite)







# TODO
# Parse du fichier
# Calculer la distance entre les sommets = cout
# faire l'algo d'ACM: Prim
# calculer la somme de cout de l'ACM
# ecrire dans le fichier d'output








#NE PAS TOUCHER
#DO NOT TOUCH
if __name__ == '__main__':
    main(sys.argv[1:])
