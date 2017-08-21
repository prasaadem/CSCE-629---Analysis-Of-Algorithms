# Python 2.7.13
# OS: Macintosh
# Author: Aditya Emani - 524002563
# Course: CSCE 629 - Analysis of Algorithms - Fall 2016

# Maximum Flow


class Edge(object):
  def __init__(self, u, v, w):
    self.source = u
    self.sink = v
    self.weight = w

class Flow(object):
  def  __init__(self):
    self.adjacent = {}
    self.flow = {}

  def getEdgesToCorners(self, v):
    return self.adjacent[v]

  def addOneEdge(self, u, v, w = 0):
    if u == v:
      raise ValueError("u == v")
    
    edge = Edge(u, v, w)
    edgeback = Edge(v, u, 0)
    edge.edgeback = edgeback
    edgeback.edgeback = edge

    self.adjacent[u].append(edge)
    self.adjacent[v].append(edgeback)
    
    self.flow[edge] = 0
    self.flow[edgeback] = 0

  def addCorners(self, vertex):
    self.adjacent[vertex] = []

  def augmentedPath(self, source, sink, path):
    if source == sink:
      return path
    for edge in self.getEdgesToCorners(source):
      residual = edge.weight - self.flow[edge]
      if residual > 0 and not (edge, residual) in path:
        result = self.augmentedPath(edge.sink, sink, path + [(edge, residual)])
        if result != None:
          return result

  def maximumFlow(self, source, sink):
    path = self.augmentedPath(source, sink, [])
    while path != None:
      flow = min(res for edge, res in path)
      for edge, res in path:
        self.flow[edge] += flow
        self.flow[edge.edgeback] -= flow
      path = self.augmentedPath(source, sink, []) 
    print 'The maximum flow from ' + source + ' to ' + sink + ' is: '
    return sum(self.flow[edge] for edge in self.getEdgesToCorners(source))


if __name__ == "__main__":
  g = Flow()
  map(g.addCorners, ['a', 'b', 'c', 'd', 'e', 'f'])
  g.addOneEdge('a', 'b', 9)
  g.addOneEdge('a', 'c', 8)
  g.addOneEdge('b', 'c', 6)
  g.addOneEdge('b', 'd', 4)
  g.addOneEdge('c', 'e', 5)
  g.addOneEdge('c', 'e', 2)
  g.addOneEdge('d', 'f', 8)
  g.addOneEdge('d', 'f', 2)
  print g.maximumFlow('a', 'c')