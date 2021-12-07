## Used a lot of the functions from hw2

#Alex Richter
import hw2_utils as utils
from graphspace_python.api.client import GraphSpace
from graphspace_python.graphs.classes.gsgraph import GSGraph

def main():
    badgerEdgeList, badgerAdjList, badgerAdjListUnweighted, badgerNodeList = read_badger('badger-files/badger-edges.txt')
    # badgerAdjList = read_adjlist('badger-files/badger-edges.txt', 1)
    # badgerCloseDict, badgerEccentDict = calculate(badgerAdjList)
    # outputFiles('BadgerEccentricityBFS.txt', badgerEccentDict)
    # outputtoGraph(badgerNodeList, badgerEdgeList, badgerAdjList, 'badgerEccentricityBFS', 'eccentricity', badgerEccentDict)
    # outputFiles('BadgerClosenessBFS.txt', badgerCloseDict)
    # outputtoGraph(badgerNodeList, badgerEdgeList, badgerAdjList, 'badgerClosenessBFS', 'closeness', badgerCloseDict)

    badgerCloseDictW, badgerEccentDictW = calculateDijkstra(badgerAdjList)
    outputFiles('BadgerEccentricityDijkstraWeighted.txt', badgerEccentDictW)
    outputtoGraph(badgerNodeList, badgerEdgeList, 'BadgerEccentricityDijkstraWeighted', 'eccentricity', badgerEccentDictW)
    outputFiles('BadgerClosenessDijkstraWeighted.txt', badgerCloseDictW)
    outputtoGraph(badgerNodeList, badgerEdgeList,'BadgerClosenessDijkstraWeighted', 'closeness', badgerCloseDictW)

    badgerCloseDictUW, badgerEccentDictUW = calculateDijkstra(badgerAdjListUnweighted)
    outputFiles('BadgerEccentricityDijkstraUnweighted.txt', badgerEccentDictUW)
    outputtoGraph(badgerNodeList, badgerEdgeList, 'BadgerEccentricityDijkstraUnweighted', 'eccentricity', badgerEccentDictUW)
    outputFiles('BadgerClosenessDijkstraUnweighted.txt', badgerCloseDictUW)
    outputtoGraph(badgerNodeList, badgerEdgeList, 'BadgerClosenessDijkstraUnweighted', 'closeness', badgerCloseDictUW)

    # hippieEdgeList, hippieAdjList, hippieNodeList = read_hippie('hippie_current.txt')
    # print(hippieAdjList)
    # hippieAdjList = read_adjlist('hippie_current.txt', 2)
    # hippieCloseDict, hippieEccentDict = calculate(hippieAdjList)
    # outputFiles('HippieEccentricityBFS.txt', hippieEccentDict)
    # outputFiles('HippieClosenessBFS.txt', hippieCloseDict)

    # outputFiles('HippieEccentricityDijkstraUnweighted.txt', hippieEccentDijDict)
    # outputFiles('HippieEccentricityDijkstraWeighted.txt', hippieEccentDictW)
    # outputFiles('HippieClosenessDijkstraUnweighted.txt', hippieCloseDijDict)
    # outputFiles('HippieClosenessDijkstraWeighted.txt', hippieCloseDictW)

    # hippie = pruneGraph(hippieAdjList, hippieEdgeList, hippieNodeList)
    # output(badgerNodeList, badgerEdgeList, 'badger')
    # output(hippieNodeList, hippieEdgeList, 'hippie')
    return # done with main()

def outputFiles(filename, d):
    f = open(filename, "w")
    sortDict = dict(list(reversed(sorted(d.items(), key=lambda item: item[1]))))

    for key, value in sortDict.items():
        f.write(str(key)+ '     '+ str(value)+'\n')

    f.close()
    return
