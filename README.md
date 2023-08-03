# Maze Traversal using Depth-First Traversal

<img width="268" alt="DFS_LeetCode" src="https://github.com/girik21/MazeTraversal/assets/87162191/200cd5ee-6933-4c66-a704-84813cadd14b">

## Presentation Link
https://docs.google.com/presentation/d/135g4dm39EbHHAFCM-BvidKKgEbnW31rUAgkkjTC1ars/edit?usp=sharing

## Abstract
- Efficiently traverse mazes using the Depth-First Search (DFS) algorithm.
- Implement a concise and elegant DFS solution for maze navigation.
- Explore diverse maze configurations and assess DFS performance.
- Successfully traverse mazes with rigorous testing.
- Showcase DFS efficiency and reliability in complex mazes.
- Provide insightful findings and future recommendations.

## Introduction
- Traverse from the starting point to the finishing line inside a maze.
- Utilize Depth-First Search (DFS) algorithm for efficient maze traversal.
- Accomplish the maze-solving goal with an elegantly concise implementation, highlighting the power of DFS.

## Design
- Convert a maze into a graph by representing cells as vertices and walls as edges.
- Identify and represent walls of each cell in the maze as edges in the graph.
- Create vertices for each cell, connecting neighboring vertices with edges representing walls.
- Connect open spaces (corridors) by adding edges between corresponding vertices.
- Handle loops or cycles by adding necessary edges to represent them in the graph.

## Implementation
- Represent the cells as a 2D matrix.
- Input the starting and the ending position.
- The class `Solution` contains methods to traverse the maze and find paths using DFS.
- Utilize a `visited` set to keep track of explored cells during maze traversal.
- Initialize the `visited` set as an empty set before starting the DFS traversal.
- Add the coordinates of each explored cell to the `visited` set to avoid revisiting.
<img width="768" alt="Screenshot 2023-08-03 at 4 53 17 PM" src="https://github.com/girik21/MazeTraversal/assets/87162191/dc8632aa-5940-432d-a7a8-c923773b8a3f">

## Test Cases
- Test the DFS maze traversal with various maze configurations.
- Ensure successful navigation from the starting point to the destination.
<img width="768" alt="Screenshot 2023-08-03 at 4 50 51 PM" src="https://github.com/girik21/MazeTraversal/assets/87162191/bce067c3-3200-421d-a9ca-e3fcdc31f29f">
  
## References
- `Leetcode` <a>https://leetcode.com/problems/the-maze/</a>
- `Prof Henry Chang website` <a>https://hc.labnet.sfbu.edu/~henry/npu/classes//algorithm/graph_alg/slide/maze.html#a1</a>
- `ChatGPT How to solve DFS maze using python` <a>https://chat.openai.com/</a>
