from collections import deque

graph = {'1': ['1', '2'],
         '2': ['3', '4'],
         '3': ['1'],
         '4': ['2'],
         '5': ['3'],
         '6': ['4']}

def bfs(graph, start, search):
    searchQueue = deque()  # очередь
    searchQueue += graph[start]  # добавляем всех соседей начальной точки в очередь
    visited = []  # посещенные вершины
    while searchQueue:
        node = searchQueue.popleft()  # вытащели первое число
        if node not in visited:
            if node == search:
                print('Found')
                print(visited)
                return True
            else:
                searchQueue += graph[node] # добавляем всех соседей посещенной вершины
                visited += [node]
    print('not found')
    return False
bfs(graph, input('Начальная точка '), input('Искомая точка '))