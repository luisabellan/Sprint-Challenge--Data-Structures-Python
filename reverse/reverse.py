class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev=None):

        # Iteratively
        #
        # current = self.head
        # while(current is not None):
        #     next = current.next_node
        #     current.next_node = prev
        #     prev = current
        #     current = next
        # self.head = prev

        # Recursively

        def _reverse(node, prev):
            if not node:
                return prev
            next = node.next_node
            node.next_node = prev
            prev = node
            node = next
            return _reverse(node, prev)

        # updates original head
        self.head = _reverse(node=self.head, prev=None)



""" list = LinkedList()
list.add_to_head(1)
list.add_to_head(2)
list.add_to_head(3)
print(list.head.get_value())

list2 = LinkedList()
node = Node(list.head.get_value())
list2.add_to_head(prev) """
"""

list = LinkedList()
list.add_to_head(1)
list.add_to_head(2)
list.add_to_head(3)
list.add_to_head(4)
list.add_to_head(5)
#print(list.head.value) # 5
list.reverse_list(list.head, None)
print(list.head.value) # 5 -> 1
print(list.head.get_next().value) # 4 -> 2
print(list.head.get_next().get_next().value) # 3 -> 3

 """
