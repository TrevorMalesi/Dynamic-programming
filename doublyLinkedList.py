class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
        self.previous=None
class doubleLinkedList:
    def __init__(self):
        self.head=None
    
    #add new elements
    def push(self,dataValue):
        new_node=Node(dataValue)
        new_node.next=self.head
        if self.head is not None:
            self.head.previous=new_node
        self.head=new_node
    #print the doubly linked list
    def printDoublyLinkedList(self,node):
        while  (node is not None):
            print(node.data)
            last=node
            node=node.next
doubleLinkedList=doubleLinkedList()
doubleLinkedList.push(12)
doubleLinkedList.push(8)
doubleLinkedList.push(62)
doubleLinkedList.printDoublyLinkedList(doubleLinkedList.head)