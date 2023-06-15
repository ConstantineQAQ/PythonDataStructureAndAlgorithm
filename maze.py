from collections import deque

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # 0
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],  # 1
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],  # 2
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],  # 3
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],  # 4
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],  # 5
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],  # 6
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],  # 7
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],  # 8
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]  # 9
]

dirs = [
    lambda x, y: (x + 1, y),
    lambda x, y: (x - 1, y),
    lambda x, y: (x, y - 1),
    lambda x, y: (x, y + 1)
]


def maze_path(x1, y1, x2, y2):
    stack = [(x1, y1)]
    while len(stack) > 0:
        curr_node = stack[-1]  # 栈顶元素
        if curr_node[0] == x2 and curr_node[1] == y2:  # 到达终点
            for p in stack:  # 打印路径
                print(p)
            return True
        for dir in dirs:  # 按照四个方向进行探索
            next_node = dir(curr_node[0], curr_node[1])
            if maze[next_node[0]][next_node[1]] == 0:  # 可以走
                stack.append(next_node)  # 入栈
                maze[next_node[0]][next_node[1]] = 2  # 标记已经走过
                break
        else:
            maze[curr_node[0]][curr_node[1]] = 2
            stack.pop()
    else:
        print("no path")
        return False


def maze_path_queue(x1, x2, y1, y2):
    queue = deque()
    queue.append((x1, y1, -1))
    path = []
    while len(queue) > 0:
        curr_node = queue.pop()
        path.append(curr_node)
        if curr_node[0] == x2 and curr_node[1] == y2:
            for p in path:
                print(p)
            return True
        for dir in dirs:
            next_node = dir(curr_node[0], curr_node[1])
            if maze[next_node[0]][next_node[1]] == 0:
                queue.append((next_node[0], next_node[1], len(path) - 1))
                maze[next_node[0]][next_node[1]] = 2
    else:
        print("no path")
        return False


maze_path(1, 1, 8, 8)
maze_path_queue(1, 1, 8, 8)
