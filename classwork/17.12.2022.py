graph = {
    "a": ["b"]
}
print(graph)


class graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def edges(self):
        return self.findedges()

    def findedges(self):
        edgename = []
        for vrtx in self.gdict:
            for nxtvrtx in self.gdict[vrtx]:
                if {nxtvrtx, vrtx} not in edgename:
                    edgename.append({vrtx, nxtvrtx})
        return edgename


graph_elements = {
    "a": ["b"]
}
g = graph(graph_elements)
print(g.edges())

graph = {
    "a": ["b"]
}


def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next1 in set(graph[vertex]) - set(path):
            if next1 == goal:
                yield path + [next1]
            else:
                stack.append((next1, path + [next1]))


if list(dfs_paths(graph, "a", "b")) == [['a', 'b']]:
    print(True)
else:
    print(False)
