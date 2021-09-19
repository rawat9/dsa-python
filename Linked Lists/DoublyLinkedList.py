class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, head=None):
        self.head = head
        self.length = 1

    def append(self, element):
        """
        Adds the `element` at the end of the LinkedList
        10 (head) --> 5 --> 16 (tail) --> null
        """
        current = self.head
        newNode = Node(element)

        if self.head:
            while current.next:
                current = current.next
            current.prev = current
            current.next = newNode
            self.length += 1
        else:
            self.head = newNode

    def prepend(self, element) -> None:
        """
        Adds the `element` at the beginning of the LinkedList
        10 --> 5 --> 16 --> 20 --> null
        element --> 10 --> 5 --> 16 --> 20 --> null
        """
        newNode = Node(element)
        newNode.next = self.head
        self.head.prev = newNode
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

    def insert(self, index: int, data: int):
        if index >= self.length:
            self.append(data)
            return 

        if index == 0:
            self.prepend(data)
            return 
        
        newNode = Node(data)

        # leader = value at index - 1
        leader = self.traverseToIndex(index-1)
        follower = leader.next
        leader.next = newNode
        newNode.prev = leader
        newNode.next = follower
        follower.prev = newNode
        self.length += 1

    def traverseToIndex(self, index: int):
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
        node.next.prev = leader
        self.length -= 1
        

if __name__ == '__main__':
    ll = DoublyLinkedList()
    ll.append(10)
    ll.append(5)
    ll.append(8)
    ll.append(1)
    ll.prepend(2)
    ll.insert(2, 9)
    ll.remove(3)
    print('DoublyLinkedList:', ll.print_list(), 'Length:', ll.length)