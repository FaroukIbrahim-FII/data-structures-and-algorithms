from collections import deque

class Queue:
  def __init__(self):
    self.dq = deque()

  def enqueue(self, value):
    self.dq.append(value)

  def dequeue(self):
    return self.dq.pop(0)

  def __len__(self):
    return len(self.dq)



class Vertex:
  def __init__(self, value):
    self.value = value

class Edge:
  def __init__(self,vertex, weight):
    self.vertex = vertex
    self.weight = weight

class Graph:
  def __init__(self):
    self.__adj_list = {}


  def add_node(self, value):
    node = Vertex(value)
    self.__adj_list[node] = []
    return node


  def add_edge(self, start_vertex, end_vertex, weight=0):
    if start_vertex not in self.__adj_list:
      raise KeyError("Start Vertex is not found")
    if end_vertex not in self.__adj_list:
      raise KeyError("Start Vertex is not found")
    edge = Edge(end_vertex, weight)
    self.__adj_list[start_vertex].append(edge)


  def get_neighbors(self, vertex):
    return self.__adj_list.get(vertex, [])



  def get_nodes(self):
    if self.__adj_list == []:
        return "null"
    return self.__adj_list.keys()


  def size(self):
    return len(self.__adj_list)


  def bfs(self, start_vertex):
    queue = Queue()
    result = []
    visited = set()

    queue.enqueue(start_vertex)
    visited.add(start_vertex)
    result.append(start_vertex)

    while len(queue):
      current_vertex = queue.dqueue()

      neighbors = self.get_neighbors(current_vertex)

      for edge in neighbors:
        neighbor = edge.vertex

        if neighbor not in visited:
          queue.enqueue(neighbor)
          visited.add(neighbor)
          result.append(neighbor)

    return result
