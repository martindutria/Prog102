class Node:
    def __init__(self, data):
        self.node_data = data
        self.node_ref = None


class MyList:
    def __init__(self):
        self.node_init = None
        self.index_count = 0

    def empty(self):
        return self.node_init is None

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

    def __index__(self, item):
        n = self.node_init
        index=0
        while n.node_data is not item:
            index += 1
            n = n.node_ref
        return index
    def __iter__(self):
        return self

    def __next__(self):
        pass

    def __str__(self):
        n = self.node_init
        str_print = "["
        if n is None:
            return "[]"
        elif len == 1:
            return "["+str(n)+"]"
        else:
            pos = 1
            while n is not None and pos < len(self):
                str_print += str(n.node_data)+","
                n = n.node_ref
                pos += 1
            return str_print+str(n.node_data)+"]"
