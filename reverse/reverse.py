import time

start_time = time.time()

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

        # Recursively - Here the runtime will depend on the number of nodes so O(n)

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
end_time = time.time()

#runtime: 2.5272369384765625e-05 seconds using LL
# runtime: 6.937980651855469e-05 seconds using array
print (f"runtime: {end_time - start_time} seconds")


# Stretch: using python arrays or lists
# array = [5,4,3,2,1]
# for i in reversed(array):
#     print(i)
#
# end_time = time.time()
#
# print (f"runtime: {end_time - start_time} seconds") # runtime: 6.937980651855469e-05 seconds using array

#
# list = LinkedList()
# list.add_to_head(1)
# list.add_to_head(2)
# list.add_to_head(3)
# print(list.head.get_value())
#
#
#
#
# list = LinkedList()
# list.add_to_head(1)
# list.add_to_head(2)
# list.add_to_head(3)
# list.add_to_head(4)
# list.add_to_head(5)
# #print(list.head.value) # 5
# list.reverse_list(list.head, None)
# print(list.head.value) # 5 -> 1
# print(list.head.get_next().value) # 4 -> 2
# print(list.head.get_next().get_next().value) # 3 -> 3
