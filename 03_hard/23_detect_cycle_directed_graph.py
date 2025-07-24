# Detect if a given directed graph contains a cycle.

from collections import defaultdict

def has_cycle(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    visited = [False] * n
    rec_stack = [False] * n

    def dfs(node):
        visited[node] = True
        rec_stack[node] = True

        for neighbor in graph[node]:
            if not visited[neighbor]:
                if dfs(neighbor):
                    return True
            elif rec_stack[neighbor]:
                return True

        rec_stack[node] = False
        return False

    for node in range(n):
        if not visited[node]:
            if dfs(node):
                return True
    return False

# Example usage
if __name__ == "__main__":
    n = 4
    edges = [(0, 1), (1, 2), (2, 3), (3, 1)]  # Contains a cycle
    print(f"Input: Nodes = {n}, Edges = {edges}")
    print(f"Output: {has_cycle(n, edges)}")  # True
