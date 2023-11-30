
tuples = {}
with open("web-Stanford.txt", "r") as file:
    for line in file:
        # Skip comments and empty lines
        if line[0] == "#" or line[0] == "\n":
            continue
        
        # Split line into two int nodes and sort them
        edge = line.split()
        for i in range(len(edge)):
            edge[i] = int(edge[i])
        edge.sort()
        
        edge = tuple(edge)
        
        if edge not in tuples:
            tuples[edge] = 0
        
with open("web-Stanford-noDupes.txt", "w") as file:
    for edge in tuples:
        file.write(str(edge[0]) + " " + str(edge[1]) + "\n")