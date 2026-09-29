class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        p = self.head
        for i in range(index + 1):
            if p is None:
                return -1
            if i == index:
                return p.data
            p = p.next
        return -1

    def insertHead(self, val: int) -> None:
        new_node = node(val)
        if self.head is None:
            new_node.next = None
            self.head = new_node
            self.tail = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def insertTail(self, val: int) -> None:
        new_node = node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def remove(self, index: int) -> bool:
        if self.head is None:
            return False

        if index == 0:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
            return True

        p = self.head
        q = p.next

        if q is None:
            return False

        for i in range(1, index):
            if q is None:
                return False
            p = p.next
            q = q.next

        if q is None:
            return False

        if q == self.tail:
            self.tail = p

        p.next = q.next
        q.next = None
        return True

    def getValues(self):
        p = self.head
        res = []
        while p:
            res.append(p.data)
            p = p.next
        return res
