# A* Algorithm in Python

This repository contains an implementation of the A* Algorithm in Python for finding the shortest path in a weighted graph from a specified source vertex to a destination vertex.

## Overview

The A* Algorithm is a popular pathfinding algorithm used in graph traversal and artificial intelligence. It efficiently finds the shortest path from a source vertex to a destination vertex in a weighted graph, considering both the actual cost from the start vertex and a heuristic estimate to the target.

## How to Use

1. **Inputting the Graph:**
   - Run the Python script `astar.py`.
   - Enter edges for the graph with weights in the format: `'source destination weight'`. Use '#' to stop adding edges.

2. **Specifying Source and Destination:**
   - After entering the graph edges, the program will prompt you to enter the coordinates of the source and destination vertices.
   - Input the source and destination vertices as 'x y' coordinates.

3. **Viewing Results:**
   - The program will display the shortest path from the specified source vertex to the destination vertex, if a path exists.

## Example Usage

```bash
$ python astar.py
Enter edges for the graph with weights (format: 'source destination weight'). Enter '#' to stop:
1 2 4
1 3 1
2 3 2
3 4 5
# (Enter '#' to stop)
Enter the source vertex coordinates (format: 'x y'): 0 0
Enter the destination vertex coordinates (format: 'x y'): 4 4

Shortest path from (0, 0) to (4, 4):
[(0, 0), (1, 3), (3, 4), (4, 4)]
```

## Additional Notes

- The code includes a heuristic function (Euclidean distance) for estimating the remaining distance to the destination.
- Adapt the input and heuristic calculation based on your specific graph and problem domain.
