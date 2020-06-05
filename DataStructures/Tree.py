# Implementing Basic Tree


class TreeNode:
    def __init__(self, root):
        self.value = root
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def __repr__(self, level=0):
        ret = "--->" * level + repr(self.value) + "\n"
        for child in self.children:
            ret += child.__repr__(level + 1)
        return ret

    def delete_child(self, child):
        self.children.remove(child)


#Testing Basic Tree
# dnm = TreeNode("Devendra Nath")
# sumit = TreeNode("Sumit")
# amit = TreeNode("Amit")
# udit = TreeNode("Udit")
# yash = TreeNode("Yashasvi")
# mrin = TreeNode("Mrinalini")
# suvansh = TreeNode("Suvansh")
# suhaani = TreeNode("Suhaani")
# elias = TreeNode("Elias")
# dnm.add_child(amit)
# dnm.add_child(sumit)
# dnm.add_child(udit)
# amit.add_child(yash)
# amit.add_child(mrin)
# sumit.add_child(suvansh)
# sumit.add_child(suhaani)
# udit.add_child(elias)
# print(dnm)
# print(sumit.children)
# sumit.delete_child(suhaani)
# print(sumit.children)


#Implementing Binary Tree

# Implementing BST


class BinaryNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value == self.value:
            return
        elif value < self.value:
            if self.left is None:
                self.left = BinaryNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BinaryNode(value)
            else:
                self.right.insert(value)

    def inorder(self):
        if self.value:
            if self.left:
                self.left.inorder()
            print(self.value)
            if self.right:
                self.right.inorder()

    def preorder(self):
        if self:
            print(self.value)
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.value)

    def contain(self, value):
        if self.value is None:
            return False

        if self.value == value:
            return True

        if value < self.value:
            if self.left:
                if self.left.value == value:
                    return True
                else:
                    return self.left.contain(value)
            else:
                return False

        if value > self.value:
            if self.right:
                if self.right.value == value:
                    return True
                else:
                    return self.right.contain(value)
            else:
                return False

    def mintree(self):
        current = self.value
        while current.left:
            current = current.left
        return current

    def remove(self, key):
        if self.contain(key):
            if key < self.value:
                self.left.remove(key)

            elif key > self.value:
                self.right.remove(key)

            else:
                if not self.left and not self.right:
                    self.value = None

                elif self.left and not self.right:
                    temp = self.left.value
                    self.left.value = None
                    self.value = temp

                elif self.right and not self.left:
                    temp = self.right.value
                    self.right.value = None
                    self.value = temp

                else:
                    temp = self.right.mintree()
                    self.right.remove(temp)
                    self.value = temp

        else:
            return



bintree = BinaryNode(12)
bintree.insert(3)
bintree.insert(6)
bintree.insert(14)
bintree.inorder()
print("-----------")
bintree.remove(5)
bintree.inorder()
print("-----------")
bintree.remove(6)
bintree.inorder()
# bintree.preorder()
# bintree.postorder()
# print(bintree.contain(14))


