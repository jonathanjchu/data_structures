class TrieNode:

    def __init__(self, val):
        self.value = val
        self.isWord = False
        self.children = {}
    

class TrieClass:

    def __init__(self):
        self.root = TrieNode("")


    def insert(self, val):
        runner = self.root

        for c in val:
            if c not in runner.children:
                runner.children[c] = TrieNode(runner.value + c)

            runner = runner.children[c]
            
        runner.isWord = True

        return self
    

    def contains(self, val):
        runner = self.root

        if not runner:
            return False

        for c in val:
            if c in runner.children:
                runner = runner.children[c]
            else:
                return False
        return True
    

    def search(self, val):
        runner = self.root
        if not runner:
            return []

        for c in val:
            if c in runner.children:
                runner = runner.children[c]
            else:
                return []

        masterList = [runner]
        output = []
        i = 0

        while i < len(masterList):
            if masterList[i].isWord:
                output.append(masterList[i].value)
            
            for key in masterList[i].children:
                masterList.append(masterList[i].children[key])
    
            i += 1
        return output
    

    def print_all(self):
        def helper_print_all(node, depth):
            for node in node.children.values():
                print(" "*depth + node.value)
                helper_print_all(node, depth + 1)
        
        helper_print_all(self.root, 0)
    

    def print_words(self):
        def helper_print_words(node, depth):
            for node in node.children.values():
                if node.isWord:
                    print(" "*depth + node.value)
                helper_print_words(node, depth + 1)

        helper_print_words(self.root, 0)
        
        
        

trie = TrieClass()

trie.insert("cat").insert("cater").insert("catherter")
trie.insert("car").insert("cartoon").insert("carrot")
trie.insert("apple").insert("appear")
trie.insert("tries").insert("trick").insert("trip")
trie.insert("be").insert("bear").insert("beets").insert("battlestar").insert("galactica")


trie.print_all()
