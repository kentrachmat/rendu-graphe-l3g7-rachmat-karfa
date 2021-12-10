import sys
import networkx as nx
import matplotlib.pyplot as plt


def openFile():
    data = []
    for line in open('carte_data.txt', 'r').readlines():
        try:
            divise1 = line.split("\n")
            divise2 = divise1[0].split(" ")
            data.append((divise2[0],divise2[1]))
        except: 
            sys.exit("Format donnee incorrecte !!")
    return data

def createFile(S):
    with open('carte_answer.txt', 'w') as f:
        for i in S.nodes():
            f.write("{} {}\n".format(i,0))

def showGraph(S, colors='lightgrey'):
    nx.draw(S, node_size=800 ,with_labels=True, font_weight='bold', node_color=colors)
    plt.show() 

def main():
    data = openFile()
    counter = 0
    S = nx.Graph(data)
    for i,name in enumerate(S.nodes()):
        for j in S.nodes():
            if(not(name in S.neighbors(j)) and name != j):
                counter  = 1
                break
        if(counter  == 1):
            colors.append(color_listes[i])
            counter = 0
        else:
            colors.append("black")
            
    showGraph(S,colors)
    #createFile(S)

if __name__ == "__main__":
    colors = []
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