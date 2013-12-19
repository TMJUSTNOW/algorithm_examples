
import unittest
import depthFirstPaths
import graph


class TestGraph(unittest.TestCase):
	""" Unittest test methods for the graph datastructure/API in graph.py"""

	def test_dfs1(self):
		'''
		Testing if the dfs routine processes a special graph correctly.
		'''
		myGraph = graph.Graph(6)
		myGraph.addEdgesFromAdjacencyList(
			[[1],
			[2],
			[3],
			[4,5],
			[],
			[]])

		dfsOfGraph = depthFirstPaths.DepthFirstPaths(myGraph,0)
		self.assertEqual(dfsOfGraph.marked,[True, True, True, True, True, True])
		self.assertEqual(dfsOfGraph.edgeTo,[0,0,1,2,3,3])
	
if __name__=='__main__':
	unittest.main(exit=False)
