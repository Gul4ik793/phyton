class Node:

    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        if node is None:
            print("Связный список пуст")
            return
        while node is not None:
            print(node.value, end=' ')
            node = node.next
        print()

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node.value
            node = node.next
        return None

    def find_all(self, val):
        nodes = []
        node = self.head
        while node is not None:
            if node.value == val:
                nodes.append(node.value)
            node = node.next
        return nodes

    def find_all_list(self):
        nodes = []
        node = self.head
        while node is not None:
            nodes.append(node.value)
            node = node.next
        return nodes

    def delete(self, val, all=False):
        if self.head is None:
            raise ValueError("Связный список пуст, удаление невозможно")
        while self.head is not None and self.head.value == val:
            self.head = self.head.next
            print(f"Удален элемент {val} из начала списка")
            if self.head is None:
                self.tail = None
            if not all:
                return
        new_node = self.head
        while new_node is not None and new_node.next is not None:
            if new_node.next.value == val:
                new_node.next = new_node.next.next
                print(f"Удален элемент {val} из списка")
                if new_node.next is None:
                    self.tail = new_node
                if not all:
                    return
            else:
                new_node = new_node.next

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        length = 0
        node = self.head
        while node != None:
            length += 1
            node = node.next
        return length

    def insert(self, afterNode, newNode):
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            return
        new_node = self.head
        while new_node is not None:
            if new_node.value == afterNode:
                newNode.next = new_node.next
                new_node.next = newNode
                if newNode.next is None:
                    self.tail = newNode
            return
        new_node = new_node.next

list1 = []
list2 = []
def summ_list(afterNodelist, newNodelist):
    length = afterNodelist.len()
    length2 = newNodelist.len()
    if length == length2:
        list1 = afterNodelist.find_all_list()
        list2 = newNodelist.find_all_list()
        result = []
        for i in range (length):
            result.append(list1[i] + list2[i])
        return result










