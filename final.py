## HW2 Visualize Animal Social Networks
## Out: Wednesday Sept 15
## Due: Monday Sept 27
## Lab3 will give you code for calculating shortest paths

#Alex Richter
import hw2_utils as utils
from graphspace_python.api.client import GraphSpace
from graphspace_python.graphs.classes.gsgraph import GSGraph

def main():
    dolphin = read_edge_file('dolphin-files/dolphin-edges.txt')
    make_graph(dolphin)
    return # done with main()

def read_edge_file(file_name):
    #Function from HW1
    #Open the file and read in the data
    with open(file_name, 'r') as data:
        node1 = []
        node2 = []
        for line in data:
            edge = line.split()
            node1.append(edge[0])
            node2.append(edge[1])

    with open('dolphin-files/females.txt') as data:
        females = data.read().splitlines()
    with open('dolphin-files/males.txt') as data:
        males = data.read().splitlines()
    with open('dolphin-files/unknown-sex.txt') as data:
        unknownsex = data.read().splitlines()

    with open('dolphin-files/upside-down-lobtailers.txt') as data:
        udl = data.read().splitlines()
    with open('dolphin-files/side-floppers.txt') as data:
        sf = data.read().splitlines()


    #Create a list of all the nodes in the network
    ls = []
    for i in node1:
        if i not in ls: ls.append(i)

    for i in node2:
        if i not in ls: ls.append(i)

    numberOfNodes = len(ls)

    #Make the data into an adj_list, this list checks both columns because otherwise
    #nodes are not counted. The neihbors become a list and each node is its own
    #dictionary where we include the neighbors, sex, and role of each dolphin.
    adjList = {}
    for i in range(numberOfNodes):
        temp = []
        sex = ''
        role = 'unknown'
        for node in range(len(node1)):
            if node1[node] == ls[i]:
                temp.append(node2[node])
        for node in range(len(node2)):
            if node2[node] == ls[i]:
                temp.append(node1[node])
        if ls[i] in females: sex = 'female'
        if ls[i] in males: sex = 'male'
        if ls[i] in unknownsex: sex = 'unknownsex'
        if ls[i] in udl: role = 'upside down lobtailer'
        if ls[i] in sf: role = 'side flopper'
        adjList[ls[i]] = {'neighbors': temp, 'sex' : sex, 'role': role}

    return adjList

def make_graph(dolphin):
    # Function takes a adjList where it is a dictonary of dictionaries. Each
    # node has a label with the role of the dolphin in the social network, the
    # size of the node is scaled 2 times the closeness proximity of a node, and
    # the color cooresponds to the sex of the dolphin. It also takes in a graph
    # title from the user as a means to bypass the graphspace error of removing
    # a graph from the interface.
    G = GSGraph()
    attemptNum = input("Attempt Number: ") #put in to avoid multiple graph error
    G.set_name('Dolphin '+attemptNum)
    G.set_tags(['HW2']) ## tags help you organize your graphs
    for node in dolphin.keys():
        scaled = calculate_closeness(dolphin, node)*2
        closeness = str(scaled/2)
        role = dolphin[node].get('role')
        sex = dolphin[node].get('sex')
        shapeVar = ''
        colorVar = ''
        if (sex) == 'female': colorVar = 'red'
        if (sex) == 'male': colorVar = 'blue'
        if (sex) == 'unknownsex': colorVar = 'purple'
        if (role) == 'side flopper': shapeVar = 'star'
        if (role) ==  'upside down lobtailer': shapeVar = 'diamond'
        if shapeVar != '':
            G.add_node(node, label=node, popup="Role: "+role+"<br>Closeness: "+closeness+"<br>Sex: "+sex)
            G.add_node_style(node, shape=shapeVar, color=colorVar,height=scaled,width=scaled)
        else:
            G.add_node(node, label=node, popup = "Role: No specific role. <br>Closeness: "+closeness+"<br>Sex: "+sex)
            G.add_node_style(node,color=colorVar,height=scaled,width=scaled)
    for node in dolphin.keys():
        for neighbor in dolphin[node].get('neighbors'):
            G.add_edge(node,neighbor)
            G.add_edge_style(node,neighbor,width=2)
    gs = utils.get_connection()
    utils.post(gs,G,'graph_name')
    return

def calculate_closeness(G, v):
    #Most of the function is the same as the shortest_paths function in lab3, but
    #then avoids dividing by 0 and return a sum rather than a dictionary of distances.
    inf = 10000000000000000
    D = {}
    for node in G.keys():
        if node != v: D[node] = inf
        else: D[node] = 0

    Q = [v] # initialize and populate queue of nodes to explore
    sum = 0
    while len(Q) != 0:
        exploring = Q.pop(0)
        for neighbor in G[exploring].get("neighbors"):
            if D[neighbor] == inf:
                 D[neighbor] = D[exploring] + 1 # update distance to neighbor
                 Q.append(neighbor)

    #Caluculate the closeness but avoid division by 0.
    for dist in D.values():
        if dist != 0: sum += 1 / dist

    return sum

# leave this at the bottom of the file
if __name__ == '__main__':
    main()
