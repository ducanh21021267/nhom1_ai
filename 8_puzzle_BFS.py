from collections import deque

class PuzzleState:
    def __init__(self, board, parent=None, move=None):
        self.board = board
        self.parent = parent
        self.move = move
        self.empty_pos = self.find_empty()
    
    def find_empty(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return (i, j)
    
    def __eq__(self, other):
        return self.board == other.board
    
    def __hash__(self):
        return hash(str(self.board))

def bfs_8_puzzle(start, goal):
    open_list = deque([PuzzleState(start)])
    closed_set = set()
    goal_state = PuzzleState(goal)
    
    while open_list:
        current_state = open_list.popleft()
        closed_set.add(current_state)
        
        if current_state.board == goal_state.board:
            path = []
            while current_state:
                path.append(current_state.board)
                current_state = current_state.parent
            return path[::-1]
        
        x, y = current_state.empty_pos
        neighbors = [
            (x-1, y), (x+1, y), (x, y-1), (x, y+1)
        ]
        
        for nx, ny in neighbors:
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_board = [row[:] for row in current_state.board]
                new_board[x][y], new_board[nx][ny] = new_board[nx][ny], new_board[x][y]
                
                neighbor_state = PuzzleState(new_board, parent=current_state)
                
                if neighbor_state not in closed_set and neighbor_state not in open_list:
                    open_list.append(neighbor_state)
                    
    return None  # No solution found

def print_path(path):
    for step in path:
        for row in step:
            print(row)
        print()

# Input the initial board configuration
start = [
    [1, 2, 3],
    [4, 0, 5],
    [6, 7, 8]
]

# Goal state
goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Solve the puzzle using BFS
path = bfs_8_puzzle(start, goal)

# Print the solution path
if path:
    print("Solution path:")
    print_path(path)
else:
    print("No solution found.")
