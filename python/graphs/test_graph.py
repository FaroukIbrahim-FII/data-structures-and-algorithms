from graph import Graph, Vertex


def test_node_can_be_successfully_added_to_the_graph():
  graph = Graph()
  expected = "fffffffffffff"
  actual = graph.add_node('fffffffffffff').value
  assert actual == expected


# A collection of all nodes can be properly retrieved from the graph

def test_get_nodes():

    graph = Graph()

    fii = graph.add_node('FII')

    ibrahim = graph.add_node('ibrahim')

    node = Vertex('node')

    expected = 2

    actual = len(graph.get_nodes())

    assert actual == expected


# All appropriate neighbors can be retrieved from the graph
# Neighbors are returned with the weight between nodes included
# An edge can be successfully added to the graph
def test_get_neighbors():

    graph = Graph()

    fii = graph.add_node('FII')

    ibrahim = graph.add_node('ibrahim')

    graph.add_edge(fii, ibrahim, 27)

    neighbors = graph.get_neighbors(fii)

    assert len(neighbors) == 1

    neighbor_edge = neighbors[0]

    assert neighbor_edge.vertex.value == 'ibrahim'

    assert neighbor_edge.weight == 27


# The proper size is returned, representing the number of nodes in the graph
# A graph with only one node and edge can be properly returned
def test_size():

    graph = Graph()

    graph.add_node('one')

    expected = 1

    actual = graph.size()

    assert actual == expected


# An empty graph properly returns null
def test_empty():

    graph = Graph()

    expected = 0

    actual = len(graph.get_nodes())

    assert actual == expected

def test_bfs():
    graph = Graph()

    apple = graph.add_node('apple')
    cherry = graph.add_node('cherry')
    orange = graph.add_node('orange')
    banana = graph.add_node('banana')

    graph.add_edge(apple,banana)
    graph.add_edge(orange,banana)
    graph.add_edge(cherry,orange)
    graph.add_edge(banana,cherry)

    expected = 'apple ,banana ,cherry ,orange ,'
    actual = graph.bfs(apple)
    assert actual == expected
