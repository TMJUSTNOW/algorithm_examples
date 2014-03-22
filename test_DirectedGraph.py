import unittest
import directedGraph


class TestDirectedGraph(unittest.TestCase):
	""" Unittest test methods for the directedGraph datastructure/API in directedGraph.py"""

	def test_graph2(self):
		'''
		Testing if we can correctly get the adjacencyList after adding edges.
		'''
		myGraph = directedGraph.DirectedGraph(4)
		myGraph.addEdge(0,2)
		myGraph.addEdge(1,2)
		myGraph.addEdge(3,2)
		actual = []
		for v in range(myGraph.nVertices):
			actual.extend([[v,w] for w in myGraph.adjacencyList[v]])

		expected = [[0,2],[1,2],[3,2]]
		self.assertEqual(actual,expected)

if __name__=='__main__':
	unittest.main(exit=False)