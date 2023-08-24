class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Append a node to the circular linked list
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            curr_node = self.head
            while curr_node.next != self.head:
                curr_node = curr_node.next
            curr_node.next = new_node
            new_node.next = self.head

    # Delete a node from the circular linked list
    def delete(self, data):
        if self.head is None:
            return

        # If the head node is to be deleted
        if self.head.data == data:
            curr_node = self.head
            while curr_node.next != self.head:
                curr_node = curr_node.next
            curr_node.next = self.head.next
            self.head = self.head.next
        else:
            curr_node = self.head
            prev_node = None
            while curr_node.next != self.head:
                prev_node = curr_node
                curr_node = curr_node.next
                if curr_node.data == data:
                    prev_node.next = curr_node.next
                    break

    # Iterate through the circular linked list
    def iterate(self):
        if self.head is None:
            return
        curr_node = self.head
        while True:
            print(curr_node.data)
            curr_node = curr_node.next
            if curr_node == self.head:
                break


# Test the circular linked list implementation
if __name__ == '__main__':
    cll = CircularLinkedList()
    cll.append(1)
    cll.append(2)
    cll.append(3)
    cll.append(4)

    print("Circular Linked List:")
    cll.iterate()

    cll.delete(3)
    print("Circular Linked List after deleting 3:")
    cll.iterate()
