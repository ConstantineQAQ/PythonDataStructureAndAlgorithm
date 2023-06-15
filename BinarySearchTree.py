# BinarySearchTree
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        node = Node(key)
        if self.root is None:
            self.root = node
        else:
            self._insert(node, self.root)

    def _insert(self, node, cur_node):
        if node.key < cur_node.key:
            if cur_node.left is None:
                cur_node.left = node
                node.parent = cur_node
            else:
                self._insert(node, cur_node.left)
        else:
            if cur_node.right is None:
                cur_node.right = node
                node.parent = cur_node
            else:
                self._insert(node, cur_node.right)

    def search(self, key):
        if self.root is None:
            return False
        else:
            return self._search(key, self.root)

    def _search(self, key, cur_node):
        if key == cur_node.key:
            return True
        elif key < cur_node.key:
            if cur_node.left is None:
                return False
            else:
                return self._search(key, cur_node.left)
        else:
            if cur_node.right is None:
                return False
            else:
                return self._search(key, cur_node.right)

    def delete(self, key):
        if self.root is None:
            return False
        else:
            return self._delete(key, self.root)

    def _delete(self, key, cur_node):
        if key == cur_node.key:
            if cur_node.left is None and cur_node.right is None:
                if cur_node.parent.left == cur_node:
                    cur_node.parent.left = None
                else:
                    cur_node.parent.right = None
                del cur_node
            elif cur_node.left is None:
                if cur_node.parent.left == cur_node:
                    cur_node.parent.left = cur_node.right
                else:
                    cur_node.parent.right = cur_node.right
                del cur_node
            elif cur_node.right is None:
                if cur_node.parent.left == cur_node:
                    cur_node.parent.left = cur_node.left
                else:
                    cur_node.parent.right = cur_node.left
                del cur_node
            else:
                left_max = self._find_max(cur_node.left)
                cur_node.key = left_max.key
                self._delete(left_max.key, left_max)
        elif key < cur_node.key:
            if cur_node.left is None:
                return False
            else:
                return self._delete(key, cur_node.left)
        else:
            if cur_node.right is None:
                return False
            else:
                return self._delete(key, cur_node.right)

    def _find_max(self, cur_node):
        if cur_node.right is None:
            return cur_node
        else:
            return self._find_max(cur_node.right)

    def print_tree(self):
        if self.root is None:
            print("Empty Tree")
        else:
            self._print_tree(self.root)

    def _print_tree(self, cur_node):
        if cur_node is not None:
            self._print_tree(cur_node.left)
            print(cur_node.key, end=' ')
            self._print_tree(cur_node.right)

    def inOrderTraverse(self, root):
        if root is None:
            return
        self.inOrderTraverse(root.left)
        print(root.key, end=' ')
        self.inOrderTraverse(root.right)

    def preOrderTraverse(self, root):
        if root is None:
            return
        print(root.key, end=' ')
        self.preOrderTraverse(root.left)
        self.preOrderTraverse(root.right)

    def postOrderTraverse(self, root):
        if root is None:
            return
        self.postOrderTraverse(root.left)
        self.postOrderTraverse(root.right)
        print(root.key, end=' ')

    # 按照层次遍历
    def levelOrderTraverse(self, root):
        if root is None:
            return
        queue = []
        queue.append(root)
        while len(queue) > 0:
            node = queue.pop(0)
            print(node.key, end=' ')
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)


def print_treemodel(root, key="key", left="left", right="right"):
    def display(root, key=key, left=left, right=right):
        if getattr(root, right) is None and getattr(root, left) is None:
            line = '%s' % getattr(root, key)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        if getattr(root, right) is None:
            lines, n, p, x = display(getattr(root, left))
            s = '%s' % getattr(root, key)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        if getattr(root, left) is None:
            lines, n, p, x = display(getattr(root, right))
            s = '%s' % getattr(root, key)
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        left_lines, left_n, left_p, left_x = display(getattr(root, left))
        right_lines, right_n, right_p, right_x = display(getattr(root, right))
        s = '%s' % getattr(root, key)
        u = len(s)
        first_line = (left_x + 1) * ' ' + (left_n - left_x - 1) * '_' + s + right_x * '_' + (right_n - right_x) * ' '
        second_line = left_x * ' ' + '/' + (left_n - left_x - 1 + u + right_x) * ' ' + '\\' + (
                right_n - right_x - 1) * ' '
        if left_p < right_p:
            left_lines += [left_n * ' '] * (right_p - left_p)
        elif right_p < left_p:
            right_lines += [right_n * ' '] * (left_p - right_p)
        zipped_lines = zip(left_lines, right_lines)
        lines = [first_line, second_line] + [a + ' ' * u + b for a, b in zipped_lines]
        return lines, left_n + right_n + u, max(left_p, right_p) + 2, left_n + u // 2

    lines, *_ = display(root, key, left, right)
    for line in lines:
        print(line)


if __name__ == '__main__':
    bst = BinarySearchTree()
    a = map(int, input().split())
    for _ in a:
        bst.insert(_)
    bst.print_tree()
    print()
    print("中序遍历结果为：", end=' ')
    bst.inOrderTraverse(bst.root)
    print()
    print("先序遍历结果为：", end=' ')
    bst.preOrderTraverse(bst.root)
    print()
    print("后序遍历结果为：", end=' ')
    bst.postOrderTraverse(bst.root)
    print()
    print("按照层次遍历结果为：", end=' ')
    bst.levelOrderTraverse(bst.root)
    bst.delete(3)
    print()
    bst.levelOrderTraverse(bst.root)
    print()
    print("查找的结果为：", end=' ')
    print(bst.search(5))
    print_treemodel(bst.root)
