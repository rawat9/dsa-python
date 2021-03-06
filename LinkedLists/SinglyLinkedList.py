class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.tail = None
        self.length = 1
        
    def append(self, data):
        """
        Adds a new Node at the end of the Linked List
        """
        newNode = Node(data)
        
        if self.head:
            self.tail.next = newNode
            self.tail = newNode
            self.length += 1
        else:
            self.head = newNode
            self.tail = self.head

    def get_position(self, position):
        counter = 1
        current = self.head

        if position < 1:
            return None
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1
        return None

    def prepend(self, data):
        """
        Adds the `element` at the beginning of the LinkedList
        10 --> 5 --> 16 --> 20 >> null
        element --> 10 --> 5 --> 16 --> 20 >> null
        """
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        self.length += 1

    def print_list(self):
        """
        Prints the linkedlist 
        """
        array = []
        current = self.head
        while current != None:
            array.append(current.data)
            current = current.next
        return array

    def insert(self, index, data):
        if index >= self.length:
            self.append(data)
            return 

        if index == 0:
            self.prepend(data)
            return 
        
        newNode = Node(data)

        # leader = value at index - 1
        leader = self.traverseToIndex(index-1)
        
        # holdingPointer = where we need to insert the value
        holdingPointer = leader.next

        # insert the node at given index* / leader -> newNode
        leader.next = newNode

        # newNode -> holdingPointer         
        newNode.next = holdingPointer
        self.length += 1

    def traverseToIndex(self, index):
        """
        Helper Function: find the value at index
        """
        counter = 0
        current = self.head 
        while counter != index:
            current = current.next
            counter += 1
        return current

    def remove(self, index):
        leader = self.traverseToIndex(index-1) 

        # node = node to delete
        node = leader.next
        leader.next = node.next
        self.length -= 1
        
    def frequency(self, data):
        """
       Return the count of element
        """
        count = 0
        current = self.head

        while current.next:
            if current.data == data:
                count += 1
            current = current.next

        return f'Frequency of {data}: {count}'

    def lessthan(self, data):
        count = 0
        current = self.head

        while current.next:
            if current.data < data:
                count += 1
            current = current.next
        
        return f'Numbers less than {data}: {count}'


if __name__ == '__main__':
    ll = LinkedList()
    ll.append(22)
    ll.append(2)
    ll.append(2)
    ll.append(77)
    ll.append(100)
    ll.append(6)
    ll.append(43)
    # ll.insert(4, 99)
    # ll.insert(10, 3)
    # ll.remove(4)
    print('LinkedList:', ll.print_list(), 'Length:', ll.length)
    print(ll.frequency(2))
    print(ll.lessthan(100))



