class DLNode:
    
    def __init__(self, val):
        self.value = val
        self.next = None
        self.prev = None
    
    
    def display_node(self):
        print(self.value)

        if self.prev != None:
            print(f"Prev: {self.prev.value}")
        else:
            print("Prev: None")
            
        if self.next != None:
            print(f"Next: {self.next.value}")
        else:
            print("Next: None")
      
        return self



class DList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_front(self, val):
        node = DLNode(val)
        node.next = self.head
        self.head = node

        if node.next != None:
            node.next.prev = node
        else:
            self.tail = node
        
        return self
    

    def add_to_back(self, val):        
        if self.tail == None:
            self.add_to_front(val)
        else:
            node = DLNode(val)
            prev_node = self.tail
            prev_node.next = node
            node.prev = prev_node
            self.tail = node
        
        return self
    

    def insert_at(self, val, i):
        if self.head == None:
            print("Empty List")
        elif i == 0:
            self.add_to_front(val)
        else:
            node = self.head
            pos = 1
            while node != None and pos <= i:
                node = node.next
                pos += 1
            
            if node == None:
                print("Index out of range")
            else:
                new_node = DLNode(val)
                
                prev_node = node.prev
                
                new_node.prev = prev_node
                new_node.next = node

                prev_node.next = new_node
                
                node.prev = new_node
                    
        return self


    def remove_from_front(self):
        if self.head != None:
            output = self.head.value

            if self.head.next != None:
                self.head = self.head.next
                self.head.prev = None
            else:
                self.head = None
                self.tail = None
        else:
            output = None

        return output
    

    def remove_from_back(self):
        if self.tail != None:
            output = self.tail.value

            if self.tail.prev != None:
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                self.head = None
                self.tail = None
        
        else:
            output = None

        return output
            

    def remove_val(self, val):
        front_runner = self.head
        back_runner = self.tail

        while front_runner.prev != back_runner:
            if front_runner.value == val:
                self.remove_node(front_runner)
                return self
            elif back_runner.value == val:
                self.remove_node(back_runner)
                return self
            
            front_runner = front_runner.next
            back_runner = back_runner.prev
        
        print(f"{val} not found")
        return self

    
    def remove_node(self, node):
        if node == self.head:
            self.remove_from_front()
        elif node == self.tail:
            self.remove_from_back()

        prev_node = node.prev
        next_node = node.next

        if next_node == None:
            self.tail = prev_node
        else:
            next_node.prev = prev_node
            
        prev_node.next = next_node
        
        return self
    

    def remove_duplicates(self):
        if self.head == None or self.head.next == None:
            return self
        
        outer_runner = self.head
        inner_runner = self.head.next

        while outer_runner != None:
            inner_runner = outer_runner.next

            while inner_runner != None:

                if inner_runner.value == outer_runner.value:
                    self.remove_node(inner_runner)
                    
                inner_runner = inner_runner.next
            outer_runner = outer_runner.next
        
        return self


    def display_node_at(self, i):
        if self.head == None:
            print("Empty List")
        elif i == 0:
            self.head.display_node()
        else:
            node = self.head
            pos = 0    
            while node != None and pos < i:
                node = node.next
                pos += 1
            
            if node == None:
                print("Index out of range")
            else:
                node.display_node()

        return self


    def display_list(self, is_verbose=False):
        if self.head == None:
            print("Empty List")
        else:
            if is_verbose:
                print("head ->", self.head.value)
                print()

            node = self.head
            while node != None:    
                if is_verbose:
                    node.display_node()
                    print()
                else:
                    print(node.value)
                    
                node = node.next
            
            if is_verbose:
                print(self.tail.value, "<- tail")

        return self


    def display_list_reverse(self, is_verbose=False):
        if self.tail == None:
            print("Empty List")
        else:
            if is_verbose:
                print(self.tail.value, "<- tail")

            node = self.tail
            while node != None:    
                if is_verbose:
                    node.display_node()
                    print()
                else:
                    print(node.value)
                    
                node = node.prev

            if is_verbose:
                print("head ->", self.head.value)
                print()
        return self


    def reverse_list(self):
        runner = self.head
        self.head = self.tail
        self.tail = runner

        while runner != None:
            runner.next, runner.prev = runner.prev, runner.next
            runner = runner.prev

        
    def length(self):
        runner = self.head
        count = 0

        while runner:
            runner = runner.next
            count += 1
        
        return count
        


# dl = DList()
# dl.add_to_front("paper").add_to_back("weight").add_to_back("lift")
# #dl.display_list()
# print()

# dl.add_to_front("news")#.display_node_at(0)
# dl.display_list()
# print()

# # dl.display_node_at(2)
# # print()

# dl.display_list(True)
# print()
# print("insert ball at 2")
# dl.insert_at("ball", 2)
# dl.display_list(True)
# print()
# # dl.display_list_reverse()
# # print()
# dl.remove_val("weight").remove_val("foobar")
# dl.display_list()
# print()

# dl.add_to_back("up").add_to_back("news").add_to_back("news").add_to_back("lift").add_to_back("wind")
# dl.display_list()
# print()
# dl.remove_duplicates()
# dl.display_list(True)

dl2 = DList()
dl2.add_to_front("gum").add_to_back("drop").add_to_back("dead").add_to_back("pool")
dl2.add_to_back("water").add_to_back("polo").add_to_back("club").add_to_back("soda")
dl2.add_to_back("fountain").add_to_back("water").add_to_back("polo")

dl2.insert_at("dead", 6)
dl2.display_list()
dl2.remove_duplicates()
print()

#dl2.remove_val("polo")
dl2.display_list()
print()
dl2.reverse_list()
dl2.display_list()

