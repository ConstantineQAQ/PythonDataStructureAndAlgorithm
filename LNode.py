class LNode:
    def __init__(self, element, next):
        self.element = element
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def prepend(self, element):
        self.head = LNode(element, self.head)

    def append(self, element):
        if self.head is None:
            self.head = LNode(element, None)
            return
        p = self.head
        while p.next is not None:
            p = p.next
            p.next = LNode(element, None)

    def pop(self):
        if self.head is None:
            raise ValueError("in pop")
        e = self.head.element
        self.head = self.head.next
        return e

    def pop_last(self):
        if self.head is None:
            raise ValueError("in pop_last")
        p = self.head
        if p.next is None:
            e = p.element
            self.head = None
            return e
        while p.next.next is not None:
            p = p.next
        e = p.next.element
        p.next = None
        return e

