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

    def insert_front(self, data):
        new_node = DataNode(data)
        if self.head is None :
          self.head = new_node
        else:
          new_node.next = self.head
          self.head = new_node
        self.count += 1

    def insert_before(self, node, data):
        new_node = DataNode(data)
        if self.head is None :
          print("Cannot insert,",node,"does not exist.")
          return
        if self.head.data == node:
            self.insert_front(data)
            return
        cur = self.head
        while cur.next:
           if cur.next.data == node:
              new_node = DataNode(data)
              new_node.next = cur.next
              cur.next = new_node
              self.count += 1
              return
           cur = cur.next
        print("Cannot insert,",node,"does not exist.")

def main():
  mylist = SinglyLinkedList()
  for _ in range(int(input())):
    text = input()
    condition, data = text.split(": ")
    if condition == "F":
      mylist.insert_front(data)
    elif condition == "L":
      mylist.insert_last(data)
    elif condition == "B":
      mylist.insert_before(*data.split(", "))
    # elif condition == "D":
    #    mylist.delete(data)
    else:
        print("Invalid Condition!")
  mylist.traverse()

main()
