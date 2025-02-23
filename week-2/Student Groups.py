class ArrayStack:
    def __init__(self):
        self.stack = list()

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty() == 0:
            return self.stack.pop()
        return
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
class SepMembers:
    def __init__(self, m, n, members):
        self.m = m
        self.n = n
        self.members = members
        self.stack = ArrayStack()

        self.groups = list()
        for _ in range(m):
            self.groups.append(list())

    def Seperate(self):
        for member in self.members:
            self.stack.push(member)

        index = 0
        while not self.stack.is_empty():
            member = self.stack.pop()
            group = self.groups.__getitem__(index)
            group.append(member)
            index = (index + 1) % self.m

    def print_stack(self):
        for i in range(self.m):
            group_str = "Group " + str(i+1) + ":"
            group = self.groups.__getitem__(i)
            for j, member in enumerate(group):
                if j > 0:
                    group_str += ", "
                else:
                    group_str += " "
                group_str += member
            print(group_str)

def main():
    m = int(input())
    n = int(input())

    members = list()
    for _ in range(n):
        member = input().strip()
        members.append(member)

    seperate = SepMembers(m, n, members)
    seperate.Seperate()
    seperate.print_stack()

main()
