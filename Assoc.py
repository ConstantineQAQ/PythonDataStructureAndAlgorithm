# 创建一个哈希节点类，包含键、值和下一个节点的引用
class HashNode:
    def __init__(self, key, value):
        self.key = key  # 键
        self.value = value  # 值
        self.next = None  # 下一个节点的引用


# 创建一个哈希表类
class HashTable:
    # 初始化哈希表
    def __init__(self, size):
        self.size = size  # 哈希表的大小
        self.table = [None] * self.size  # 初始化为空表

    # 私有方法，计算哈希值
    def _hash(self, key):
        return key % 10  # 使用简单的模运算计算哈希值

    # 插入键值对
    def put(self, key, value):
        hash_key = self._hash(key)  # 计算键的哈希值
        if self.table[hash_key] is None:  # 如果该位置为空，则直接插入
            self.table[hash_key] = HashNode(key, value)
        else:  # 如果不为空，则需要处理冲突
            node = self.table[hash_key]
            while node.next is not None and node.key != key:  # 遍历链表
                node = node.next
            if node.key == key:  # 如果找到了键相同的节点，更新值
                node.value = value
            else:  # 否则，在链表末尾添加新的节点
                node.next = HashNode(key, value)

    # 获取键对应的值
    def get(self, key):
        hash_key = self._hash(key)  # 计算键的哈希值
        node = self.table[hash_key]  # 获取哈希值对应的节点
        while node is not None and node.key != key:  # 遍历链表
            node = node.next
        if node is None:  # 如果没有找到，返回None
            return None
        else:  # 如果找到了，返回对应的值
            return node.value


if __name__ == '__main__':
    hash_table = HashTable(10)  # 创建哈希表
    hash_table.put(1, 'a')  # 插入键值对
    hash_table.put(2, 'b')
    hash_table.put(3, 'c')
    print("3键对应的值为：", hash_table.get(3))  # 获取键对应的值
    hash_table.put(11, 'd')
    hash_table.put(21, 'e')
    hash_table.put(13, 'f')
    print("13键对应的值为：", hash_table.get(13))  # 获取键对应的值
