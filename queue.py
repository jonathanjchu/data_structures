from double_linked_list import DList

class Queue:

    def __init__(self):
        self.queue = DList()
    

    def enqueue(self, val):
        self.queue.add_to_back(val)
        return self
    

    def dequeue(self):
        return self.queue.remove_from_front()
    

    def length(self):
        return self.queue.length()
