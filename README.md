# Analyzing the Effect of Different Shortest Path Algorithms on Eccentricty and Centrality Closeness 

## Abstract
_In a few sentences, describe the purpose of the project, the approach, and the results. This should summarize the whole project._

The goal of this project is to see how using different shortest path algorithms affects the eccentricity and centrality closeness of nodes in both weighted and unweighted networks. 

## Motivation 

_In a few sentences, describe the biological problem, and why a computational approach may be useful_

## Methods 

1. Graphs and the computational problem
2. Approaches you used
3. Datasets/Inputs
4. Output Types (a list of predictions? A GraphSpace graph? Etc.)

### BFS

### Dijkstra

### Closeness Centrality 

Write a `calculate_closeness()` function that returns a dictionary of (node,closeness-centrality) pairs.  Closeness centrality <img src="https://render.githubusercontent.com/render/math?math=C(v)"> for a node <img src="https://render.githubusercontent.com/render/math?math=v \in V"> is computed as

<img src="https://render.githubusercontent.com/render/math?math=\Large C(v) = \sum_{u \in V} \frac{1}{\delta_{uv}}">

where <img src="https://render.githubusercontent.com/render/math?math=\delta_{uv}"> is the length of the shortest path from node <img src="https://render.githubusercontent.com/render/math?math=u"> to node <img src="https://render.githubusercontent.com/render/math?math=v">.

:bulb: Note that the distance <img src="https://render.githubusercontent.com/render/math?math=\delta_{vv}=0"> will always be zero (the distance from the source to itself).  You can ignore this case; otherwise you will get a `Divide by Zero` error.

:bulb: In general, if you have a disconnected network, you can ignore any case where <img src="https://render.githubusercontent.com/render/math?math=\delta_{uv}=\infty">. (These networks are connected, so you won't run into this case in HW2).

:hammer: Lab3 will include instructions for calculating the length of the shortest path from one node to all others. In other words, you will have a `shortest_path()` function that will take a node `v` and return a dictionary of (`u`,distance) pairs that contains the shortest path length from `v` to each other node.

### Eccentricity Closeness
Write a `calculate_eccentricity()` function that calculates the Eccentricity centrality. Instead of the sum, take the _maximum_ shortest path from <img src="https://render.githubusercontent.com/render/math?math=v> to any other node <img src="https://render.githubusercontent.com/render/math?math=u \in V>. Note that this corresponds to the _minimum_ reciprocal of this value.:

<img src="https://render.githubusercontent.com/render/math?math=\Large C_{ecc}(v) = \min_{u \in V} \frac{1}{\delta_{uv}}">

where <img src="https://render.githubusercontent.com/render/math?math=\delta_{uv}"> is the length of the shortest path from node <img src="https://render.githubusercontent.com/render/math?math=u"> to node <img src="https://render.githubusercontent.com/render/math?math=v">.

You can resize the nodes in the GraphSpace network according to the eccentricity centrality - be sure to give this graph a different name so your closeness centrality is still in GraphSpace.

## Results

_In one paragraph, summarize your findings_

## Discussion

_In one paragraph, discuss how your findings (or anticipated findings) would fit into the bigger biological problem/question._

## References 

_List of references you used._
