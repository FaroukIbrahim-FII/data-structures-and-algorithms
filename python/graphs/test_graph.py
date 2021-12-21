from graph import Graph, Vertex, business_trip


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


def test_business_trip():

    graph = Graph()

    new_york = graph.add_node('new_york')
    london = graph.add_node('london')
    amman = graph.add_node('amman')
    paris = graph.add_node('paris')
    naboo = graph.add_node('Naboo')
    narnia = graph.add_node('Narnia')

    graph.add_edge(new_york,london,150)
    graph.add_edge(london,new_york,150)
    graph.add_edge(new_york,amman,82)
    graph.add_edge(amman,new_york,82)

    graph.add_edge(london,amman,99)
    graph.add_edge(amman,london,99)
    graph.add_edge(london,paris,42)
    graph.add_edge(paris,london,42)

    # Happy Path
    assert "True, $82" == business_trip(graph,[amman, new_york])

    # Edge Case
    assert "False, $0" == business_trip(graph,[london,paris, naboo])

    # expected failure
    assert "False, $0" == business_trip(graph,[narnia, london,naboo])


def test_breadth_first():
    graph = Graph()

    a = graph.add_node('F')
    b = graph.add_node('A')
    c = graph.add_node('R')
    d = graph.add_node('O')
    e = graph.add_node('U')
    f = graph.add_node('K')

    graph.add_edge(a,b)
    graph.add_edge(a,d)

    graph.add_edge(b,c)
    graph.add_edge(b,d)

    graph.add_edge(d,e)
    graph.add_edge(d,f)



    expected = ['F', 'A', 'R', 'O', 'U', 'K']
    actual = graph.depth_first(a)
    assert actual == expected
