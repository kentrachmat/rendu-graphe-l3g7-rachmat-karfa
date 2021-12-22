import functions as ft
import networkx as nx
import time as tm
import sys

def main():
    """
    Cette fonction est appelée lorsque le programme est exécuté, 
    elle lit les données et essaie de résoudre avec un algorithme choisi par l'utilisateur.
    et il montrera le graph avec les couleurs distribuées en utilisant networkx
    """
    #lit les données du fichier txt et le transformer en liste de tuples
    data = ft.openFileSudoku(sys.argv[2])
    
    #créer le graph sudoku  
    S   = nx.sudoku_graph()  
    ans = 0
    
    #définir la couleur par défaut sur tous les sommet
    for sommet in S.nodes :
        S.nodes[sommet]["color"] = 0


    for i in range(1,10):
        for j in range(1,10):
            if(data[0][0] == i and data[0][1] == j):
                colors.append(color_listes[ data[0][2] ])
                del data[0]
            else :
                colors.append(color_listes[0])

    ft.showGraph(S)

    #menu pour l'utilisateur afin qu'il puisse choisir l'algorithme pour résoudre le problème 
    while ans != "1" and ans != "2":
        print("-- Veuillez choisir l'algorithme pour résoudre ce problème de sudoku --")
        print("1. Glouton")
        print("2. Glouton Naïf")
        ans = input("input : ")

    #enregistrer le temps (début)
    debut   = tm.time()

    #exécuter l'algorithme
    if(ans == "1"):
        ans = "Glouton"
        ft.glouton(S)
    else:
        ans = "Glouton Naïf"
        ft.glouton_naif(S)

    #enregistrer le temps (fin)
    fin     = tm.time()

    #montrer à l'utilisateur les informations concernant l'algorithme, par exemple le temps pris, 
    #le fichier de sortie et le graph
    print("\nL'algorithme est fini vous avez choisi {}".format(ans))
    print("La solution du problème est dans : {}".format(sys.argv[4]))
    print("Les données du problème est dans : {}".format(sys.argv[2]))
    print("Le temps de l'algorithme : {} s".format(round((fin - debut), 10)))
    print("Le graphique sera affiché dans une nouvelle fenêtre")

if __name__ == "__main__":

    #vérifier si les arguments sont corrects ou non
    if(len(sys.argv) != 5):
        print("Veuillez utiliser le bon format d'entrée !")
        print("> python3 sudoku.py -i [data/nom de les données].txt -o [nom de l'output].txt")
        exit()

    main()







    """
    from operator import itemgetter
    data = sorted(openFile(), key=itemgetter(0,1))

    S = nx.empty_graph(81)
    for i in range(9):
        for j in range(1, 9):
            for k in range(j):
                S.add_edge(i*9 + k, i*9 + j)

    for i in range(9):
        for j in range(i, 81, 9):
            for k in range(i, j, 9):
                S.add_edge(k, j)

    for ix in range(3):
        for iy in range(3):
            start = 27 * ix + 3 * iy
            for j in range(1, 9):
                for k in range(j):
                    u = start + (k % 3) + 9 * (k // 3)
                    v = start + (j % 3) + 9 * (j // 3)
                    S.add_edge(u, v)

    colors = []
    for i in range(1,10):
        for j in range(1,10):
            if(data[0][0] == i and data[0][1] == j):
                colors.append(color_listes[ data[0][2] ])
                del data[0]
            else :
                colors.append(color_listes[0])
    """