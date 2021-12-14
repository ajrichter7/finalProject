## Used a lot of the functions from hw2

#Alex Richter
import hw2_utils as utils
from graphspace_python.api.client import GraphSpace
from graphspace_python.graphs.classes.gsgraph import GSGraph

def main():
    # badgerEdgeList, badgerAdjList, badgerNodeList = read_badger('badger-files/badger-edges.txt')
    # print('len edgeList = ', len(badgerEdgeList))
    # print('len adjList = ', len(badgerAdjList))
    # print('len nodelist =', len(badgerNodeList))
    # badgerEdgeList, badgerAdjList, badgerNodeList = pruneGraph(badgerEdgeList, badgerAdjList, badgerNodeList)
    # badgerCloseDict, badgerEccentDict = calculate(badgerAdjList)
    # outputFiles('BadgerEccentricityBFS.txt', badgerEccentDict)
    # outputtoGraph(badgerNodeList, badgerEdgeList, 'badgerEccentricityBFS', 'eccentricity', badgerEccentDict)
    # outputFiles('BadgerClosenessBFS.txt', badgerCloseDict)
    # outputtoGraph(badgerNodeList, badgerEdgeList,'badgerClosenessBFS', 'closeness', badgerCloseDict)

    # badgerCloseDictW, badgerEccentDictW = calculateDijkstra(badgerAdjList)
    # outputFiles('BadgerEccentricityDijkstraWeighted.txt', badgerEccentDictW)
    # outputtoGraph(badgerNodeList, badgerEdgeList, 'BadgerEccentricityDijkstraWeighted', 'eccentricity', badgerEccentDictW)
    # outputFiles('BadgerClosenessDijkstraWeighted.txt', badgerCloseDictW)
    # outputtoGraph(badgerNodeList, badgerEdgeList,'BadgerClosenessDijkstraWeighted', 'closeness', badgerCloseDictW)
    #
    # badgerCloseDictUW, badgerEccentDictUW = calculateDijkstra(badgerAdjList, 'unweighted')
    # outputFiles('BadgerEccentricityDijkstraUnweighted.txt', badgerEccentDictUW)
    # outputtoGraph(badgerNodeList, badgerEdgeList, 'BadgerEccentricityDijkstraUnweighted', 'eccentricity', badgerEccentDictUW)
    # outputFiles('BadgerClosenessDijkstraUnweighted.txt', badgerCloseDictUW)
    # outputtoGraph(badgerNodeList, badgerEdgeList, 'BadgerClosenessDijkstraUnweighted', 'closeness', badgerCloseDictUW)

    hippieEdgeList, hippieAdjList, hippieNodeList = read_hippie('hippie_current.txt')
    # print('len edgeList = ', len(hippieEdgeList))
    # print('len adjList = ', len(hippieAdjList))
    # print('len nodelist =', len(hippieNodeList))
    hippieEdgeList, hippieAdjList, hippieNodeList = pruneGraph(hippieEdgeList, hippieAdjList, hippieNodeList)
    # print('len edgeList = ', len(hippieEdgeList))
    # print('len adjList = ', len(hippieAdjList))
    # print('len nodelist =', len(hippieNodeList))
    hippieCloseDict, hippieEccentDict = calculate(hippieAdjList)
    # hippieEdgeList, hippieAdjList, hippieNodeList = fixdisconnectedcomp(hippieEdgeList, hippieAdjList, hippieNodeList, hippieCloseDict)
    # hippieCloseDict, hippieEccentDict = calculate(hippieAdjList)
    outputFiles('HippieEccentricityBFS.txt', hippieEccentDict)
    outputtoGraph(hippieNodeList, hippieEdgeList, 'HippieEccentricityBFS', 'eccentricity', hippieEccentDict)
    outputFiles('HippieClosenessBFS.txt', hippieCloseDict)
    outputtoGraph(hippieNodeList, hippieEdgeList,'HippieClosenessBFS', 'closeness', hippieCloseDict)

    hippieCloseDictW, hippieEccentDictW = calculateDijkstra(hippieAdjList, 'weighted')
    outputFiles('HippieEccentricityDijkstraWeighted.txt', hippieEccentDictW)
    outputtoGraph(hippieNodeList, hippieEdgeList, 'HippieEccentricityDijkstraWeighted', 'eccentricity', hippieEccentDictW)
    outputFiles('HippieClosenessDijkstraWeighted.txt', hippieCloseDictW)
    outputtoGraph(hippieNodeList, hippieEdgeList,'HippieClosenessDijkstraWeighted', 'closeness', hippieCloseDictW)

    hippieCloseDictUW, hippieEccentDictUW = calculateDijkstra(hippieAdjList, 'unweighted')
    outputFiles('HippieEccentricityDijkstraUnweighted.txt', hippieEccentDictUW)
    outputtoGraph(hippieNodeList, hippieEdgeList, 'HippieEccentricityDijkstraUnweighted', 'eccentricity', hippieEccentDictUW)
    outputFiles('HippieClosenessDijkstraUnweighted.txt', hippieCloseDictUW)
    outputtoGraph(hippieNodeList, hippieEdgeList, 'HippieClosenessDijkstraUnweighted', 'closeness', hippieCloseDictUW)

    return # done with main()

def outputFiles(filename, d):
    f = open(filename, "w")
    sortDict = dict(list(reversed(sorted(d.items(), key=lambda item: item[1]))))

    for key, value in sortDict.items():
        f.write(str(key)+ '     '+ str(value)+'\n')

    f.close()
    return

