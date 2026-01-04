# yt_video1_bfs.py

from collections import deque

# -----------------------------
# 1. Tree Node Definition
# (DO NOT CHANGE — kept exactly as requested)
# -----------------------------

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return f"Node({self.value})"


def bfs(root):
    if root is None:
        return

    queue = deque([root])

    while queue:
        node = queue.popleft()
        print(node)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


# Example tree
mytree = Node(
    'A',
    Node('B', Node('D'), Node('E')),
    Node('C', Node('F'), Node('G'))
)

bfs(mytree)

# ----- 🧠 BFS (print nodes) Output:
# Node(A)
# Node(B)
# Node(C)
# Node(D)
# Node(E)
# Node(F)
# Node(G)


# -----------------------------
# 2. BFS that returns a list
# -----------------------------

def bfs_return_list(root):
    if root is None:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        result.append(node.value)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result


# ----- 🧠 BFS (return list) Output:
# ['A', 'B', 'C', 'D', 'E', 'F', 'G']


# -----------------------------
# 3. BFS with levels separated
# -----------------------------

def bfs_by_level(root):
    if root is None:
        return []

    result = []
    queue = deque([root])

    while queue:
        level = []
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.value)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level)

    return result


# ----- 🧠 BFS (levels) Output:
# [['A'], ['B', 'C'], ['D', 'E', 'F', 'G']]


# -----------------------------
# 4. BFS for a Graph
# -----------------------------

def bfs_graph(graph, start):
    visited = set([start])
    queue = deque([start])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result


# ----- 🧠 BFS (graph) Output:
# ['A', 'B', 'C', 'D', 'E', 'F']


# -----------------------------
# Example Usage
# -----------------------------
if __name__ == "__main__":

    print("\n--- BFS that returns a list ---")
    print(bfs_return_list(mytree))

    print("\n--- BFS with levels separated ---")
    print(bfs_by_level(mytree))

    print("\n--- BFS for Graph ---")
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    print(bfs_graph(graph, 'A'))
