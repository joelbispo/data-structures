def depth_first_print(graph, source):
    stack = [source]

    while len(stack) > 0: 
        current = stack.pop()
        print(current)
    
        for neighbor in graph[current]:
            stack.append(neighbor)

graph = {
    'a': ['c', 'b'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
} 


print(depth_first_print(graph, 'a'))
