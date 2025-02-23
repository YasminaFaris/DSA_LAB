class BSTNode:
    def __init__(self, data: int=None):
        """ > w < """
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        pNew = BSTNode(data)
        if self.root is None:
            self.root = pNew
        else:
            prev = self.root
            while True:
                if data < prev.data:
                    if prev.left is None:
                        prev.left = pNew
                        break
                    else:
                        prev = prev.left
                else:
                    if prev.right is None:
                        prev.right = pNew
                        break
                    else:
                        prev = prev.right
    
    def preorder(self, root):
        if (root != None):
            print("->", root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)
    
    def inorder(self, root):
        if (root != None):
            self.inorder(root.left)
            print("->", root.data, end=" ")
            self.inorder(root.right)
    
    def postorder(self, root):
        if (root != None):
            self.postorder(root.left)
            self.postorder(root.right)
            print("->", root.data, end=" ")
    
    def is_empty(self):
        if self.root is None:
            return True
        else:
            return False
    
    def traverse(self):
        if self.is_empty():
            print("This is an empty binary search tree.")
        else:
            print("Preorder:", end=" ")
            self.preorder(self.root)
            print()
            print("Inorder:", end=" ")
            self.inorder(self.root)
            print()
            print("Postorder:", end=" ")
            self.postorder(self.root)
            print()

    def find_min(self):
        pos = self.root
        while pos.left is not None:
            pos = pos.left
        return pos.data
    
    def find_max(self):
        pos = self.root
        while pos.right is not None:
            pos = pos.right
        return pos.data
        

def main():
  my_bst = BST()
  for i in range(int(input())):
    my_bst.insert(int(input()))
  my_bst.traverse()
  print("Max:", my_bst.find_max())
  print("Min:", my_bst.find_min())

main()