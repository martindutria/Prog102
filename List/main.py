class Node:
    def __init__(self, data):
        self.node_data = data
        self.node_ref = None


class MyList:
    def __init__(self):
        self.node_init = None
        self.index_count = 0

    def add(self, data):
        new_node = Node(data)
        if self.node_init is None:
            self.node_init = new_node
            return
        n = self.node_init
        while n.node_ref is not None:
            n = n.node_ref
        n.node_ref = new_node

    def __getitem__(self, index):
        if index == 0:
            return self.node_init.node_data
        i = 1
        n = self.node_init
        while i < index+1 and n is not None:
            n = n.node_ref
            i = i + 1
        if n is None:
            print("Index out of bound")
        else:
            return n.node_data

    def __setitem__(self, index, data):
        if index == 0:
            self.node_init.node_data = data
        i = 1
        n = self.node_init
        while i < index+1 and n is not None:
            n = n.node_ref
            i = i + 1
        if n is None:
            print("Index out of bound")
        else:
            n.node_data = data

    def __len__(self):
        if self.node_init is None:
            return 0
        n = self.node_init
        count = 0
        while n is not None:
            count = count + 1
            n = n.node_ref
        return count

    def __contains__(self, item):
        if self.node_init is None:
            return False
        n = self.node_init
        while n is not None:
            if n.node_data == item:
                return True
            n = n.node_ref
        return False

    def __iter__(self):
        return self

    def __str__(self):
        n = self.node_init
        print("[", end="")
        if n is None:
            return "List has no element"
        else:

            if len == 1:
                return str(n)+"]"
            else:
                pos = 1
                while n is not None and pos < len(self):
                    print(str(n.node_data), end=",")
                    n = n.node_ref
                    pos += 1
                return str(n.node_data)+"]"


new_list = MyList()
print(new_list)
new_list.add(25)
new_list.add("carlos")
new_list.add(True)
print(len(new_list))
print(new_list)
new_list[0] = 50
print(new_list)
new_list.add("martin")
print(new_list)
print(len(new_list))
print(new_list[3])
print("martin" not in new_list)