def read_badger(file_name):
    #Function from HW1
    #Open the file and read in the data
    #node1, node2, weight

    #returns a edgelist which is a dictionary where the key is the tuple/edge and the value is the weight
    #returns a nodelist of all the nodes in the graph
    #returns an adjList where it accounts for the edgeweight (dictionary of dictionaries)
    with open(file_name, 'r') as data:
        edgelist = {}
        adjList = {}
        node1 = []
        node2 = []
        for line in data:
            edge = line.split()
            node1.append(edge[0])
            node2.append(edge[1])
            edgelist[(edge[0], edge[1])] = float(edge[2])
            if edge[0] not in adjList:
                adjList[edge[0]] = {}
            adjList[edge[0]][edge[1]] = float(edge[2])
            if edge[1] not in adjList:
                adjList[edge[1]] = {}
            adjList[edge[1]][edge[0]] = float(edge[2])

    #Create a list of all the nodes in the network
    nodelist = []
    for i in node1:
        if i not in nodelist: nodelist.append(i)

    for i in node2:
        if i not in nodelist: nodelist.append(i)

    return edgelist, adjList, nodelist

def read_hippie(file_name):
    #Function similar to read_badger except we change the input for delimiters
    #Use node1 name and not node1 id <-- might change later
    #Open the file and read in the data
    #node1, node1 id, node2, node2 id, weight, info

    #returns a edgelist which is a dictionary where the key is the tuple/edge and the value is the weight
    #note: we ignore edges that do not have a large weight do to the size of the graph, higher than .95
    #returns a nodelist of all the nodes that have edges in the graph
    #returns an adjList that is a dictionary of dictionaries and accounts for edgeweights
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
            if d[node] < 1e-5:
                # had to add this condition because otherwise the nodes would not appear! do to it being a disconnected component
                # we calculate eccentricity and divide by "inf" so eccentricity values very small.
                G.add_node_style(node,color = c, height=20, width=20)
            else:
                G.add_node_style(node,color = c, height=10 / d[node],width=10 / d[node])
        for edge in edgeList:
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
            #changes the color of the nodes based on the closeness value for the node
            G.add_node_style(node, color = c, height=10 * d[node],width=10 * d[node])
        for edge in edgeList:
            G.add_edge(edge[0],edge[1])
    gs = utils.get_connection()
    utils.post(gs,G,'graph_name')
    return

#Attempted to function to figure out if connected component by taking in the edge list,
#adjlist, nodels, and closeDictionary. It was supposed to remove edges if it was not close to any other nodes
# def fixdisconnectedcomp(edge, adj, nodels, closeDict):
#     templs = []
#     print(closeDict)
#     for node, value in closeDict.items():
#         if value == float(0):
#             templs.append(node)
#             # for k in adj[node].keys():
#             #     del adj[k][node]
#             #     edge = [x for x in edge if x!= (k, node) and x!= (node, k)]
#             # nodels.remove(node)
#             # del adj[node]
#     print(templs)
#     return edge, adj, nodels

def calculate(adjList):
    #calls function to create dictionary of closeness and eccentricity values for each node in the graph
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

def calculateDijkstra(adjList, weighting):
    #Calculating closeness and eccentricity dictionaries in which we calculate score for
    #each node in the graph. uses dijkstra's
    closeDict = {}
    eccentDict = {}
    # disconnectednodes = set()
    for node in adjList.keys():
        c, e = dijkstra(adjList, node, weighting)
        # disconnectednodes.update(ls)
        closeDict[node] = c
        eccentDict[node] = e
    return closeDict, eccentDict

def dijkstra(adjList, input, weighting):
    #implementation of dijkstra
    inf = 10000000000000000
    D = {}
    D[input] = 0
    unvisited = []
    for node in adjList.keys():
        unvisited.append(node)
        if node != input:
            D[node] = inf

    closeness = 0
    if weighting == 'weighted':
        while len(unvisited) != 0:
            curNode = min(unvisited, key=lambda node:D[node]) #will get the key for smallest value
            unvisited.remove(curNode)
            if D[curNode] == inf:
                #edge case of disconnected network
                break
            for neighbor, cost in adjList[curNode].items():
                if D[curNode] + cost <= D[neighbor] and D[curNode] + cost > 0:
                    D[neighbor] = D[curNode] + cost

    if weighting == 'unweighted':
        while len(unvisited) != 0:
            curNode = min(unvisited, key=lambda node:D[node]) #will get the key for smallest value
            unvisited.remove(curNode)
            if D[curNode] == inf:
                #edge case of disconnected network
                break
            for neighbor, cost in adjList[curNode].items():
                if D[curNode] + 1 <= D[neighbor] and D[curNode] + 1 > 0:
                    D[neighbor] = D[curNode] + 1

    #Calculate the closeness but avoid division by 0.
    for dist in D.values():
        if dist != 0: closeness += 1 / dist

    maxPathNode = max(D, key=D.get)

    eccentricity = 1 / float(D[maxPathNode])
    return closeness, eccentricity


def pruneGraph(edgeList, adjList, nodeList):
    #helper function to make the graph (hippe) smaller so less nodes to graph
    #if a node is connected to less than 5 nodes, then we will remove the node
    #this means we expect it not to be an important node because it has few connections
    newadjList = adjList.copy()
    for key in adjList.keys():
        if len(adjList[key]) < 5:
            for k2 in adjList[key].keys():
                del newadjList[k2][key]
                edgeList = [x for x in edgeList if x!= (k2, key) and x!= (key, k2)]
            nodeList.remove(key)
            del newadjList[key]

    return edgeList, newadjList, nodeList
# leave this at the bottom of the file
if __name__ == '__main__':
    main()
