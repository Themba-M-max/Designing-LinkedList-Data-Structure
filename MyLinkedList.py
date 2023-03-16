class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get_node(self, index: int) -> int:        
        node = self.head
        for i in range(index):
            node = node.next
        return node

    def get(self, index: int) -> int:
        if self.size == 0 or index >= self.size:
            return -1

        return self.get_node(index).val

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        if self.size == 0:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if self.size == 0:
            self.head = new_node
        else:
            tail = self.get_node(self.size-1)
            tail.next = new_node
            
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index == self.size:
            return self.addAtTail(val)
        if index == 0:
            return self.addAtHead(val)

        node = self.get_node(index-1)
        new_node = Node(val)
        node.next, new_node.next = new_node, node.next

        self.size += 1


    def deleteAtIndex(self, index: int) -> None:
        if self.size == 0 or index >= self.size:
            return

        if index == 0:
            self.head = self.head.next
        elif index == self.size - 1:
            node = self.get_node(index)
            node.next = None
        else:
            node = self.get_node(index-1)
            node.next = node.next.next
        self.size -= 1