## Function taken from lab2utils.py
## read undirected edge list into adjacency list.
## adjlist is a DICTIONARY, which can be accessed like A[v].
def read_adjlist(infile:str, x) -> dict:
    adjlist = {}
    with open(infile) as fin:
        for line in fin:
            edge = line.strip().split()
            if edge[0] not in adjlist:
                adjlist[edge[0]] = set()
            if edge[x] not in adjlist:
                adjlist[edge[x]] = set()
            adjlist[edge[0]].add(edge[x])
            adjlist[edge[x]].add(edge[0])
    return adjlist

def read_badger(file_name):
    #Function from HW1
    #Open the file and read in the data
    #node1, node2, weight

    #returns a edgelist which is a dictionary where the key is the tuple/edge and the value is the weight
    #returns a nodelist of all the nodes in the graph
    with open(file_name, 'r') as data:
        edgelist = {}
        adjList = {}
        adjListUnweighted = {}
        node1 = []
        node2 = []
        for line in data:
            edge = line.split()
            node1.append(edge[0])
            node2.append(edge[1])
            edgelist[(edge[0], edge[1])] = float(edge[2])
            if edge[0] not in adjList:
                adjList[edge[0]] = {}
                adjListUnweighted[edge[0]] = {}
            adjList[edge[0]][edge[1]] = float(edge[2])
            adjListUnweighted[edge[0]][edge[1]] = 1
            if edge[1] not in adjList:
                adjList[edge[1]] = {}
                adjListUnweighted[edge[1]] = {}
            adjList[edge[1]][edge[0]] = float(edge[2])
            adjListUnweighted[edge[1]][edge[0]] = 1
    #Create a list of all the nodes in the network
    nodelist = []
    for i in node1:
        if i not in nodelist: nodelist.append(i)

    for i in node2:
        if i not in nodelist: nodelist.append(i)

    return edgelist, adjList, adjListUnweighted, nodelist

def read_hippie(file_name):
    #Function similar to read_badger except we change the input for delimiters
    #Use node1 name and not node1 id <-- might change later
    #Open the file and read in the data
    #node1, node1 id, node2, node2 id, weight, info

    #returns a edgelist which is a dictionary where the key is the tuple/edge and the value is the weight
    #note: we ignore edges that do not have a large weight do to the size of the graph
    #returns a nodelist of all the nodes that have edges in the graph
    with open(file_name, 'r') as data:
        edgelist = {}
        node1 = []
        node2 = []
        adjList = {}
        for line in data:
            edge = line.split()
            try:
                if edge[0] != edge[2] and float(edge[4]) >= .95:
                    node1.append(edge[0])
                    node2.append(edge[2])
                    edgelist[(edge[0], edge[2])] = float(edge[4])
                    if edge[0] not in adjList:
                        adjList[edge[0]] = {}
                    adjList[edge[0]][edge[2]] = float(edge[4])
                    if edge[2] not in adjList:
                        adjList[edge[2]] = {}
                    adjList[edge[2]][edge[0]] = float(edge[4])
            except: pass

    #Create a list of all the nodes in the network
    nodelist = []
    for i in node1:
        if i not in nodelist: nodelist.append(i)

    for i in node2:
        if i not in nodelist: nodelist.append(i)

    return edgelist, adjList, nodelist

def outputtoGraph(nodelist, edgeList, title, type, d):
    G = GSGraph()
    attemptNum = input("Attempt Number: ") #put in to avoid multiple graph error
    G.set_name(title+attemptNum)
    G.set_tags(['finalProject']) ## tags help you organize your graphs
    if type == 'eccentricity':
        for node in nodelist:
            G.add_node(node, label=node)
            c = 'yellow'
            if d[node] > .5: c = 'blue'
            if d[node] > .25: c = 'purple'
            if d[node] > .05: c = 'red'
            if d[node] > .0025: c = 'orange'
            G.add_node_style(node,color = c, height=10 / d[node],width=10 / d[node])
        for edge in edgeList.keys():
            G.add_edge(edge[0],edge[1])
    if type == 'closeness':
        for node in nodelist:
            G.add_node(node, label=node)
            c = 'yellow'
            if d[node] > 25: c = 'orange'
            if d[node] > 50: c = 'red'
            if d[node] > 100: c = 'purple'
            if d[node] > 1000: c = 'blue'
            if d[node] > 5000: c = 'green'
            G.add_node_style(node, color = c, height=10 * d[node],width=10 * d[node])
        for edge in edgeList.keys():
            G.add_edge(edge[0],edge[1])
    gs = utils.get_connection()
    utils.post(gs,G,'graph_name')
    return

