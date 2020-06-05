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


class Stack:
    def __init__(self, limit):
        self.size = 0
        self.limit = limit
        self.head = None

    def is_empty(self):
        return self.size == 0

    def has_space(self):
        return self.limit > self.size

    def peek(self):
        return self.head.get_value()

    def push(self, value):
        if self.has_space():
            newval = Node(value)
            newval.set_next(self.head)
            self.head = newval
            self.size += 1
        else:
            raise StackOverflowError

    def pop(self):
        if not self.is_empty():
            removeditem = self.head
            newhead = self.head.get_next()
            self.head.set_next(None)
            self.head = newhead
            self.size -= 1
            return removeditem.get_value()
        else:
            raise StackUnderflowError

    def print(self):
        current = self.head
        while current:
            print(str(current.get_value()))
            current = current.get_next()


class StackOverflowError(Exception):
    def __init__(self):
        print("Stack Overflow!")


class StackUnderflowError(Exception):
    def __init__(self):
        print("Stack Underflow!")


# Testing
print("testing")
teststack = Stack(6)
teststack.push(3)
teststack.push(11)
teststack.push(211)
# print(teststack.peek())
teststack.push(17)
teststack.push(2132)
teststack.push(2)
#teststack.push(9)
teststack.pop()
teststack.print()

