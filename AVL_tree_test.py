class AVLTree:
    def __init__(self):
        self.root = None

    class AVLNode:
        def __init__(self, key, value, left=None, right=None):
            self.key = None
            self.left = None
            self.right = None
            self.value = None
            self.height = 1

    @staticmethod
    def _height(self, node) -> int:
        return node.height if node is not None else 0

    @staticmethod
    def _update_height(self, node):
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    # 获取节点的平衡因子，即左子树高度减去右子树高度
    @staticmethod
    def _get_balance(self, node):
        return self._height(node.left) - self._height(node.right)

    # 左旋
    @staticmethod
    def _left_rotate(self, node):
        yellow = node.right
        green = yellow.left
        yellow.left = node
        node.right = green
        # 更新高度顺序不能错
        self._update_height(node)
        self._update_height(yellow)

    # 右旋
    @staticmethod
    def _right_rotate(self, node):
        yellow = node.left
        green = yellow.right
        yellow.right = node
        node.left = green
        # 更新高度顺序不能错
        self._update_height(node)
        self._update_height(yellow)

    @staticmethod
    def _left_right_rotate(self, node):
        node.left = self._left_rotate(node.left)
        return self._right_rotate(node)

    @staticmethod
    def _right_left_rotate(self, node):
        node.right = self._right_rotate(node.right)
        return self._left_rotate(node)

    @staticmethod
    def _balance(self, node):
        if node is None:
            return None
        bf = self._get_balance(node)
        if bf > 1 and self._get_balance(node.left) >= 0:  # LL
            return self._right_rotate(node)
        elif bf > 1 and self._get_balance(node.left) < 0:  # LR
            return self._left_right_rotate(node)
        elif bf < -1 and self._get_balance(node.right) <= 0:  # RR
            return self._left_rotate(node)
        elif bf < -1 and self._get_balance(node.right) > 0:  # RL
            return self._right_left_rotate(node)
        return node

    def put(self, key, value):
        self.root = self._put(self.root, key, value)

    @staticmethod
    def _put(self, node, key, value) -> AVLNode:
        if node is None:
            return self.AVLNode(key, value)
        if key < node.key:
            node.left = self._put(node.left, key, value)
        elif key > node.key:
            node.right = self._put(node.right, key, value)
        else:
            node.value = value
        self._update_height(node)
        node = self._balance(node)
        return node

    def remove(self, key):
        self.root = self._remove(self.root, key)

    @staticmethod
    def _remove(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self._remove(node.left, key)
        elif key > node.key:
            node.right = self._remove(node.right, key)
        else:
            if node.left is None and node.right is None:
                return None
            elif node.left is None:
                node = node.right
            elif node.right is None:
                node = node.left
            else:
                # s 后继节点
                s = node.right
                while s.left is not None:
                    s = s.left
                # 处理 s 的右子树
                # 用s节点取代node节点
                s.right = self._remove(node.right, s.key)
                s.left = node.left
                node = s
        self._update_height(node)
        node = self._balance(node)
        return node
