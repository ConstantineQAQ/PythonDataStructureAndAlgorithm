'''
ADT Graph:
    Graph() creates a new, empty graph.
    addVertex(vert) adds an instance of Vertex to the graph.
    addEdge(fromVert, toVert) Adds a new, directed edge to the graph that connects two vertices.
    addEdge(fromVert, toVert, weight) Adds a new, weighted, directed edge to the graph that connects two vertices.
    getVertex(vertKey) finds the vertex in the graph named vertKey.
    getVertices() returns the list of all vertices in the graph.
    in returns True for a statement of the form vertex in graph, if the given vertex is in the graph, False otherwise.
'''
import sys

from DequeClass import StackClass
import numpy
from DequeClass import QueueClass as SQueue
import heapq
import math


class Graph:  # basic graph class, using adjacency matrix
    def __init__(self, mat, unconn=0):
        vnum = len(mat)  # number of vertices
        for x in mat:  # check validity
            if len(x) != vnum:
                raise ValueError('Argument for Graph is bad')
        self._mat = [mat[i][:] for i in range(vnum)]  # copy mat
        mode = input("请输入你想要的图的类型：(无权图请输入1，有权图请输入2):\n")
        if mode == '1':
            self._unconn = 0
        elif mode == '2':
            self._unconn = float('inf')
        self._vnum = vnum

    def vertex_num(self):
        return self._vnum

    def _invalid(self, v):
        return 0 > v or v >= self._vnum

    def add_vertex(self):
        raise ValueError('Adj-Matrix does not support "add_vertex"')

    def add_edge(self, vi, vj, val=1):
        if self._invalid(vi) or self._invalid(vj):
            raise ValueError(str(vi) + ' or ' + str(vj) + ' is not a valid vertex.')
        self._mat[vi][vj] = val

    def get_edge(self, vi, vj):
        if self._invalid(vi) or self._invalid(vj):
            raise ValueError(str(vi) + ' or ' + str(vj) + ' is not a valid vertex.')
        return self._mat[vi][vj]

    def out_edges(self, vi):
        if self._invalid(vi):
            raise ValueError(str(vi) + ' is not a valid vertex.')
        return self._out_edges(self._mat[vi], self._unconn)

    @staticmethod
    def _out_edges(row, unconn):
        edges = []
        for i in range(len(row)):
            if row[i] != unconn:
                edges.append((i, row[i]))
        return edges

    def __str__(self):
        return '[\n' + '\n'.join(map(str, self._mat)) + '\n]' + 'Unconnected: ' + str(self._unconn)


class GraphAL(Graph):
    def __init__(self, mat=[], unconn=0):
        super().__init__(mat, unconn)
        vnum = len(mat)
        for x in mat:
            if len(x) != vnum:
                raise ValueError('Argument for Graph')
        self._mat = [Graph._out_edges(mat[i], unconn) for i in range(vnum)]
        self._vnum = vnum
        self._unconn = unconn

    def add_vertex(self):
        self._mat.append([])
        self._vnum += 1
        return self._vnum - 1

    def add_edge(self, vi, vj, val=1):
        if self._vnum == 0:
            raise ValueError('Cannot add edge to empty graph.')
        if self._invalid(vi) or self._invalid(vj):
            raise ValueError(str(vi) + ' or ' + str(vj) + ' is not a valid vertex.')
        row = self._mat[vi]
        i = 0
        while i < len(row):
            if row[i][0] == vj:
                self._mat[vi][i] = (vj, val)
                return
            if row[i][0] > vj:
                break
            i += 1
        self._mat[vi].insert(i, (vj, val))

    def get_edge(self, vi, vj):
        if self._invalid(vi) or self._invalid(vj):
            raise ValueError(str(vi) + ' or ' + str(vj) + ' is not a valid vertex.')
        for i, val in self._mat[vi]:
            if i == vj:
                return val
        return self._unconn

    def out_edges(self, vi):
        if self._invalid(vi):
            raise ValueError(str(vi) + ' is not a valid vertex.')
        return self._mat[vi]

    def __str__(self):
        return "[\n" + ",\n".join(map(str, self._mat)) + "\n]" \
            + "\nUnconnected: " + str(self._unconn)


# 图的深度优先遍历
def DFS_graph(graph, v0):
    # 获取图的顶点数
    vnum = graph.vertex_num()
    # 初始化visited数组，表示所有顶点均未被访问
    visited = [0] * vnum
    # 将起始顶点标记为已访问
    visited[v0] = 1
    # 初始化DFS序列，将起始顶点加入其中
    DFS_seq = [v0]
    # 初始化栈，将起始顶点的出边加入栈中
    st = StackClass()
    st.push((0, graph.out_edges(v0)))
    while not st.is_empty():
        i, edges = st.pop()
        if i < len(edges):
            v, e = edges[i]
            st.push((i + 1, edges))
            # 如果顶点v未被访问，则将其加入DFS序列中，并将其出边加入栈中
            if not visited[v]:
                DFS_seq.append(v)
                visited[v] = 1
                st.push((0, graph.out_edges(v)))
    return DFS_seq


# 图的广度优先遍历
def BFS_graph(graph, v0):
    # 获取图的顶点数
    vnum = graph.vertex_num()
    # 初始化visited数组，表示所有顶点均未被访问
    visited = [0] * vnum
    # 将起始顶点标记为已访问
    visited[v0] = 1
    # 初始化BFS序列，将起始顶点加入其中
    BFS_seq = [v0]
    # 初始化队列，将起始顶点的出边加入队列中
    qu = SQueue()
    qu.enqueue(graph.out_edges(v0))
    while not qu.is_empty():
        edges = qu.dequeue()
        for v, e in edges:
            # 如果顶点v未被访问，则将其加入BFS序列中，并将其出边加入队列中
            if not visited[v]:
                BFS_seq.append(v)
                visited[v] = 1
                qu.enqueue(graph.out_edges(v))
    return BFS_seq


