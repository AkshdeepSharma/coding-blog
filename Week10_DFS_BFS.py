graph = {'A': {'B', 'C'},
          'B': {'A', 'D'},
          'C': {'A', 'E', 'F'},
          'D': {'B', 'G'},
          'E': {'C', 'G'},
          'F': {'C'},
          'G': {'D', 'E', 'H'},
          'H': {'G'}}


# Depth first search done iteratively.
def dfs_iterative(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited


# Depth first search done recursively.
def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next_node in graph[start] - visited:
        dfs_recursive(graph, next_node, visited)
    return visited


# Depth first search done iteratively to find the paths from start to goal.
def dfs_iterative_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next_node in graph[vertex] - set(path):
            if next_node == goal:
                yield path + [next_node]
            else:
                stack.append((next_node, path + [next_node]))


# Depth first search done recursively to find the paths from start to goal.
def dfs_recursive_paths(graph, start, goal, path=None):
    if path is None:
        path = [start]
    if start == goal:
        yield path
    for next_node in graph[start] - set(path):
        yield from dfs_recursive_paths(graph, next_node, goal, path + [next])


# Breadth first search using a queue.
def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited


# Breadth first search using a queue to find the paths from start to goal.
def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next_node in graph[vertex] - set(path):
            if next_node == goal:
                yield path + [next_node]
            else:
                queue.append((next_node, path + [next_node]))
