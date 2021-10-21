class BinaryTree:
    def __init__(self,data=None):
        self.data=data
        self.left=None
        self.right=None
    def insert(self,data):
        if self.data:
            if data<self.data:
                if self.left is None:
                    self.left=BinaryTree(data)
                else:
                    self.left.insert(data)
            elif data>self.data:
                if self.right is None:
                    self.right=BinaryTree(data)
                else:
                    self.right.insert(data)
        else:
            self.data=data
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()
    #preorder left->root->right
    def preorder_traversal(self,root):
        preorder=[]
        if root:
            preorder=self.preorder_traversal(root.left)
            preorder.append(root.data)
            preorder=preorder+self.preorder_traversal(root.right)
        return preorder
    #inorder root->left->right
    def inorder_traversal(self,root):
        inorder=[]
        if root:
            inorder.append(root.data)
            inorder=inorder+self.inorder_traversal(root.left)
            inorder=inorder+self.inorder_traversal(root.right)
        return inorder
    #postorder left->right->root
    def postorder_traversal(self,root):
        postorder=[]
        if root:
            postorder=self.inorder_traversal(root.left)
            postorder=postorder+self.inorder_traversal(root.right)
            postorder.append(root.data)
        return postorder
b=BinaryTree(12)
b.insert(6)
b.insert(14)
b.insert(3)
b.insert(5)
b.printTree()
print(b.preorder_traversal(b))
print(b.inorder_traversal(b))
print(b.postorder_traversal(b))