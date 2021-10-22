class Node:
    def __init__(self,data=None) -> None:
        self.data=data
        self.next=None
class Linked:
    def __init__(self):
        self.head=None
    def printlist(self):
        value=self.head
        while value is not None:
            print(value.data)
            value = value.next
l=Linked()
l.head=Node("Monday")
day2=Node("Tuesday")
day3=Node("Tuesday")
l.head.next=day2
day2.next=day3
l.printlist()