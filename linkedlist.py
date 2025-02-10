from Spaceship import Spaceship

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def __str__(self):
        return str(self.head)

    def append(self, value):
        new_node = Node(value)
        if (self.length == 0):
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def prepend(self, value):
        new_node = Node(value)
        if (self.length == 0):
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def delfirst(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def dellast(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def insertatindex(self, value, index):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            self.prepend(value)
        elif index == self.length:
            self.append(value)
        else:
            new_node = Node(value)
            current = self.head
            iterator = 0
            while iterator < index - 1:
                current = current.next
                iterator += 1
            new_node.next = current.next
            current.next = new_node
            self.length += 1

    def deleteatindex(self, index):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            self.delfirst(value)
        elif index == self.length:
            self.dellast(value)
        else:
            iterator = 0
            temp = self.head
            pre = self.head
            while iterator < index:
                pre = temp
                temp = temp.next
                iterator += 1
            pre.next = temp.next
            return temp





# TODO : Write function insertatindex to insert a newnode at any given index. Consider all edge cases, including missing nodes.
# TODO : Write fucntion deleteatindex to delete a newnode at any given index. COnsider all edge cases, including missing nodes.
# Make sure to reuse existing function for the correct edge cases for both TODOs
# Write appropriate test function below to test for the new functions.
s1 = Spaceship("Voyager", 300)
s2 = Spaceship("Enterprise", 300)
s3 = Spaceship("Atlantis", 300)
s4 = Spaceship("Challenger", 300)
s5 = Spaceship("Artemis", 300)
mylinkedlist = LinkedList(s1)
mylinkedlist.append(s2)
mylinkedlist.append(s3)
mylinkedlist.append(s4)
mylinkedlist.append(s5)
mylinkedlist.deleteatindex(2)

mylinkedlist.print_list()