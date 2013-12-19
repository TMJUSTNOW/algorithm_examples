
import unittest
import depthFirstPaths


class TestGraph(unittest.TestCase):
	""" Unittest test methods for the graph datastructure/API in graph.py"""

	def test_graph1(self):
		'''
		Testing if the nVertices is storing the right number of vertices.
		'''
		myGraph = graph.Graph(4)
		self.assertEqual(myGraph.nVertices,4)
	def test_graph2(self):
		'''
		Testing if we can correctly get the adjacencyList after adding edges.
		'''
		myGraph = graph.Graph(4)
		myGraph.addEdge(0,2)
		myGraph.addEdge(1,2)
		myGraph.addEdge(3,2)
		actual = []
		for v in range(myGraph.nVertices):
			actual.extend([[v,w] for w in myGraph.adjacencyList[v]])

		expected = [[0,2],[1,2],[2,0],[2,1],[2,3],[3,2]]
		self.assertEqual(actual,expected)

if __name__=='__main__':
	unittest.main(exit=False)




	myGraph = Graph(6)
	myGraph.addEdgesFromAdjacencyList(
		[[1],
		[2],
		[3],
		[4,5],
		[],
		[]])

	dfsVal = DepthFirstPaths(myGraph,0)
	print dfsVal.marked
	print dfsVal.edgeTo