# Định nghĩa lớp PuzzleState để biểu diễn trạng thái của trò chơi.
class PuzzleState:
    def __init__(self, board, parent=None, move=None):
        self.board = board  # Bảng hiện tại của trạng thái
        self.parent = parent  # Trạng thái cha của trạng thái hiện tại
        self.move = move  # Bước di chuyển từ trạng thái cha đến trạng thái hiện tại
        self.empty_pos = self.find_empty()  # Vị trí của ô trống trong bảng
    
    # Phương thức để tìm vị trí của ô trống trong bảng
    def find_empty(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return (i, j)
    
    # Phương thức so sánh hai trạng thái PuzzleState bằng cách so sánh bảng của chúng
    def __eq__(self, other):
        return self.board == other.board
    
    # Phương thức tạo giá trị băm cho trạng thái PuzzleState dựa trên bảng của nó
    def __hash__(self):
        return hash(str(self.board))

# Hàm thực hiện tìm kiếm theo chiều sâu để giải bài toán 8-puzzle
def dfs_8_puzzle(start, goal):
    stack = [PuzzleState(start)]  # Stack để lưu trữ các trạng thái cần duyệt
    closed_set = set()  # Tập hợp để lưu trữ các trạng thái đã duyệt
    goal_state = PuzzleState(goal)  # Trạng thái mục tiêu
    
    while stack:
        current_state = stack.pop()  # Lấy trạng thái ở đầu stack để duyệt
        closed_set.add(current_state)  # Đánh dấu trạng thái hiện tại đã duyệt
        
        # Kiểm tra nếu trạng thái hiện tại là trạng thái mục tiêu
        if current_state.board == goal_state.board:
            path = []
            # Truy ngược từ trạng thái hiện tại đến trạng thái bắt đầu để lấy đường đi
            while current_state:
                path.append(current_state.board)
                current_state = current_state.parent
            return path[::-1]  # Trả về đường đi từ trạng thái bắt đầu đến trạng thái mục tiêu
        
        x, y = current_state.empty_pos
        neighbors = [
            (x-1, y), (x+1, y), (x, y-1), (x, y+1)
        ]
        
        # Duyệt qua các ô hàng xóm của ô trống
        for nx, ny in neighbors:
            if 0 <= nx < 3 and 0 <= ny < 3:
                # Tạo trạng thái hàng xóm mới bằng cách di chuyển ô trống đến ô hàng xóm
                new_board = [row[:] for row in current_state.board]
                new_board[x][y], new_board[nx][ny] = new_board[nx][ny], new_board[x][y]
                neighbor_state = PuzzleState(new_board, parent=current_state)
                
                # Nếu trạng thái hàng xóm chưa được duyệt, thêm nó vào stack
                if neighbor_state not in closed_set:
                    stack.append(neighbor_state)
                    
    return None  # Trả về None nếu không tìm thấy giải pháp

# Hàm để in đường đi giải bài toán
def print_path(path):
    for step in path:
        for row in step:
            print(row)
        print()

# Bảng ban đầu của trò chơi
start = [
    [1, 2, 3],
    [4, 0, 5],
    [6, 7, 8]
]

# Bảng mục tiêu
goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Giải bài toán bằng thuật toán DFS
path = dfs_8_puzzle(start, goal)

# In đường đi giải
if path:
    print("Solution path (DFS):")
    print_path(path)
else:
    print("No solution found.")
