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

def dfs(g, start_node, end_node):
	frontier = []
	frontier.append(start_node)
	explored = set()
	while (len(frontier) > 0):
		current_node = frontier.pop()
		if (current_node in explored):
			continue
		if (current_node == end_node):
			return end_node
		frontier += g[current_node]
		explored.add(current_node)
print(dfs(graph, "you", "thom"))

