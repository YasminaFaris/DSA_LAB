class BSTNode:
   def __init__(self, data: int=None):
       self.data = data
       self.left = None
       self.right = None

class BST:
   def __init__(self):
       self.root = None
       
   def is_empty(self):
       return self.root == None

   def insert(self, data):
       if not self.root:
           self.root = BSTNode(data)
           return
       current = self.root
       while True:
           if data < current.data:
               if current.left is None:
                   current.left = BSTNode(data)
                   break
               current = current.left
           else:
               if current.right is None:
                   current.right = BSTNode(data)
                   break
               current = current.right

   def find_min(self):
       if self.is_empty():
           return None
       current = self.root
       while current.left:
           current = current.left
       return current.data

   def find_max(self):
       if self.is_empty():
           return None
       current = self.root
       while current.right:
           current = current.right
       return current.data
       
   def deleteNode(self, root, key):
       if not root:
           return root
           
       if key < root.data:
           root.left = self.deleteNode(root.left, key)
       elif key > root.data:
           root.right = self.deleteNode(root.right, key)
       else:
           if root.left is None:
               temp = root.right
               root = None
               return temp
               
           elif root.right is None:
               temp = root.left
               root = None
               return temp
               
           current = root.left
           while current.right:
               current = current.right
           root.data = current.data
           root.left = self.deleteNode(root.left, current.data)
           
       return root
       
   def delete(self, data):
       if self.is_empty():
           print("Delete Error, " + str(data) + " is not found in Binary Search Tree.")
           return
           
       def find(node, key):
           if not node or node.data == key:
               return True if node else False
           return find(node.left, key) if key < node.data else find(node.right, key)
               
       if not find(self.root, data):
           print("Delete Error, " + str(data) + " is not found in Binary Search Tree.")
           return None
           
       self.root = self.deleteNode(self.root, data)
       return data

   def preorder_traversal(self, node):
       if node:
           print("-> " + str(node.data), end=" ")
           self.preorder_traversal(node.left)
           self.preorder_traversal(node.right)

   def inorder_traversal(self, node):
       if node:
           self.inorder_traversal(node.left)
           print("-> " + str(node.data), end=" ")
           self.inorder_traversal(node.right)

   def postorder_traversal(self, node):
       if node:
           self.postorder_traversal(node.left)
           self.postorder_traversal(node.right)
           print("-> " + str(node.data), end=" ")
           
   def preorder(self):
       print("Preorder: ", end="")
       self.preorder_traversal(self.root)
       print()

   def inorder(self):
       print("Inorder: ", end="")
       self.inorder_traversal(self.root)
       print()

   def postorder(self):
       print("Postorder: ", end="")
       self.postorder_traversal(self.root)
       print()

   def traverse(self):
       if self.is_empty():
           print("This is an empty binary search tree.")
       else:
           self.preorder()
           self.inorder()
           self.postorder()

def main():
   my_bst = BST()
   while 1:
       text = input()
       if text == "Done":
           break
       condition, data = text.split(": ")
       if condition == "I":
           my_bst.insert(int(data))
       elif condition == "D":
           my_bst.delete(int(data))
       else:
           print("Invalid Condition")
   my_bst.traverse()

main()