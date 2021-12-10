def glouton(S):
    all_color = []
    color_count = 0
    
    for i in S.nodes():
        all_color.append(color_count)
        color_count += 1
    
    for sommet in G.nodes():
        color_present = []
        
        for color in sommet.neighbours:
            color_present.append(color)
        
        for i in color_present:
            all_color.remove(i) 
        sommet['color'] = all_color[0]

        for i in color_present:
            all_color.append(i)