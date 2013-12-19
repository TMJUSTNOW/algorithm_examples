class Graph:
	"""
	A simple graph Data structure.
	Assume vertices are numbered from 0 to nVertices-1
	"""
	nVertices = 0 #number of vertices
	nEdges = 0 #number of edges
	def __init__(self,nVertices=0):
		""" (Graph,int) -> NoneType
		>>> myGraph  = Graph(3)
		>>> myGraph.nVertices
		3
		"""
		self.nVertices = nVertices

	def addEdge(self,v,w):
		"""Add an edge between vertices v and w"""

	def adj(self,v):
		"""Returns a list of vertices adjacent to vertex v"""
		return []

	def __str__(self):
		"""String representation"""
		line1 = 'Graph has {0} vertices.\n'.format(self.nVertices)
		line2 = 'Graph has {0} edges.\n'.format(self.nEdges)
		line3 = ''
		for v in range(self.nVertices):
			for w in self.adj(v):
				line3 = line3 + "{0}-{1}\n".format(v,w)
		return line1+line2+line3


def main():
	print "Graph Processing Data Structure Main function. Here are some examples."

	myGraph = Graph(4)
	print myGraph

if __name__=="__main__":
	main()
