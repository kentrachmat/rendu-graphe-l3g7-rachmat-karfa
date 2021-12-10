import sys
import networkx as nx
import matplotlib.pyplot as plt
from operator import itemgetter


def openFile():
    data = []
    for line in open('sudoku_data.txt', 'r').readlines():
        try:
            divise1 = line.split("\n")
            divise2 = divise1[0].split(" ")
            data.append( [int(i) for i in divise2])
        except: 
            sys.exit("Format donnee incorrecte !!")
    return data

def createFile(S):
    with open('sudoku_answer.txt', 'w') as f:
        for i in range(1,10):
            for j in range(1,10):
                f.write("{} {} {}\n".format(i,j,0))

def showGraph(S, colors='lightgrey'):
    nx.draw(S, node_size=400 ,with_labels=True, font_weight='bold', node_color=colors)
    plt.show() 

def main():
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
    showGraph(S,colors)
    #createFile(S)

if __name__ == "__main__":
    color_listes = {
        1 : "blue",
        2 : "red",
        3 : "green",
        4 : "orange",
        5 : "yellow",
        6 : "brown",
        7 : "black",
        8 : "pink",
        9 : "purple",
        0 : "grey"
    }
    main()