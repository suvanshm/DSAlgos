class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, newnext):
        self.next = newnext



class Queue:
    def __init__(self, limit=None):
        self.limit = limit
        self.size = 0
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.size == 0

    def has_space(self):
        if self.limit:
            return self.limit > self.size
        else:
            return True

    def get_size(self):
        return self.size

    def peek(self):
        return self.head.get_value()

    def enqueue(self, value):
        if self.has_space():
            entry = Node(value)
            if self.is_empty():
                self.head = entry
                self.tail = entry
            else:
                self.tail.set_next(entry)
                self.tail = entry
            self.size += 1
        else:
            raise QueueOverflowError

    def dequeue(self):
        if not self.is_empty():
            if self.get_size() == 1:
                self.head = None
                self.tail = None
                self.size = 0
            else:
                remove = self.head
                self.head = self.head.get_next()
                return remove.get_value()
                self.size -= 1
        else:
            raise QueueUnderflowError

    def printqueue(self):
        if not self.is_empty():
            current = self.head
            values = []
            while current:
                values.append(current.get_value())
                current = current.get_next()
            print(*values, sep=",")


class QueueOverflowError(Exception):
    def __init__(self):
        print("Queue Overflow!")


class QueueUnderflowError(Exception):
    def __init__(self):
        print("Queue Underflow!")


# Testing:
testqueue = Queue(4)
# testqueue.printqueue()
testqueue.enqueue("a b c")
testqueue.enqueue("ka kha gha")
testqueue.enqueue("alif bey")
testqueue.enqueue("last one")
# testqueue.printqueue()
# testqueue.enqueue("ek baar phir")
testqueue.dequeue()

testqueue.printqueue()
