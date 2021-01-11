
graph1 = { 
'A' : ['B','I'], 
'B' : ['A'], 
'C' : ['D','E','F','I'], 
'D' : ['C'], 
'E' : ['C','H'], 
'F' : ['C','G'], 
'G' : ['F','I'], 
'H' : ['E','G'], 
'I' : ['A','C','G'] 
} 

def dfs(graph, node, visited):
    ''' this function will take graph ,starting point and
    an empty list(to store visited nodes).'''
    if node not in visited:
        visited.append(node) 
        for n in graph[node]:
            dfs(graph,n, visited)
    return visited 
visited = dfs(graph1,'A', []) 
print(visited)

### BREADTH FIRST SEARCH:
import collections
def bfs(graph, start): 
    visited2, queue = [], collections.deque([start])
    visited2.append(start)
    while queue: 
        vertex = queue.popleft()
        for neighbour in graph[vertex]: 
            if neighbour not in visited2: 
                visited2.append(neighbour) 
                queue.append(neighbour) 
    return visited2
    
print(bfs(graph1, 'A'))
