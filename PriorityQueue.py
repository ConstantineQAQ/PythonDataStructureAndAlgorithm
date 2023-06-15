# 基于堆的优先队列
class PriorityQueue:
    def __init__(self, elist=[]):
        self.elems = elist
        if elist:
            self.buildheap()

    def is_empty(self):
        return not self.elems

    def peek(self):
        if self.is_empty():
            raise Exception("in peek")
        return self.elems[0]

    def enqueue(self, e):
        child = len(self.elems)
        parent = (child - 1) // 2
        while child > 0 and self.elems[parent] > e:
            self.elems[child] = self.elems[parent]
            child, parent = parent, (parent - 1) // 2
        self.elems[child] = e

    def siftup(self, e, last):
        elems, i, j = self.elems, last, (last - 1) // 2
        while i > 0 and e < elems[j]:
            elems[i] = elems[j]
            i, j = j, (j - 1) // 2
        elems[i] = e

    def dequeue(self):
        if self.is_empty():
            raise Exception("in dequeue")
        elems = self.elems
        elems[0], elems[-1] = elems[-1], elems[0]
        e = elems[-1]
        elems[-1] = None  # help garbage collection

        # 下滤
        self.siftdown(0)
        return e

    def siftdown(self, parent):
        left = parent * 2 + 1  # 左孩子
        right = left + 1  # 右孩子
        max = parent  # 假设父节点最大
        elemes = self.elems
        if left < len(elemes) and elemes[left] > elemes[max]:
            max = left  # 左孩子最大
        if right < len(elemes) and elemes[right] > elemes[max]:
            max = right  # 右孩子最大
        if max != parent:
            elemes[parent], elemes[max] = elemes[max], elemes[parent]
            self.siftdown(max)

    def buildheap(self):
        end = len(self.elems)
        for i in range(end // 2, -1, -1):
            self.siftdown(i)


if __name__ == '__main__':
    heap = PriorityQueue([2, 3, 1, 7, 6, 4, 5])
    print(heap.elems)
    while not heap.is_empty():
        heap.elems[0], heap.elems[-1] = heap.elems[-1], heap.elems[0]
        heap.siftdown(0)
    print(heap.elems)
