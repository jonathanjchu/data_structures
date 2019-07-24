from single_linked_list import SList

class Stack:

    def __init__(self):
        self.stack = SList()
    

    def push(self, val):
        self.stack.add_to_front(val)
        return self
    

    def pop(self):
        return self.stack.remove_from_front()


    def length(self):
        return self.stack.length()
    

    def print_stack(self):
        self.stack.print_values()
        return self


