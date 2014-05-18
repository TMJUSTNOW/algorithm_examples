class Graph:
	"""

	A simple graph Data structure using the adjacency-list representation.
	Assume vertices are numbered from 0 to nVertices-1

	"""
	nVertices = 0 #number of vertices
	adjacencyList = [] #We will represent edges using adjacency-list representation.
	#adjacencyList will be a list of lists.

	def __init__(self,nVertices=0):
		''' (Graph,int) -> NoneType

		Initialize the graph with the given vertices.

		>>> myGraph  = Graph(3)
		>>> myGraph.nVertices
		3
		'''
		assert nVertices >= 0, "Number of vertices is smaller than 0."


		self.nVertices = nVertices
		self.adjacencyList = [[] for x in range(self.nVertices)]


	def addEdge(self,v,w):
		"""(Graph,int,int) -> NoneType

		Add an edge between vertices v and w

		>>> myGraph = Graph(2)
		>>> myGraph.addEdge(0,1)
		>>> print myGraph


		"""

		assert 0 <= v <= self.nVertices-1, "Vertex index is smaller or greater than the number of vertices."
		assert 0 <= w <= self.nVertices-1, "Vertex index is smaller or greater than the number of vertices."


		if v==w:
			return #todo: self loops should raise exception
		elif w in self.adj(v) or v in self.adj(w):
			return #todo: multiple edges should raise exception
		
		self.adjacencyList[v].append(w)
		self.adjacencyList[w].append(v)

	def adj(self,v):
		"""(Graph,int) -> list

		Returns a list of vertices adjacent to vertex v

		>>> myGraph = Graph(2)
		>>> myGraph.addEdge(0,1)
		>>> myGraph.adj(1)
		[0]

		"""
		assert 0 <= v <= self.nVertices-1, "Vertex index is smaller or greater than the number of vertices."
		return self.adjacencyList[v]

	def __str__(self):
		"""(Graph) -> String
		
		String representation

		"""
		line1 = 'Graph has {0} vertices.\n'.format(self.nVertices)
		line2 = ''
		nEdges = 0
		for v in range(self.nVertices):
			for w in self.adj(v):
				line2 += "{0}-{1}\n".format(v,w)
				nEdges += 1
		line3 = 'Graph has {0} edges.\n'.format(nEdges/2) #divide by 2 to avoid doublecount
		return line1+line3+line2[:-1]#removing the last '\n' for prettyness.

	def addEdgesFromAdjacencyList(self,adjacencyList=[]):
		"""(Graph,list of lists) -> NoneType

		Append an adjacency list of edges to the graph. 
		This method is not essential.
		
		"""
		for v,nbhd in enumerate(adjacencyList):
			for w in nbhd:
				self.addEdge(v,w)


if __name__=="__main__":

	print "Graph Data Structure. See test_graph to see how it is used."

