# Analyzing the Effect of Different Shortest Path Algorithms on Eccentricty and Closeness Centrality
## Abstract

The goal of this project is to see how using different shortest path algorithms affects the eccentricity and closeness centrality of nodes in both weighted and unweighted networks. I used the Badger network from HW2 as a baseline, then attempted to prune Hippie. I ran into diffculties calculating eccentricity in Hippie because I could only get subgraphs that were _disconnected components_. 

## Motivation 

Centrality measurements are one useful tool in analyzing networks. We care about centrality measurements because we can see how connected a particular node is in the graph. This is helpful in biological instances because you can understand if a particular node is necessary in the network and can be easily removed without messing with the overall function of the network (i.e. take a highly connected animal out of a food network, there will be an issue). If we can view how different shortest path algorithms effect the outcome of centrality measurements, we can see which nodes are actually more helpful and integral to the overall system. This project wishes to see how shortest path algorithms effect the eccenticity and closness centrality measurements for nodes in a network. 

## Methods 

1. Calculating the eccentricity closeness and the centrality closeness of nodes in a network. 
2. Changing the way in which we calculate shortest paths to account for weights and see differences in connectivity. 
3. Used two different datasets. From HW2, used Badger Dataset as a baseline. Then also implemented over parsed [Hippie Dataset](http://cbdm-01.zdv.uni-mainz.de/~mschaefer/hippie/download.php/ "Database source website for download"). 
4. Output format: Annotated graphspace graphs. Various txt files, titled appropriately. The eccentricity files are ordered largest to smallest value. The closeness files are ordered largest to smallest value as well. 

<table border="0">
 <tr>
    <td><b style="font-size:30px">Badger Files</b></td>
    <td><b style="font-size:30px">Hippie Files</b></td>
 </tr>
 <tr>
    <td> BadgerEccentricityBFS.txt<br /> BadgerEccentricityDijkstraUnweighted.txt<br /> BadgerEccentricityDijkstraWeighted.txt<br />BadgerClosenessBFS.txt<br />BadgerClosenessDijkstraUnweighted.txt<br /> BadgerClosenessDijkstraWeighted.txt <br />
     </td>
    <td>HippieEccentricityBFS.txt<br /> 
    HippieEccentricityDijkstraUnweighted.txt<br /> 
    HippieEccentricityDijkstraWeighted.txt<br /> 
    HippieClosenessBFS.txt<br /> 
    HippieClosenessDijkstraUnweighted.txt<br /> 
    HippieClosenessDijkstraWeighted.txt</td>
 </tr>
</table>

First, I ran the algorithms for BFS and Dijkstras on the Hippie and Badger networks. I then outputted their eccentricity and closeness measurements in separate files. Each network has 6 associated txt files. 
* BFS does not account for weighted edges so we only output two files for the Hippie and Badger networks, respectively. 
* Dijkstra we run the calculations for centrality measures twice, accounting for the weights of an edge and not accounting for edge weights to see how it effects the centrality measures. _We would expect that the weighted measures of Dijkstra are the most accurate measurements of centrality for the network._  

### Breadth First Search

We created a Breadth First Search (BFS) algorithm in Lab3. 
```
Create a queue Q 
Mark v as visited and put v into Q 
While Q is non-empty 
    Remove the head u of Q 
    Mark and enqueue all (unvisited) neighbours of u
```

### Dijkstra

We learned about Dijkstra's algorithm in class. 
```
For each node in the graph: 
  dist[node] = infinity
  
Initialize the dist of source node to 0 
Initialize a Q to be the set of all nodes in the graph 

While Q not empty:
  Select a node A that has the smallest dist
  Remove A from Q
  For each neighbor B of A: 
     If dist[A] + cost(A,B) < dist[B] # where cost(A,B) --> weight of the edge
        dist[B] = dist[A] + cost(A,B)
return dist
    
```

### Centrality Measures

#### Closeness 

The **closeness centrality** of a node is the average length of the shortest path between the node and all other nodes in a network. Closeness centrality <img src="https://render.githubusercontent.com/render/math?math=C(v)"> for a node <img src="https://render.githubusercontent.com/render/math?math=v \in V"> is computed as

<img src="https://render.githubusercontent.com/render/math?math=\Large C(v) = \sum_{u \in V} \frac{1}{\delta_{uv}}">

The node with the highest closeness centrality is the closest to all the other nodes. 

In HW2, we wrote a `calculate_closeness()` function that returns a dictionary of (node,closeness-centrality) pairs.  

#### Eccentricity Closeness

In HW2, it outlines a challenge in which we wite a `calculate_eccentricity()` function that calculates the eccentricity centrality. Instead of the sum, take the _maximum_ shortest path from <img src="https://render.githubusercontent.com/render/math?math=v"> to any other node <img src="https://render.githubusercontent.com/render/math?math=u \in V">. Note that this corresponds to the _minimum_ reciprocal of this value.:

<img src="https://render.githubusercontent.com/render/math?math=\Large C_{ecc}(v) = \min_{u \in V} \frac{1}{\delta_{uv}}">

where <img src="https://render.githubusercontent.com/render/math?math=\delta_{uv}"> is the length of the shortest path from node <img src="https://render.githubusercontent.com/render/math?math=u"> to node <img src="https://render.githubusercontent.com/render/math?math=v">.

If a node has a higher eccentricity value, it means that the node is relatively close to every node in the graph. If the node has a smaller ecccentricity value that means that the node we are calculating the eccentricity value has at least one node in which it is not closely connected to. 

### Datasets 

#### Badger

The [badger social network](https://www.sciencedirect.com/science/article/pii/S0960982213011238?via%3Dihub) is stored as two files in the `badger-files/` directory:

- `badger-files/badger-edges.txt`: file of edges as `node1 node2 edge_weight`, where you can ignore the third column (note that if `A B` is a line, then `B A` is _not_ in the file).
- `badger-files/badger-info.txt`: file of four tab-delimited columns: `badger name`, `sex`, `infection status`, and `social group`.  The badger name is the same as the node name in the edges file.  This file also has a header.

#### Hippie 

The [Hippie Dataset](http://cbdm-01.zdv.uni-mainz.de/~mschaefer/hippie/download.php/ "Database source website for download") is one massive edge list file with various columns. 

The columns are: `node1`, `node1 id`, `node2`, `node2 id`, `weight`, and `notes` 

I parsed the network using high confidence, so only edges with weights over .8. I also decided not to include self loops in the network as that would effect the centrality measurements. 

## Results

BFS and unweighted Dijkstra returned the same graphs and outputed the same closeness and eccentricity scores. Weighted Dijkstra performed the best, which was to be expected because it took in more information to do so. Hippie was difficult to use because it was hard to get connected components and trying to size down a giant network. The subgraph of Hippie I ended up using had disconnected nodes and therefore, led to incorrect eccentricity scores. 

### Badger Network Analysis
Included are the respective graphs for running the various iterations of the algorithms. 

**Badger Closeness calculated using BFS:** The size varies with the closeness score as it is calculated by _multiplying_ a constant by the closeness value of that node, as closeness values are bigger than 1. The nodes that are colored yellow are the default color. Those that are colored orange have a higher closeness score (i.e. score greater than 25). If you want the respective score for each node, please check [the correct txt file](https://github.com/ajrichter7/finalProject/blob/main/BadgerClosenessBFS.txt). 
![Badger Closeness BFS](https://github.com/ajrichter7/finalProject/blob/main/images/badgerclosenessbfs.png) 

**Badger Eccentricity calculated using BFS:** The size varies with the eccentricity score as it is calulated by _dividing_ a constant by the eccentricity value of that node, as eccentricity values are less than 1. If you want the respective score for each node, please check [the correct txt file](https://github.com/ajrichter7/finalProject/blob/main/BadgerEccentricityBFS.txt). 
![Badger Eccentricity BFS](https://github.com/ajrichter7/finalProject/blob/main/images/badgereccentricitybfs.png) 

**Badger Closeness and Eccentricity calculated using Dijkstra's (Unweighted):** I then ran Dijkstra's on the badger networks but using the unweighted adjacency list of edges. This simply meant that I gave each edge a weight of 1. When I ran it, it produced the same exact closeness and eccentricity scores as the BFS. This is not surprising as Dijkstra's without different weights is essentially BFS. This can be confirmed in the graphs and files that I uploaded to the repo. 
* [Closeness txt using Dijkstra's Unweighted](https://github.com/ajrichter7/finalProject/blob/main/BadgerClosenessDijkstraUnweighted.txt) =  [Closeness txt using BFS](https://github.com/ajrichter7/finalProject/blob/main/BadgerClosenessBFS.txt)
* [Eccentricity txt using Dijkstra's Unweighted](https://github.com/ajrichter7/finalProject/blob/main/BadgerEccentricityDijkstraUnweighted.txt) = [Eccentricty txt using BFS](https://github.com/ajrichter7/finalProject/blob/main/BadgerEccentricityBFS.txt)

**Badger Closeness calculated using Dijkstra's (Weighted):** The size varies with the closeness score as it is calculated by _multiplying_ a constant by the closeness value of that node, as closeness values are bigger than 1. The nodes that are colored yellow are the default color. Unlike the graph from using BFS or unweighted Dijkstra's, there are no nodes with a closeness score greater than 25. If you want the respective score for each node, please check [the correct txt file](https://github.com/ajrichter7/finalProject/blob/main/BadgerClosenessDijkstraWeighted.txt). 
![Badger Closeness Dijkstra Weighted](https://github.com/ajrichter7/finalProject/blob/main/images/badgerclosedijW.png)

**Badger Eccentricity calculated using Dijkstra's (Weighted):** The size varies with the eccentricity score as it is calulated by _dividing_ a constant by the eccentricity value of that node, as eccentricity values are less than 1. This is noticeably different than using unweighted Dijkstra's or BFS. The file produced shows a large variation in eccentricity scores. If you were to look at the respective eccentricity scores of the nodes when using BFS/unweighted Dijkstra's, you would see a lot of repetition in the eccentricity scores. If you want the respective score for each node, please check [the correct txt file](https://github.com/ajrichter7/finalProject/blob/main/BadgerEccentricityDijkstraWeighted.txt). 
![Badger Eccentricity Dijkstra Weighted](https://github.com/ajrichter7/finalProject/blob/main/images/badgereccentricitydijW.png)

### Hippie Network Analysis

Hippie is a massive network of tens of thousands of nodes and edges. So I attempted to scale it. I inserted constants in the code that can be easily changed, so if you wish to test the algorithms on a larger graph one can easily do so. I trim down the Hippie network that I run the algorithms on to get a smaller network by:
1. Edge weight: when reading in the Hippie file, I only care about adding an edge from the network if the edge has a weight of over .95. I chose this score because there are still 1763 edges and 1510 nodes in the network... this was still too large for graphspace to load properly...
2. Pruning the adjList 
```
Function that will take in the adjList, edgeList, nodeList
Removes entries in adjList that have less than 10 connections
Removes entry from nodeList
Removes any edge that had that entry as an endpoint from the edgeList

Returns updated adjList, edgeList, nodeList
```
**Hippie Closeness calculated using BFS:** The size varies with the closeness score as it is calculated by _multiplying_ a constant by the closeness value of that node, as closeness values are bigger than 1. The nodes that are colored yellow are the default color. Those that are colored orange have a higher closeness score (i.e. score greater than 25). If you want the respective score for each node, please check [the correct txt file](https://github.com/ajrichter7/finalProject/blob/main/HippieClosenessBFS.txt). 
![Hippie Closeness BFS](https://github.com/ajrichter7/finalProject/blob/main/images/hippieclosebfs.png) 

**Hippie Eccentricity calculated using BFS:** Originally, I sought to vary the node size with the eccentricity score as it is calulated by _dividing_ a constant by the eccentricity value of that node, as eccentricity values are less than 1. This was **not** successful because it is a disconnected component when I take part of the Hippie network. If you want the respective score for each node, please check [the correct txt file](https://github.com/ajrichter7/finalProject/blob/main/HippieEccentricityBFS.txt). 
![Hippie Eccentricity BFS](https://github.com/ajrichter7/finalProject/blob/main/images/hippieeccentdijUW.png) 

**Hippie Closeness and Eccentricity calculated using Dijkstra's (Unweighted):** I then ran Dijkstra's on the hippie network but using the unweighted adjacency list of edges. This simply meant that I gave each edge a weight of 1. When I ran it, it produced the same exact closeness and eccentricity scores as the BFS. This is not surprising as Dijkstra's without different weights is essentially BFS. This can be confirmed in the graphs and files that I uploaded to the repo. It should be noted that regardless of any algorithm, all of the times ran on Hippie because it is disconnected component, the eccentricity scores are all the same. _Because all of the eccentricity scores are the same, I only included the graphspace graph for the eccentricity scores of Hippie created then._
* [Closeness txt using Dijkstra's Unweighted](https://github.com/ajrichter7/finalProject/blob/main/HippieClosenessDijkstraUnweighted.txt) =  [Closeness txt using BFS](https://github.com/ajrichter7/finalProject/blob/main/HippieClosenessBFS.txt)
* [Eccentricity txt using Dijkstra's Unweighted](https://github.com/ajrichter7/finalProject/blob/main/HippieEccentricityDijkstraUnweighted.txt) = [Eccentricty txt using BFS](https://github.com/ajrichter7/finalProject/blob/main/HippieEccentricityBFS.txt)

**Hippie Closeness calculated using Dijkstra's (Weighted):** The size varies with the closeness score as it is calculated by _multiplying_ a constant by the closeness value of that node, as closeness values are bigger than 1. The nodes that are colored yellow are the default color. Unlike the graph from using BFS or unweighted Dijkstra's, there are no nodes with a closeness score greater than 25. If you want the respective score for each node, please check [the correct txt file](https://github.com/ajrichter7/finalProject/blob/main/HippieClosenessDijkstraWeighted.txt). 
![Hippie Closeness Dijkstra Weighted](https://github.com/ajrichter7/finalProject/blob/main/images/hippieclosedijWeighted.png)

**Hippie Eccentricity calculated using Dijkstra's (Weighted):** See note above on eccentricity difficulties. If you want the respective score for each node, please check [the correct txt file](https://github.com/ajrichter7/finalProject/blob/main/HippieEccentricityDijkstraWeighted.txt). 

## Discussion

This work is necessary because it can show important measurements. It is important to know the closeness and eccentricity measurements of a node because it shows how important a node is to the entire system.

### Future Work on Eccentricity

The importance of this work ties into my issues with eccentricity. Due to the fact that every node in Hippie had the same eccentricity score means that I chose a disconnected component. I attempted to write a function that would remove the disconnected nodes in the network and recalculated the eccentricity scores. This code is commented out in `final.py`. If every node in the network has the same eccentricity score, that means there exists a node in the network that is not connected. This is important because it can help us discover connected components within a graph. 

## References 

* Slides from class. 
* BFS: https://www.studytonight.com/post/breadth-first-search-or-bfs-for-a-graph