def DFS_span_forest(graph):
    # 获取图的顶点数
    vnum = graph.vertex_num()
    # 初始化span_forest数组，表示所有顶点均未被访问
    span_forest = [None] * vnum

    # 定义dfs函数，用于遍历图
    def dfs(graph, v):
        nonlocal span_forest
        # 遍历v的出边
        for u, w in graph.out_edges(v):
            # 如果u未被访问，则将(u,v)加入span_forest中，并继续遍历u的出边
            if span_forest[u] is None:
                span_forest[u] = (v, w)
                dfs(graph, u)

    # 遍历所有顶点
    for v in range(vnum):
        # 如果v未被访问，则将(v,0)加入span_forest中，并遍历v的出边
        if span_forest[v] is None:
            span_forest[v] = (v, 0)
            dfs(graph, v)
    return


def Kruskal(graph):
    vnum = graph.vertex_num()
    reps = [i for i in range(vnum)]
    mst, edges = [], []
    for vi in range(vnum):
        for v, w in graph.out_edges(vi):
            edges.append((w, vi, v))
    edges.sort()
    for w, vi, vj in edges:
        if reps[vi] != reps[vj]:
            mst.append(((vi, vj), w))
            if len(mst) == vnum - 1:
                break
            rep, orep = reps[vi], reps[vj]
            for i in range(vnum):
                if reps[i] == orep:
                    reps[i] = rep
    return mst


# Dijkstra算法
def Dijkstra(graph, start):
    # 获取图的顶点数
    vnum = graph.vertex_num()
    # 初始化dist数组，表示从起始顶点到其他顶点的最短距离
    dist = [float('inf')] * vnum
    dist[start] = 0
    # 初始化path数组，表示从起始顶点到其他顶点的最短路径
    path = [None] * vnum
    # 初始化小根堆，用于存储未确定最短距离的顶点
    pq = [(0, start)]
    while pq:
        # 取出堆顶元素，即当前距离起始顶点最近的顶点
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        # 遍历u的出边
        for v, w in graph.out_edges(u):
            # 如果可以通过u到达v使得距离更短，则更新dist和path数组，并将v加入小根堆中
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                path[v] = u
                heapq.heappush(pq, (dist[v], v))
    return dist, path


# 拓扑排序
def toposort(graph):
    vnum = graph.vertex_num()
    indegree, toposeq, zerov = [0] * vnum, [], -1
    for vi in range(vnum):
        for v, w in graph.out_edges(vi):
            indegree[v] += 1
    for vi in range(vnum):
        if indegree[vi] == 0:
            indegree[vi] = zerov
            zerov = vi
    for n in range(vnum):
        if zerov == -1:
            return False
        toposeq.append(zerov)
        vi = zerov
        zerov = indegree[zerov]
        for v, w in graph.out_edges(vi):
            indegree[v] -= 1
            if indegree[v] == 0:
                indegree[v] = zerov
                zerov = v
    return toposeq


# 设置事件的最早开始时间
def setEventE(vnum, graph, toposeq, ee):
    for k in range(vnum - 1):
        i = toposeq[k]
        for j, w in graph.out_edges(i):
            if ee[j] < ee[i] + w:
                ee[j] = ee[i] + w


# 设置事件的最晚开始时间
def setEventL(vnum, graph, toposeq, eelast, le):
    for i in range(vnum):
        le[i] = eelast
    for k in range(vnum - 2, -1, -1):
        i = toposeq[k]
        for j, w in graph.out_edges(i):
            if le[i] > le[j] - w:
                le[i] = le[j] - w


# AOE网的关键路径
def critical_path(graph):
    toposeq = toposort(graph)
    if not toposeq:
        return False
    vnum = graph.vertex_num()
    ee, le = [0] * vnum, [float('inf')] * vnum
    crt_path = []
    setEventE(vnum, graph, toposeq, ee)
    setEventL(vnum, graph, toposeq, ee[vnum - 1], le)
    for i in range(vnum):
        for j, w in graph.out_edges(i):
            if ee[i] == le[j] - w:
                crt_path.append((i, j, ee[i+1]))
    return crt_path


if __name__ == '__main__':
    # 创建一个4行4列的邻接矩阵
    mat = [[0, 3, 5, 6, 0],
           [3, 0, 1, 0, 0],
           [5, 1, 0, 0, 7],
           [6, 0, 0, 0, 0],
           [0, 0, 7, 0, 0]]
    graph = Graph(mat)
    print("---------下面是邻接矩阵的实现---------")
    print(graph.__str__())
    graph.add_edge(0, 0, 2)
    print(graph.__str__())
    graphal = GraphAL(mat)
    print("---------下面是邻接表的实现---------")
    print(graphal.__str__())
    print("---------下面是深度优先遍历---------")
    print(DFS_graph(graphal, 0))
    print("---------下面是广度优先遍历---------")
    print(BFS_graph(graphal, 0))
    print("---------下面是Kruskal---------")
    print(Kruskal(graph))
    print("---------下面是Dijkstra---------")
    print(Dijkstra(graph, 0))
    mataoe = [[0, 3, 2, 0, 0, 0],
              [0, 0, 0, 2, 3, 0],
              [0, 0, 0, 6, 7, 0],
              [0, 0, 0, 0, 0, 5],
              [0, 0, 0, 0, 0, 6],
              [0, 0, 0, 0, 0, 0]]
    graphaoe = Graph(mataoe)
    print("---------下面是AOE网的关键路径---------")
    print(graphaoe.__str__() + '\n')
    print(critical_path(graphaoe))
