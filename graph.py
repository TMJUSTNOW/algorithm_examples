class Graph:
	"""
	A simple graph Data structure.
	"""
	V = 0 #number of vertices
	E = 0 #number of edges
	def __init__(self,nVertices=0):
		""" (Graph,int) -> NoneType
		>>> myGraph  = Graph(3)
		>>> myGraph.V
		3
		"""
		self.V = nVertices

	def addEdge(self,v,w):
		"""Add an edge between vertices v and w"""

	def adj(self,v):
		"""Vertices adjacent to vertex v"""

	def __str__(self):
		"""String representation"""


def main():
	print "Graph Processing Data Structure Main function. Here are some examples."

	myGraph = Graph(10)
	print myGraph

if __name__=="__main__":
	main()
