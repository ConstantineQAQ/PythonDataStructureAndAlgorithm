class SStack():
    def __init__(self):
        self._elems = []
    def is_empty(self):
        return self._elems == []
    def top(self):
        if self._elems == []:
            #raise StackUnderflow("in SStack.top()")
            raise Exception('Stack is empty')
        return self._elems[-1]
    def push(self, elem):
        self._elems.append(elem)
    def pop(self):
        if self._elems == []:
            #raise StackUnderflow("in SStack.pop()")
            raise Exception('Stack is empty')
        return self._elems.pop()
    

dirs = [(0,1),(1,0),(0,-1),(-1,0)]
def mark(maze, pos):
    maze[pos[0]][pos[1]] = 2

def passable(maze, pos):
    return maze[pos[0]][pos[1]] == 0

def find_path(maze, start, end):
    mark(maze,start)
    if start == end:
        print(start,end = ' ')
        return True
    for i in [(0,1),(1,0),(0,-1),(-1,0)]:
        nextp = (start[0]+i[0],start[1]+i[1])
        if passable(maze,nextp):
            if find_path(maze,nextp,end):
                print(start,end = ' ')
                return True
    return False

def print_path(end,pos,st):
    i = 0
    print(end,i,end = ' ')
    i += 1
    while not st.is_empty():
        print(pos,i,end = ' ')
        pos,nxt = st.pop()
        i += 1
        if pos == end:
            break

def maze_solver(maze, start, end):
    if start == end : print(start);return
    st = SStack()
    mark(maze,start)
    st.push((start,0))
    while not st.is_empty():
        pos,nxt = st.pop()
        for i in range(nxt,4):
            nextp = (pos[0]+dirs[i][0],pos[1]+dirs[i][1])
            if nextp == end:
                print_path(end,pos,st)
                return
            if passable(maze,nextp):
                st.push((pos,i+1))
                mark(maze,nextp)
                st.push((nextp,0))
                break
    print("No path found")

maze = [[0,1,0,0,0,0,0,0,0,0],
        [0,0,0,1,1,1,1,1,1,0],
        [1,1,0,1,0,0,0,0,1,0],
        [0,1,0,1,0,1,1,0,1,0],
        [0,1,0,1,0,1,0,0,1,0],
        [0,1,0,1,0,1,0,1,1,0],
        [0,1,0,1,0,1,0,1,0,0],
        [0,1,0,1,0,1,0,1,0,1],
        [0,1,0,1,0,1,0,1,0,1],
        [0,0,0,0,0,0,0,0,0,0]]

start = (0,0)
end = (9,8)

#find_path(maze,start,end)
maze_solver(maze,start,end)