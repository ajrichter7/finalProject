# Analyzing the Effect of Different Shortest Path Algorithms on Eccentricty and Closeness Centrality
## Abstract
_In a few sentences, describe the purpose of the project, the approach, and the results. This should summarize the whole project._

The goal of this project is to see how using different shortest path algorithms affects the eccentricity and closeness centrality of nodes in both weighted and unweighted networks. 

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

_In one paragraph, summarize your findings_

### Badger Network Analysis

### Hippie Network Analysis

## Discussion

_In one paragraph, discuss how your findings (or anticipated findings) would fit into the bigger biological problem/question._

## References 

* Slides from class. 
* BFS: https://www.studytonight.com/post/breadth-first-search-or-bfs-for-a-graph

