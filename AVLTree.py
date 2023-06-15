from BinarySearchTree import Node, BinarySearchTree


# 定义AVL树节点类，继承自二叉树节点类
class AVLNode(Node):
    def __init__(self, key):
        super().__init__(key)  # 调用父类构造函数
        self.height = 1  # 额外增加一个高度属性，初始化为1


# 定义AVL树类，继承自二叉搜索树类
class AVLTree(BinarySearchTree):
    def __init__(self):
        super().__init__()  # 调用父类构造函数

    # 获取节点的高度
    @staticmethod
    def _get_height(node):
        if node is None:  # 若节点为空，高度为0
            return 0
        return node.height

    # 更新节点的高度
    def _update_height(self, node):
        # 节点的高度等于其左右子树高度的最大值加1
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

    # 获取节点的平衡因子，即左子树高度减去右子树高度
    def _get_balance(self, node):
        return self._get_height(node.left) - self._get_height(node.right)

    # 插入操作
    def insert(self, key):
        self.root = self._insert_recursive(key, self.root)

    # 插入操作的递归函数
    def _insert_recursive(self, key, node):
        if not node:
            return AVLNode(key)  # 创建新的AVL节点
        elif key < node.key:
            node.left = self._insert_recursive(key, node.left)  # 在左子树中插入
        else:
            node.right = self._insert_recursive(key, node.right)  # 在右子树中插入

        self._update_height(node)  # 更新节点高度

        return self._balance(node)  # 平衡节点并返回

    # 平衡节点
    def _balance(self, node):
        # 如果节点的左子树比右子树高度大2，需要右旋
        if self._get_balance(node) > 1:
            # 如果节点的左子树的右子树的高度大于其左子树的高度，先进行左旋
            if self._get_balance(node.left) < 0:
                node.left = self._left_rotate(node.left)
            node = self._right_rotate(node)  # 右旋
        # 如果节点的右子树比左子树高度大2，需要左旋
        elif self._get_balance(node) < -1:
            # 如果节点的右子树的左子树的高度大于其右子树的高度，先进行右旋
            if self._get_balance(node.right) > 0:
                node.right = self._right_rotate(node.right)
            node = self._left_rotate(node)  # 左旋

        return node

    # 左旋操作
    def _left_rotate(self, node):
        print(node.key)
        new_root = node.right
        node.right = new_root.left
        new_root.left = node

        self._update_height(node)
        self._update_height(new_root)
        print(new_root.key)
        return new_root

    # 右旋操作
    def _right_rotate(self, node):
        print(node.key)
        new_root = node.left
        node.left = new_root.right
        new_root.right = node

        self._update_height(node)
        self._update_height(new_root)

        print(new_root.key)
        return new_root

    # 删除操作
    def remove(self, key):
        self.root, deleted = self._remove_recursive(key, self.root)
        return deleted

    # 删除操作的递归函数
    def _remove_recursive(self, key, node):
        if node is None:  # 如果节点为空，直接返回
            return node, False

        elif key < node.key:  # 如果删除的键小于当前节点，到左子树中删除
            node.left, deleted = self._remove_recursive(key, node.left)
        elif key > node.key:  # 如果删除的键大于当前节点，到右子树中删除
            node.right, deleted = self._remove_recursive(key, node.right)
        else:  # 找到要删除的节点
            deleted = True
            # 节点有两个子节点的情况，找到左子树中的最大节点替代当前节点，然后删除那个最大节点
            if node.left and node.right:
                temp_node = self._get_max(node.left)
                node.key = temp_node.key
                node.left, _ = self._remove_recursive(temp_node.key, node.left)
            # 节点只有一个子节点或没有子节点的情况
            elif node.left:
                node = node.left
            else:
                node = node.right

        # 如果删除后的节点不为空，更新高度并平衡
        if node is not None:
            self._update_height(node)
            node = self._balance(node)

        return node, deleted

    # 获取子树中的最大值节点
    def _get_max(self, node):
        if node.right is None:  # 如果没有右子节点，当前节点就是最大值节点
            return node
        else:  # 否则到右子树中继续寻找
            return self._get_max(node.right)


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


# 测试代码
if __name__ == '__main__':
    avl_tree = AVLTree()
    avl_tree.insert(3)
    print_treemodel(avl_tree.root)
    print("=====================================")
    avl_tree.insert(29)
    print_treemodel(avl_tree.root)
    print("=====================================")
    avl_tree.insert(2)
    print_treemodel(avl_tree.root)
    print("=====================================")
    avl_tree.insert(4)
    print_treemodel(avl_tree.root)
    print("=====================================")
    avl_tree.insert(59)
    print_treemodel(avl_tree.root)
    print("=====================================")
    avl_tree.insert(1)
    print_treemodel(avl_tree.root)
    print("=====================================")
    avl_tree.insert(4)
    print_treemodel(avl_tree.root)
    print("=====================================")
    avl_tree.insert(5)
    print_treemodel(avl_tree.root)
    print("=====================================")
    avl_tree.insert(6)
    print_treemodel(avl_tree.root)
    print("=====================================")
    avl_tree.insert(17)
    print_treemodel(avl_tree.root)
    print("=====================================")
    avl_tree.insert(15)
    print_treemodel(avl_tree.root)
    print("=====================================")
    avl_tree.insert(16)
    print_treemodel(avl_tree.root)
