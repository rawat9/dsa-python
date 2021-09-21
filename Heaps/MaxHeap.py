class MaxHeap:
    def __init__(self, max_size):
        """
        Create a max-heap with maximum capacity of max_size
        """
        self._elements = [0] * max_size  
        self._count = 0
    
    def __len__(self):
        """
        Return the number of items in the heap
        """
        return self._count

    def capacity(self):
        """
        Return the maximum capacity of the heap
        """
        return len(self._elements)

    def insert(self, value):
        """
        Adds a new value to the heap
        """
        assert self._count < self.capacity(), "Cannot add to a full heap"

        # add the new value to the end of the list
        self._elements[self._count] = value
        self._count += 1

        # Sift the new value up the tree
        self._siftUp(self._count - 1)
        
    def extract(self):
        """
        Extract the maximum value from the heap
        """
        assert self._count > 0, "Cannot extract from an empty heap"

        # Save the root value and copy the last heap value to the root
        root = self._elements[0]
        self._count -= 1
        self._elements[0] = self._elements[self._count]

        # sift the root value down the tree
        self._siftDown(0)
        return root

    def swap(self, fpos, spos):
        """
        Swap two nodes
        """
        self._elements[fpos], self._elements[spos] = self._elements[spos], self._elements[fpos]

    def _siftUp(self, ndx):
        """
        Sift up the value at the ndx element up the tree
        """
        if ndx > 0:
            parent = ndx // 2
            if self._elements[ndx] > self._elements[parent]: # swap elements
                self.swap(ndx, parent)
                self._siftUp(parent)

    def _siftDown(self, ndx):
        """
        Sift the value at the the ndx element down the tree
        """
        left = (2 * ndx) + 1
        right = (2 * ndx) + 2

        # Determine which node contains the larger value
        largest = ndx
        if left < self._count and self._elements[left] >= self._elements[largest]:
            largest = left
        if right < self._count and self._elements[right] >= self._elements[largest]:
            largest = right

        # if the largest value is not at the current index (ndx),
        # swap it with the largest value and repeat the process
        if largest != ndx:
            self.swap(ndx, largest)
            self._siftDown(largest)

    def printHeap(self):
        for i in range(self._count // 2):
            print(" PARENT : " + str(self._elements[i]) + 
                  " LEFT CHILD : " + str(self._elements[(2 * i) + 1]) +
                  " RIGHT CHILD : " + str(self._elements[(2 * i) + 2]))

if __name__ == '__main__':
    maxHeap = MaxHeap(15)
    maxHeap.insert(100)
    maxHeap.insert(84)
    maxHeap.insert(71)
    maxHeap.insert(60)
    maxHeap.insert(23)
    maxHeap.insert(12)
    maxHeap.insert(29)
    maxHeap.insert(1)
    maxHeap.insert(37)
    maxHeap.insert(4)
    maxHeap.insert(90)
    print(' ', maxHeap._count)
    maxHeap.printHeap()
    print('Max Value from the heap: ', maxHeap.extract())


