class BSNode:

    def __init__(self, val):
        self.left = None
        self.right = None
        self.value = val



class BinarySearchTree:

    def __init__(self):
        self.root = None
    
    
    def add(self, val):
        if not self.root:
            self.root = BSNode(val)
        else:
            runner = self.root
            prev = self.root

            while runner != None:
                prev = runner
                if val == runner.value:
                    print(f"Duplicate value. {val} is already in tree")
                    return self
                if val < runner.value:
                    runner = runner.left
                else:
                    runner = runner.right
            
            runner = BSNode(val)
            if val < prev.value:
                prev.left = runner
            else:
                prev.right = runner
        
        return self

    
    def get_height(self):
        
        def climb(node):
            if not node:
                return 0
            else:
                left_count = climb(node.left) + 1
                right_count = climb(node.right) + 1
                return left_count if left_count > right_count else right_count

        return climb(self.root)


    def print_tree(self):
        height = self.get_height() + 1
        count = 0
        level = 1
        breadth = [self.root] # queue

        while breadth:
            node = breadth.pop(0)

            if node:
                print(f"{height*height*' '} {node.value}", end='')
                breadth.append(node.left)
                breadth.append(node.right)

            else:
                print(height*height*" " + "  ", end='')
            
            count += 1
            if count == level:
                    level = 2 * level + 1
                    print()
                    height -= 1


                


bst = BinarySearchTree()
bst.add(53).add(23).add(90).add(45).add(10).add(80).add(100)
bst.add(85).add(95)
bst.add(81)

bst.print_tree()
