# HuffmanTree
import sys


class Node:
    def __init__(self, freq, char=None):
        self.left = None
        self.right = None
        self.freq = freq
        self.char = char

    def __lt__(self, other):
        return self.freq < other.freq


def create_tree(nodes):
    while len(nodes) > 1:
        nodes.sort()
        left_node = nodes.pop(0)
        right_node = nodes.pop(0)
        new_node = Node(left_node.freq + right_node.freq)
        new_node.left = left_node
        new_node.right = right_node
        nodes.append(new_node)
    return nodes[0]


def traverse(node, code, huffman_codes):
    if node.char:
        huffman_codes[node.char] = code
    else:
        traverse(node.left, code + '0', huffman_codes)
        traverse(node.right, code + '1', huffman_codes)


def huffman_encoding(text):
    # 1.构建字典
    freq_dict = {}
    for char in text:
        if char in freq_dict:
            freq_dict.update({char: freq_dict[char] + 1})
        else:
            freq_dict.setdefault(char, 1)

    # 2.构造霍夫曼树
    nodes = [Node(freq_dict[char], char) for char in freq_dict]
    root = create_tree(nodes)

    # 3.递归获取每个char的霍夫曼编码
    huffman_codes = {}
    traverse(root, "", huffman_codes)

    # 4.获取原 Text 的霍夫曼编码
    encoded_text = ""
    for char in text:
        encoded_text += huffman_codes[char]

    return encoded_text, huffman_codes


def huffman_decoding(encoded_text, huffman_codes):
    decoded_text = ""
    code = ""
    for bit in encoded_text:
        code += bit
        for char in huffman_codes:
            if huffman_codes[char] == code:
                decoded_text += char

                code = ""
                break

    return decoded_text


if __name__ == "__main__":
    codes = {}
    a_great_sentence = input("Please input a sentence:")
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, huffman_codes = huffman_encoding(a_great_sentence)
    print("The content of the encoded data is: {}\n".format(encoded_data))
    print("The huffman codes is: {}\n".format(huffman_codes))

    decoded_data = huffman_decoding(encoded_data, huffman_codes)
    print("The content of the encoded data is: {}\n".format(decoded_data))
