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


# Test Nodes:
# 1 --> 2 --> 3 --> 4 --> 5
testnode = Node(5)
# Nodes can be empty also
testnode5 = Node(88)
testnode4 = Node(62423, testnode5)
testnode3 = Node(131, testnode4)
testnode2 = Node(17, testnode3)
testnode.set_next(testnode2)


class LinkedList:
    def __init__(self, value = None):
        headnode = Node(value)
        self.head = headnode

    def get_head(self):
        return self.head

    def new_head(self, value=None):
        headnode = Node(value)
        headnode.set_next(self.head)
        self.head = headnode

    def printlist(self):
        current = self.head
        strlist = ""
        while current:
            if current.get_value() is not None:
                strlist += str(current.get_value()) + "\n"
            else:
                strlist += "None \n"
            current = current.get_next()
        print(strlist)

    def remove(self, value):
        while self.get_head().get_value() == value:
            self.head = self.get_head().get_next()

        current = self.get_head()
        while current.get_next() is not None:
            if current.get_next().get_value() == value:
                current.set_next(current.get_next().get_next())
                pass
            current = current.get_next()

    def reverse(self):
        current = self.head
        prev = None
        while current:
            nextnode = current.get_next()
            current.set_next(prev)
            prev = current
            current = nextnode
        self.head = prev

    def recursive_reverse_util(self, current, prev):
        if current.get_next() is None:
            self.head = current
            self.head.set_next(prev)
            return
        nextnode = current.get_next()
        current.set_next(prev)
        self.recursive_reverse_util(nextnode, current)

    def recursive_reverse(self):
        if self.head is None:
            return
        self.recursive_reverse_util(self.head, None)


# #Test List
testlist = LinkedList(testnode5.get_value())
testlist.new_head(testnode4.get_value())
testlist.new_head(testnode3.get_value())
testlist.new_head(testnode2.get_value())
testlist.new_head(testnode.get_value())
testlist.new_head(11)
testlist.reverse()
testlist.printlist()
print("------------")
testlist.recursive_reverse()
testlist.printlist()


