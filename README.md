# Analyzing the Effect of Different Shortest Path Algorithms on Eccentricty and Closeness Centrality
## Abstract
_In a few sentences, describe the purpose of the project, the approach, and the results. This should summarize the whole project._

The goal of this project is to see how using different shortest path algorithms affects the eccentricity and closeness centrality of nodes in both weighted and unweighted networks. 

## Motivation 

_In a few sentences, describe the biological problem, and why a computational approach may be useful_

## Methods 

1. Calculating the eccentricity closeness and the centrality closeness of nodes in a network 
2. Approaches you used
3. Datasets/Inputs
4. Output Types (a list of predictions? A GraphSpace graph? Etc.)

### Breadth First Search

We created a Breadth First Search (BFS) algorithm in Lab3. 
```
Create a queue Q 
Mark v as visited and put v into Q 
While Q is non-empty 
    Eemove the head u of Q 
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

## Results

_In one paragraph, summarize your findings_

## Discussion

_In one paragraph, discuss how your findings (or anticipated findings) would fit into the bigger biological problem/question._

## References 

Slides from class.
BFS: https://www.studytonight.com/post/breadth-first-search-or-bfs-for-a-graph

