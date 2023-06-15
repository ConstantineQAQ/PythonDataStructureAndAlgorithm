# 基于顺序表实现栈类
class StackClass:
    def __init__(self):
        self._stack = []

    def push(self, item):
        self._stack.append(item)

    def pop(self):
        if not self._stack:
            raise Exception('Stack is empty')
        return self._stack.pop()

    def top(self):
        if not self._stack:
            raise Exception('Stack is empty')
        return self._stack[-1]

    def is_empty(self):
        return self._stack == []

    def size(self):
        return len(self._stack)


""" st = StackClass()
st.push(1)
st.push(2)
while not st.is_empty():
    print(st.pop(),end=' ') """


# 基于链表实现栈类
class LNode():
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


class LStack():
    def __init__(self):
        self._top = None

    def is_empty(self):
        return self._top is None

    def top(self):
        if self._top is None:
            raise Exception('Stack is empty')
        return self._top.elem

    def push(self, elem):
        self._top = LNode(elem, self._top)

    def pop(self):
        if self._top is None:
            raise Exception('Stack is empty')
        p = self._top
        self._top = p.next
        return p.elem


def check_pares(text):
    pares = "()[]{}"
    open_pares = "([{"
    opposite = {')': '(', ']': '[', '}': '{'}

    def paretheses(text):
        i, text_len = 0, len(text)
        while True:
            while i < text_len and text[i] not in pares:
                i += 1
            if i >= text_len:
                return
            yield text[i], i
            i += 1

    st = StackClass()
    for pr, i in paretheses(text):
        if pr in open_pares:
            st.push(pr)
        elif st.pop() != opposite[pr]:
            print('Unmatching is found at', i, 'for', pr)
            return False
    print('All parentheses are correctly matched.')
    return True


def infix_exp(exp):
    stack = StackClass()
    res = []
    for i in exp:
        if i in '+-*/':
            while not stack.is_empty() and stack.top() in '*/':
                res.append(stack.pop())
            stack.push(i)
        elif i == '(':
            stack.push(i)
        elif i == ')':
            while stack.top() != '(':
                res.append(stack.pop())
            stack.pop()
        else:
            res.append(i)
    while not stack.is_empty():
        res.append(stack.pop())
    return ''.join(res)


# 基于顺序表实现队列类
class QueueClass:
    def __init__(self, init_len=8):
        self._len = init_len
        self._elems = [0] * init_len
        self._head = 0
        self._num = 0

    def is_empty(self):
        return self._num == 0

    def first(self):
        if self._num == 0:
            raise Exception('Queue is empty')
        return self._elems[self._head]

    def dequeue(self):
        if self._num == 0:
            raise Exception('Queue is empty')
        e = self._elems[self._head]
        self._head = (self._head + 1) % self._len
        self._num -= 1
        return e

    def enqueue(self, elem):
        if self._num == self._len:
            self.__extend()
        self._elems[(self._head + self._num) % self._len] = elem
        self._num += 1

    def __extend(self):
        old_len = self._len
        self._len *= 2
        new_elems = [0] * self._len
        for i in range(old_len):
            new_elems[i] = self._elems[(self._head + i) % old_len]
        self._elems, self._head = new_elems, 0


# 基于链表实现队列类
class LQueue():
    def __init__(self):
        self._head = None
        self._rear = None

    def is_empty(self):
        return self._head is None

    def first(self):
        if self._head is None:
            raise Exception('Queue is empty')
        return self._head.elem

    def dequeue(self):
        if self._head is None:
            raise Exception('Queue is empty')
        p = self._head
        if self._head is self._rear:
            self._head = None
            self._rear = None
        else:
            self._head = p.next
        return p.elem

    def enqueue(self, elem):
        p = LNode(elem)
        if self._head is None:
            self._head = p
            self._rear = p
        else:
            self._rear.next = p
            self._rear = p


""" st = StackClass()
st.push(1)
st.push(2)
while not st.is_empty():
    print(st.pop(),end=' ')

print()

st1 = LStack()
st1.push(2)
st1.push(3)
while not st1.is_empty():
    print(st1.pop(),end=' ')

print()

text = '[(5+x)-(y+z)]'
check_pares(text)

print()

text = '[(5+x)-{y+z)]'
check_pares(text)

print()

exp = '1+2*3/(2-1)'

print(infix_exp(exp))
print(infix_exp('1+2*3/((2-1*5)*4)'))

print()

q = QueueClass()
q.enqueue(1)
q.enqueue(2)
while not q.is_empty():
    print(q.dequeue(),end=' ')

print()

q1 = LQueue()
q1.enqueue(3)
q1.enqueue(2)
while not q1.is_empty():
    print(q1.dequeue(),end=' ') """
