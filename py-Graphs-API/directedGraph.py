import graph

class DirectedGraph(graph.Graph):
	"""

	A simple directed graph data structure using the adjacency-list representation.
	Assume vertices are numbered from 0 to nVertices-1

	Extends the graph API with one change: the addEdge method is slightly different.

	"""

	def addEdge(self,v,w):
		"""(DirectedGraph,int,int) -> NoneType

		Add an edge between vertices v and w

		>>> myGraph = DirectedGraph(2)
		>>> myGraph.addEdge(0,1)
		>>> print myGraph


		"""

		assert 0 <= v <= self.nVertices-1, "Vertex index is smaller or greater than the number of vertices."
		assert 0 <= w <= self.nVertices-1, "Vertex index is smaller or greater than the number of vertices."


		if v==w:
			return #todo: self loops should raise exception
		elif w in self.adj(v):
			return #todo: multiple edges should raise exception
		
		self.adjacencyList[v].append(w)


if __name__=="__main__":

	print "DirectedGraph Data Structure. See test_directedGraph to see how it is used."

