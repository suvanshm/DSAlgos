class MinHeap:

    def __init__(self):
        self.count = 0
        self.list = [None]

    def parent_idx(self, idx):
        return idx // 2

    def left_idx(self, idx):
        return idx * 2

    def right_idx(self, idx):
        return idx * 2 + 1

    def contains_child(self, idx):
        return self.count >= self.left_idx(idx)

    def add(self, val):
        # print("Adding {} to {}".format(val, self.list))
        self.list.append(val)
        self.count += 1
        self.heapify_up()
        # print("New list: {}".format(self.list))

    def get_min(self):
        if self.count == 0:
            # print("No elements!")
            return
        mininum = self.list[1]
        # print("Removing {} from {}".format(mininum, self.list))
        self.list[1] = self.list[self.count]
        self.count -= 1
        self.list.pop()
        # print("New first element: {}".format(self.list))
        self.heapify_down()
        # print("New list: {}".format(self.list))
        return mininum

    def smaller_child(self, idx):
        if self.count < self.right_idx(idx):
            return self.left_idx(idx)
        else:
            if self.list[self.right_idx(idx)] < self.list[self.left_idx(idx)]:
                return self.right_idx(idx)
            else:
                return self.left_idx(idx)

    def heapify_up(self):
        idx = self.count
        while self.parent_idx(idx) > 0:
            child = self.list[idx]
            parent = self.list[self.parent_idx(idx)]
            if child < parent:
                self.list[idx] = parent
                self.list[self.parent_idx(idx)] = child
            idx = self.parent_idx(idx)

    def heapify_down(self):
        idx = 1
        while self.contains_child(idx):
            # print("Heapifying down!")
            child_idx = self.smaller_child(idx)
            # print("Child index: {}".format(child_idx))
            child = self.list[child_idx]
            parent = self.list[idx]
            # print("Child: {}".format(child))
            # print("Parent: {}".format(parent))
            if child < parent:
                self.list[idx] = child
                self.list[child_idx] = parent
            idx = child_idx


# Testing

# testheap = MinHeap()
# testheap.add(3)
# testheap.add(6)
# testheap.add(11)
# testheap.add(4)
# testheap.add(1)
# print("---------")
# testheap.get_min()
