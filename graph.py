class Graph:
	"""
	A simple graph Data structure.
	Assume vertices are numbered from 0 to nVertices-1
	"""
	nVertices = 0 #number of vertices
	adjacencyList = [] #We will represent edges using adjacency-list representation.
	#adjacencyList will be a list of lists.

	def __init__(self,nVertices=0):
		""" (Graph,int) -> NoneType
		>>> myGraph  = Graph(3)
		>>> myGraph.nVertices
		3
		"""
		self.nVertices = nVertices
		self.adjacencyList = [[] for x in range(self.nVertices)]


	def addEdge(self,v,w):
		"""Primary: Add an edge between vertices v and w"""
		if v==w:
			return #todo: self loops should raise exception
		elif w in self.adj(v) or v in self.adj(w):
			return #todo: multiple edges should raise exception
		self.adjacencyList[v].append(w)
		self.adjacencyList[w].append(v)

	def adj(self,v):
		"""Returns a list of vertices adjacent to vertex v"""
		return self.adjacencyList[v]

	def __str__(self):
		"""String representation"""
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
		"""
		Append an adjacency list of edges to the graph. This method is not essential.
		"""
		for v,nbhd in enumerate(adjacencyList):
			for w in nbhd:
				addEdge(v,w)


def main():
	print "Graph Processing Data Structure Main function. Here are some examples."

	myGraph = Graph(4)
	myGraph.addEdge(0,2)
	myGraph.addEdge(1,2)
	myGraph.addEdge(3,2)
	print myGraph

if __name__=="__main__":
	main()
