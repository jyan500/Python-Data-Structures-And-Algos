from collections import deque
## find mango seller in your network

## friends network is defined by this hash table
graph = dict()
graph["you"] = ["alice", "bob", "claire"]
graph["alice"] = ["peggy"]
graph["bob"] = ["anuj", "peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

## where the graph is a hash map
def bfs(graph, name):
	search_queue = deque()
	## put your first degree connections in the queue
	search_queue += graph[name]
	## keep track of any of your connections that you have already searched
	searched = []
	while (search_queue):
		person = search_queue.popleft()
		if (not person in searched):
			if (is_mango_seller(person)):
				return person 
			else:
				## get your connection's friends into the queue
				search_queue += graph[person]
				searched.append(person)
	return False 

def is_mango_seller(name):
	return name[-1] == 'm'

print(bfs(graph, 'you'))
