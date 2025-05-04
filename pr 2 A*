 import heapq  # Importing the heapq module to use priority queue functionality

# Heuristic function using Manhattan distance
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
    # Calculates the Manhattan distance between two points 'a' and 'b'

# Function to get valid neighbors (up, down, left, right) that are not walls (i.e., 0 in grid)
def get_neighbors(pos, grid):
    directions = [(0,1), (1,0), (0,-1), (-1,0)]  # Right, Down, Left, Up
    neighbors = []
    rows, cols = len(grid), len(grid[0])  # Get number of rows and columns in grid
    for dx, dy in directions:
        nx, ny = pos[0] + dx, pos[1] + dy  # Calculate neighbor's coordinates
        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
            # Check bounds and ensure the cell is not blocked (0 = open path)
            neighbors.append((nx, ny))
    return neighbors

# A* algorithm function to find the shortest path from 'start' to 'goal'
def a_star(grid, start, goal):
    open_list = []  # Priority queue to store nodes to be evaluated
    heapq.heappush(open_list, (0, start))  # Push the start node with priority 0
    
    came_from = {}  # Dictionary to store the path (for backtracking)
    g_score = {start: 0}  # Cost from start to each node (start cost is 0)

    while open_list:
        _, current = heapq.heappop(open_list)  # Pop node with lowest 'f' score

        if current == goal:
            # Goal reached, reconstruct path
            path = []
            while current in came_from:
                path.append(current)  # Add current node to path
                current = came_from[current]  # Move to the previous node
            path.append(start)  # Add the start node
            return path[::-1]  # Return reversed path from start to goal

        for neighbor in get_neighbors(current, grid):
            temp_g = g_score[current] + 1  # Tentative g score (moving cost is 1)
            if neighbor not in g_score or temp_g < g_score[neighbor]:
                # If this path to neighbor is better, record it
                came_from[neighbor] = current  # Record how we reached this node
                g_score[neighbor] = temp_g  # Update g score
                f = temp_g + heuristic(neighbor, goal)  # f = g + h
                heapq.heappush(open_list, (f, neighbor))  # Add neighbor to open list with priority f

    return []  # Return empty list if no path is found

# Example 5x5 grid where:
# 0 = walkable path, 1 = wall/obstacle
grid = [
    [0, 1, 1, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 1],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

start = (0, 0)  # Starting position at top-left corner
goal = (4, 4)   # Goal position at bottom-right corner

path = a_star(grid, start, goal)  # Call the A* function
print("Path:", path)  # Print the final path

