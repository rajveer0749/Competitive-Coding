from collections import deque

def validPath(n, edges, source, destination):
    graph = [[] for _ in range(n)]

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = {source}
    queue = deque([source])

    while queue:
        node = queue.popleft()

        if node == destination:
            return True

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return False


print(validPath(3, [[0, 1], [1, 2], [2, 0]], 0, 2))