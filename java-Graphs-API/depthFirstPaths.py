class DepthFirstPaths:
	'''
	Decoupleing graph data type from graph processing
	DepthFirstPaths outputs paths from a source vertex s in a Graph.

	Applications: "FloodFill" in Image manipulation tasks.

	'''

	marked = []# list of booleans.holds a value for each vertex in the graph
	edgeTo = []# list of integers. holds the parent vertex from which a vertex was reached.
	source = 0

	def __init__(self,myGraph,source=0):
		'''(Graph,int) -> noneType

		'''
		assert 0<= source < myGraph.nVertices,"Given vertex s is not a vertex in the graph."

		self.marked = [False for x in range(myGraph.nVertices)]
		self.edgeTo = [None for x in range(myGraph.nVertices)]
		self.source = source

		self.marked[self.source] = True
		self.edgeTo[self.source] = self.source
		self.dfs(myGraph,self.source)


	def dfs(self,myGraph,s=0):
		'''(Graph,int) -> NoneType

		Change the marked and edgeTo lists by traversing over the graph.

		'''
		assert 0<= s < myGraph.nVertices,"Given vertex s is not a vertex in the graph."
		for w in myGraph.adj(s):
			if self.marked[w]!=True:
				self.marked[w]=True
				self.edgeTo[w] = s
				self.dfs(myGraph,w)

	def hasPathTo(self,s):
		assert 0<= s < len(self.marked),"Given vertex s is not a vertex in the graph."
		return self.marked[s]

	def pathTo(self,s):
		if self.hasPathTo(s)==False:
			return None
		if s==self.source: #recursion termination
			return []
		return [self.edgeTo[s]] + self.pathTo(self.edgeTo[s]) #recursion