# Python 2.7.13
# OS: Macintosh
# Author: Aditya Emani - 524002563
# Course: CSCE 629 - Analysis of Algorithms - Fall 2016

# Single Source shortest path problem

import sys

def shortest_path(graph,source,sink,visited=[],costs={},lists={}):
    if not visited: 
            costs[source]=0
    if sink == source:
        path=[]
        pred=sink
        while pred != None:
            path.append(pred)
            pred=lists.get(pred,None)
        print('shortest path: '+str(list(reversed(path))))
    else :     
        for neighbor in graph[source] :
            if neighbor not in visited:
                new_distance = costs[source] + graph[source][neighbor]
                if new_distance < costs.get(neighbor,float('inf')):
                    costs[neighbor] = new_distance
                    lists[neighbor] = source
        visited.append(source)
        unvisited={}
        for k in graph:
            if k not in visited:
                unvisited[k] = costs.get(k,float('inf'))        
        x=min(unvisited, key=unvisited.get)
        shortest_path(graph,x,sink,visited,costs,lists)
    return costs[sink]

def main():
    graph = {'x': {'a': 2, 'b': 1},
            'a': {'x': 3, 'b': 4, 'c':8},
            'b': {'x': 8, 'a': 2, 'd': 2},
            'c': {'a': 2, 'd': 9, 'e': 4},
            'd': {'b': 1, 'c': 1, 'e': 3},
            'e': {'c': 3, 'd': 3}}
    source = 'x'
    sink = 'e'
    cost = shortest_path(graph,source,sink)
    print 'cost is: ' + str(cost)

main()