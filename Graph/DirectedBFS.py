from collections import defaultdict

class Graph:
    def __init__(self):
        #default dictionary to store Graph
        self.graph = defaultdict(list)
    #Function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)

    def BFS(self,s):
        #Mark all the vertices as not visited
        visited = [False]*(len(self.graph))

        #create a queue for BFS
        queue = []

        #Mark the source node as visited adn enqueue it
        queue.append(s)
        visited[s] = True

        while queue:
            #Dequeue a vertex from queue and print it
            s=queue.pop(0)
            print s,
            #GEt all the adjacent vertices of the dequeued vetex s
            #if a adjacent has not been visited yet ,then mark it visited
            #and enqueue it
            for i in self.graph[s]:
                if visited[i] ==False:
                    queue.append(i)
                    visited[i] = True

g = Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)
print "BFS Traversal"
g.BFS(2)
