# 表达式树
class Node(object):
    """节点"""

    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None


class Tree(object):
    """二叉树"""

    def __init__(self):
        self.root = None

    def add(self, item):
        """为树添加节点"""
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            if cur_node.left is None:
                cur_node.left = node
                return
            else:
                queue.append(cur_node.left)
            if cur_node.right is None:
                cur_node.right = node
                return
            else:
                queue.append(cur_node.right)

    def breadth_travel(self):
        """广度优先遍历"""
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.item, end=' ')
            if cur_node.left is not None:
                queue.append(cur_node.left)
            if cur_node.right is not None:
                queue.append(cur_node.right)

    """深度优先遍历"""
    def preorder(self, node):
        """先序遍历"""
        if node is None:
            return
        print(node.item, end=' ')
        self.preorder(node.left)
        self.preorder(node.right)

    def inorder(self, node):
        """中序遍历"""
        if node is None:
            return
        self.inorder(node.left)
        print(node.item, end=' ')
        self.inorder(node.right)

    def postorder(self, node):
        """后序遍历"""
        if node is None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.item, end=' ')


if __name__ == '__main__':
    tree = Tree()
    for i in range(10):
        tree.add(i)
    print('广度优先遍历：', end='')
    tree.breadth_travel()
    print('\n先序遍历：', end='')
    tree.preorder(tree.root)
    print('\n中序遍历：', end='')
    tree.inorder(tree.root)
    print('\n后序遍历：', end='')
    tree.postorder(tree.root)
    print()
