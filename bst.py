#left<=parent<=right
class BST:
    def __init__(self,data=None):
        self.data=data
        self.right=None
        self.left=None

    #Insert method to create nodes
    def insert(self,data):
        if self.data:
            if data<self.data:
                if self.left is None:
                    self.left=BST(data)
                else:
                    self.left.insert(data)
            elif data>self.data:
                if self.right is None:
                    self.right=BST(data)
                else:
                    self.right.insert(data)
        else:
            self.data=data
    #method to compare value of nodes
    def comapareVal(self,value):
        if value<self.data:
            if self.left is None:
                return str(value)+" not found"
            return self.left.comapareVal(value)
        elif value>self.data:
            if self.right is None:
                return str(value)+" not found"
            return self.right.comapareVal(value)
        else:
            print(str(self.data)+" found")
            

