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

def main():
    my_bst = BST()
    for i in range(int(input())):
        my_bst.insert(int(input()))
    
    print("Preorder: ", end="")
    my_bst.preorder(my_bst.root)

main()