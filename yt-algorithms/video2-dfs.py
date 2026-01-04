# yt_video2_dfs.py

# -----------------------------
# 1. Tree Node Definition
# (Same as BFS for consistency)
# -----------------------------

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return f"Node({self.value})"


# Example tree (same as BFS)
mytree = Node(
    'A',
    Node('B', Node('D'), Node('E')),
    Node('C', Node('F'), Node('G'))
)

# =====================================================
# 2. DFS - Recursive (Pre-Order)
# =====================================================

def dfs_preorder_print(root):
    if root is None:
        return

    print(root)
    dfs_preorder_print(root.left)
    dfs_preorder_print(root.right)


# ----- 🧠 DFS Pre-Order Output:
# Node(A)
# Node(B)
# Node(D)
# Node(E)
# Node(C)
# Node(F)
# Node(G)


# =====================================================
# 3. DFS - Recursive (Return List)
# =====================================================

def dfs_preorder_list(root):
    if root is None:
        return []

    return (
        [root.value]
        + dfs_preorder_list(root.left)
        + dfs_preorder_list(root.right)
    )


# ----- 🧠 DFS (return list) Output:
# ['A', 'B', 'D', 'E', 'C', 'F', 'G']


# =====================================================
# 4. DFS - Iterative (Using Stack)
# =====================================================

def dfs_iterative(root):
    if root is None:
        return []

    stack = [root]
    result = []

    while stack:
        node = stack.pop()
        result.append(node.value)

        # Right first, so left is processed first
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result


# ----- 🧠 DFS Iterative Output:
# ['A', 'B', 'D', 'E', 'C', 'F', 'G']


# =====================================================
# 5. DFS for a Graph
# =====================================================

def dfs_graph(graph, start):
    visited = set()
    result = []

    def dfs(node):
        if node in visited:
            return

        visited.add(node)
        result.append(node)

        for neighbor in graph.get(node, []):
            dfs(neighbor)

    dfs(start)
    return result


# ----- 🧠 DFS (graph) Output:
# ['A', 'B', 'D', 'E', 'F', 'C']


# -----------------------------
# Example Usage
# -----------------------------
if __name__ == "__main__":

    print("\n--- DFS Recursive Print ---")
    dfs_preorder_print(mytree)

    print("\n--- DFS Recursive Return List ---")
    print(dfs_preorder_list(mytree))

    print("\n--- DFS Iterative ---")
    print(dfs_iterative(mytree))

    print("\n--- DFS for Graph ---")
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    print(dfs_graph(graph, 'A'))
