class DepthFirstPaths:
	'''
	Decoupleing graph data type from graph processing
	DepthFirstPaths outputs paths from a source vertex s in a Graph.

	'''

	marked = []
	edgeTo = []

	def __init__(self,myGraph,s=0):
		'''(Graph,int) -> noneType

		'''
		self.marked = [False for x in range(myGraph.nVertices)]
		self.edgeTo = [None for x in range(myGraph.nVertices)]
		self.marked[s] = True
		self.edgeTo[s] = s
		self.dfs(myGraph,s)


	def dfs(self,myGraph,s=0):
		'''(Graph,int) -> NoneType

		Change the marked and edgeTo lists by traversing over the graph.

		'''
		for w in myGraph.adj(s):
			if self.marked[w]!=True:
				self.marked[w]=True
				self.edgeTo[w] = s
				self.dfs(myGraph,w)