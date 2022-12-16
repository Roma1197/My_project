class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return self.__str__()

    def update(self, value):
        """Updates value of the Node object"""
        self.value = value


class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def __next__(self):
        return self.next

    def __len__(self):
        """Returns number of Nodes in the list.
        When this method defined, built-in len function can be called on class instances"""
        return self.size

    def add_to_tail(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node
        self.size += 1

    def add_to_head(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            current_next = self.head.next
            self.head = node
            self.head.next = current
            self.head.next.next = current_next
        self.size += 1

    def is_empty(self):
        """Returns True if there are no Nodes in the list, False otherwise"""
        return self.size == 0

    def pop(self):
        """Removes last Node from the list and returns it"""
        if self.head is None:
            print("There are no elements in the list")
        else:
            while current.next is not None:
                current = None

    def copy(self):
        """Returns a copy of linked list. Any changes of copy would not affect
        original list"""
        copy_list = LinkedList(self.head)

        if self.is_empty == True:
            print("There are no elements in the list")
        else:
            current = self.head
            while current is not None:
                current = current.next
                copy_list.add_to_tail(current.value)
        return copy_list

    def sorted(self):
        """Returns a copy of linked list, sorted in ascending order -
        Node with the smallest value goes first. Original list will not be
        changed by this method"""
        sorted_list = self.copy()
        if sorted_list.is_empty == True:
            print("There are no elements in the list")
        else:
            for i in range(0, sorted_list.size):
                current = sorted_list.head
                current_previous = sorted_list.head
                while current.next is not None:
                    if current.value > current.next.value:
                        temporary = current
                        temporary.next = current.next.next
                        current = current.next
                        if temporary != sorted_list.head:
                            current_previous.next = current
                        current.next = temporary
                        current.next.next = temporary.next
                    current_previous = current
                    current = current.next
                i += 1
        return sorted_list

    def reversed(self):
        """Returns a copy of the linked list where Nodes are ordered in reverse order:
        head node of original list becomes a tail for copy"""
        reversed_list = self.copy()
        if reversed_list.is_empty == True:
            print("There are no elements in the list")
        else:
            for i in range(0, reversed_list.size):
                current = reversed_list.head
                current_previous = reversed_list.head
                for n in range(0, reversed_list.size - i):
                    temporary = current
                    temporary.next = current.next.next
                    current = current.next
                    if temporary != reversed_list.head:
                        current_previous.next = current
                    current.next = temporary
                    current.next.next = temporary.next
                    n += 1
                i += 1
        return reversed_list

    def is_palindrome(self):
        """A palindrome is a sequence that reads the same forward and backward.
        Method returns True if current list is a palindrome, False otherwise"""
        palindrome_list = []
        current = self.head
        while current is not None:
            palindrome_list.append(current.value)
            current = current.next
        size = len(palindrome_list)
        for i in range(0, size/2):
            if palindrome_list[i] != palindrome_list[size - 1 - i]:
                return False
        return True


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.add_to_tail(1)
    linked_list.add_to_tail(2)
    linked_list.add_to_head(5)
    linked_list.add_to_head(10)
    for node in linked_list:
        print(node)

    assert len(linked_list) == 4
    assert linked_list.is_empty() == False
    assert linked_list.pop().value == 2
    list_copy = linked_list.copy()
    list_copy.add_to_tail(12)
    assert len(list_copy) != len(linked_list)
    sorted_copy = linked_list.sorted()
    assert linked_list.is_palindrome() == False
    assert linked_list.reversed().head.value == 1
