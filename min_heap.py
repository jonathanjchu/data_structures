class MinHeap:

    def __init__(self, arr=[]):
        self.heap = arr

        self.heapify()

    def heapify(self):
        start = (len(self.heap) - 1) // 2

        while start >= 0:
            self.percolate_down(start)
            start -= 1

    
    def percolate_down(self, start):
        pos = start

        while (2 * pos + 1) <= len(self.heap) - 1:
            child = 2 * pos + 1

            if child + 1 <= len(self.heap) - 1 and self.heap[child] > self.heap[child + 1]:
                child += 1

            if self.heap[pos] > self.heap[child]:
                self.heap[pos], self.heap[child] = self.heap[child], self.heap[pos]
                pos = child
            else:
                return


    def add(self, val):
        self.heap.append(val)

        pos = len(self.heap) - 1
        parent = (pos-1) // 2

        # percolate new value up
        while self.heap[parent] > self.heap[pos] and parent >= 0:
            self.heap[parent], self.heap[pos] = self.heap[pos], self.heap[parent]

            pos = parent
            parent = (pos-1) // 2

        return self            

    def remove(self):
        output = self.heap[0]
        self.heap[0] = self.heap.pop()
        
        self.percolate_down(0)

        return output
    

    def print_heap(self):
        level = 0
        prev = -1
        space = len(self.heap) * 2
        
        for count in range(len(self.heap)):
            print((space)*' ', end='')
            print(self.heap[count], end='')

            if count == 2 * (prev + 1):
                print()
                prev = count
                level += 1
                space = space // 2
        
        print()


# minheap = MinHeap()
# minheap.add(40).add(60).add(23).add(12)
# minheap.add(30).add(90).add(20).add(51).add(21).add(85)
# minheap.add(25).add(-10).add(62)
# print(minheap.heap)

# minheap.remove()
# print(minheap.heap)

# minheap.print_heap()

minheap = MinHeap([41, 3, 64, 10, 13, -9, 96, 23, 5, 68, 55, 31, -42, 93, 23, 2])
minheap.print_heap()