import heapq

class Node:
    def __init__(self, state, parent=None, g=0, h=0):
        self.state = state
        self.parent = parent
        self.g = g  
        self.h = h  
    
    def __lt__(self, other):
        return (self.g + self.h) < (other.g + other.h)

def h(state, goal_state):
    # Heuristic function (Manhattan distance)
    return sum(abs(state[i] - goal_state[i]) for i in range(len(state)))

def expand(node):
    children = []
    for i in range(len(node.state) - 1):
        for j in range(i + 1, len(node.state)):
            new_state = node.state[:]
            new_state[i], new_state[j] = new_state[j], new_state[i]  # Swap the elements
            children.append(Node(new_state, parent=node, g=node.g + 1, h=h(new_state, goal_state)))
    return children

def reconstruct_path(node):
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    return path[::-1]

def a_star(initial_state, goal_state):
    open_list = []
    closed_set = set()
    heapq.heappush(open_list, Node(initial_state, g=0, h=h(initial_state, goal_state)))
    
    while open_list:
        current_node = heapq.heappop(open_list)
        if current_node.state == goal_state:
            return reconstruct_path(current_node), current_node.g  # Return solution path and number of steps
        
        closed_set.add(tuple(current_node.state))
        
        for child in expand(current_node):
            if tuple(child.state) not in closed_set:
                heapq.heappush(open_list, child)
    
    return None, None

initial_state = [5, 2, 9, 3, 7, 10, 1, 4, 6, 8]
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

solution_path, num_steps = a_star(initial_state, goal_state)
if solution_path:
    print("Solution Path:")
    for state in solution_path:
        print(state)
    print("Number of steps:", num_steps)
else:
    print("No solution found.")