def outputEdgelist(nodelist, edgelist, title, type, d):
    G = GSGraph()
    attemptNum = input("Attempt Number: ") #put in to avoid multiple graph error
    G.set_name(title+attemptNum)
    G.set_tags(['finalProject']) ## tags help you organize your graphs
    if type == 'eccentricity':
        for node in nodelist:
            G.add_node(node, label=node)
            G.add_node_style(node,height=10 / d[node],width=10 / d[node])
        for edge in edgelist.keys():
            G.add_edge(edge[0],edge[1])
    if type == 'closeness':
        for node in nodelist:
            G.add_node(node, label=node)
            G.add_node_style(node,height=5* d[node],width=5 * d[node])
        for edge in edgelist.keys():
            G.add_edge(edge[0],edge[1])
    gs = utils.get_connection()
    utils.post(gs,G,'graph_name')
    return

def calculate(adjList):
    closeDict = {}
    eccentDict = {}
    for node in adjList.keys():
        closeness, eccentricity = ClosenessAndEccentricityBFS(adjList, node)
        closeDict[node] = closeness
        eccentDict[node] = eccentricity

    return closeDict, eccentDict

def ClosenessAndEccentricityBFS(adjList, input):
    #Most of the function is the same as the shortest_paths function in lab3, but
    #then avoids dividing by 0 and return a sum rather than a dictionary of distances.

    #For hippie, we want to calculate the centrality measures and if they high enough
    #we want to include those nodes in the graph, ow ignore. even with .9 confidence
    #still have around 1500 nodes. we don't want that many nodes.
    inf = 10000000000000000
    D = {}
    D[input] = 0
    for node in adjList.keys():
        if node != input: D[node] = inf

    Q = [input] # initialize and populate queue of nodes to explore
    closeness = 0
    while len(Q) != 0:
        exploring = Q.pop(0)
        for neighbor in adjList[exploring]:
            if D[neighbor] == inf:
                 D[neighbor] = D[exploring] + 1 # update distance to neighbor
                 Q.append(neighbor)

    #Calculate the closeness but avoid division by 0.
    for dist in D.values():
        if dist != 0: closeness += 1 / dist

    maxPathNode = max(D, key=D.get)

    eccentricity = 1 / float(D[maxPathNode])
    return closeness, eccentricity

def getKey(value, dict):
    for key, val in dict.items():
        if val == value:
            return key

def calculateDijkstra(adjList):
    closeDict = {}
    eccentDict = {}
    for node in adjList.keys():
        c, e = dijkstra(adjList, node)
        closeDict[node] = c
        eccentDict[node] = e

    return closeDict, eccentDict

def dijkstra(adjList, input):
    inf = 10000000000000000
    D = {}
    D[input] = 0
    unvisited = []
    for node in adjList.keys():
        unvisited.append(node)
        if node != input:
            D[node] = inf

    closeness = 0
    while len(unvisited) != 0:
        curNode = min(unvisited, key=lambda node:D[node]) #will get the key for smallest value
        unvisited.remove(curNode)
        if D[curNode] == inf:
            #edge case of disconnected network
            break
        for neighbor, cost in adjList[curNode].items():
            if D[curNode] + cost <= D[neighbor] and D[curNode] + cost > 0:
                D[neighbor] = D[curNode] + cost
    #Calculate the closeness but avoid division by 0.

    for dist in D.values():
        if dist != inf and dist != 0: closeness += 1 / dist

    maxPathNode = max(D, key=D.get)

    eccentricity = 1 / float(D[maxPathNode])
    return closeness, eccentricity

def pruneGraph(adjList, edgeList, nodeList):
    return
# leave this at the bottom of the file
if __name__ == '__main__':
    main()
