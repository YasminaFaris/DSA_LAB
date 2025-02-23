class DataNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.count = 0
        self.head = None

    def traverse(self):
        if self.head is None:
            print("This is an empty list.")
        else:
            now = self.head
            result = ""
            while now:
                if result:
                    result += " -> "
                result += now.data
                now = now.next
            print(result)
    
    def insert_last(self, data):
        new_node = DataNode(data)
        if self.head is None:
            self.head = new_node
        else:
            now = self.head
            while now.next:
                now = now.next
            now.next = new_node
        self.count += 1

def main():
  mylist = SinglyLinkedList()
  for _ in range(int(input())):
    mylist.insert_last(input())
  mylist.traverse()

main()
            