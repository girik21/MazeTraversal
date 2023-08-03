from typing import List

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        visited = set()
        return self.dfs(maze, tuple(start), tuple(destination), visited)

    def dfs(self, maze, start, destination, visited):
        if start == destination:
            return True

        if start in visited:
            return False

        visited.add(start)

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dx, dy in directions:
            x, y = start
            while 0 <= x + dx < len(maze) and 0 <= y + dy < len(maze[0]) and maze[x + dx][y + dy] == 0:
                x += dx
                y += dy

            if self.dfs(maze, (x, y), destination, visited):
                return True

        return False

# Test cases
maze1 = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]]
start1 = [0, 4]
destination1 = [4, 4]
solution = Solution()
print(solution.hasPath(maze1, start1, destination1))  # Output: True

maze2 = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]]
start2 = [0, 4]
destination2 = [3, 2]
print(solution.hasPath(maze2, start2, destination2))  # Output: False

maze3 = [[0, 0, 0, 0, 0], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0], [0, 1, 0, 0, 1], [0, 1, 0, 0, 0]]
start3 = [4, 3]
destination3 = [0, 1]
print(solution.hasPath(maze3, start3, destination3))  # Output: False
