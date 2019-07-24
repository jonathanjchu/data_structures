class SLNode:
    
    def __init__(self, val):
        self.value = val
        self.next = None



class SList:
    def __init__(self):
        self.head = None


    def add_to_front(self, val):
        new_node = SLNode(val)	# create a new instance of our Node class using the given value
        current_head = self.head	# save the current head in a variable
        new_node.next = current_head	# SET the new node's next TO the list's current head
        self.head = new_node	# SET the list's head TO the node we created in the last step
        return self	                # return self to allow for chaining
    
    
    def add_to_back(self, val):
        if self.head == None:	# if the list is empty
            self.add_to_front(val)	# run the add_to_front method
            return self	# let's make sure the rest of this function doesn't happen if we add to the front

        new_node = SLNode(val)
        runner = self.head

        while (runner.next != None):
            runner = runner.next
        
        runner.next = new_node	# increment the runner to the next node in the list
        return self # return self to allow for chaining

    def print_values(self):
        runner = self.head
        while (runner != None):
            print(runner.value)
            runner = runner.next
        
        return self

    
    def remove_from_front(self):
        if self.head != None:
            output = self.head.value
            self.head = self.head.next
        else:
            output = None

        return output

    
    def remove_from_back(self):
        if self.head == None:
            return None

        prev = self.head

        if prev.next == None:
            self.remove_from_front()

        runner = prev.next

        while (runner.next != None):
            output = runner.value
            prev = runner
            runner = runner.next
        
        prev.next = None

        return output

    
    def remove_val(self, val):
        prev = self.head

        current = prev.next

        while (current != None):
            if current.value == val:
                prev.next = current.next
                return self
            prev = current
            current = current.next
        
        print(f"'{val}' not found")

        return self


    def insert_at(self, val, n):
        if n <= 0:
            self.add_to_front(val)
        else:
            prev = self.head
            current = prev.next

            for i in range(n-1):
                prev = current
                current = current.next
                if current == None:
                    current = SLNode(val)
                    prev.next = current
                    return self
            
            new_node = SLNode(val)
            prev.next = new_node
            new_node.next = current
        
        return self

    
    def move_min_to_front(self):
        if self.head == None:
            print("Empty List")
            return self

        runner = self.head
        prev_node = self.head
        min_node = self.head
        before_min = self.head

        while runner != None:
            if runner.val < min_node.val:
                min_node = runner
                before_min = prev_node
            
            prev_node = runner
            runner = runner.next
        
        before_min = min_node.next
        min_node.next = self.head.next
        self.head = min_node

        return self

    
    def move_max_to_back(self):
        if self.head == None:
            print("Empty List")
            return self
        
        runner = self.head
        prev_node = self.head
        # max_node = self.head
        # before_max = self.head

        while runner != None:
            if runner.val > max_node.val:
                max_node = runner
                # before_max = prev_node
            
            prev_node = runner
            runner = runner.next
        
        # before_max = max_node.next
        prev_node = max_node
    

    def length(self):
        runner = self.head
        count = 0

        while runner:
            runner = runner.next
            count += 1
        
        return count
        


my_list = SList()
my_list.remove_from_back()

my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!")
my_list.add_to_back("actually").add_to_back("they're").add_to_back("not").print_values()

print()

my_list.remove_val("fun!").print_values()

print()

my_list.remove_from_back().print_values()

print()

my_list.remove_from_front().remove_val("actually").print_values()

print()

my_list.insert_at("these", 1).insert_at("the", 2).insert_at("droids", 3).add_to_back("looking for").print_values()

print()

my_list.insert_at("?", 100).print_values()
my_list.remove_val("foobar")
