class LinkedList:
    """Defines a Singly Linked List.

    attributes: head
    """
    
    def __init__(self):
        """Create a new list with a Sentinel Node"""
        pass

    def insert(self,x,p):
        """Insert element x in the position after p"""
        pass

    def delete(self,p):
        """Delete the node following node p in the linked list."""
        pass

    def print(self):
        """ Print all the elements of a list in a row."""
        pass

    def insertAtIndex(self,x,i):
        """Insert value x at list position i. (The position of the first element is taken to be 0.)"""
        pass

    def search(x):
        """Search for value x in the list. Return a reference to the first node with value x; return None if no such node is found."""
        pass

    def len(self):
        """Return the length (the number of elements) in the Linked List."""
        pass

    def isEmpty(self):
        """Return True if the Linked List has no elements, False otherwise."""
        pass


class ListNode:
    """Represents a node of a Singly Linked List.

    attributes: value, next. 
    """
    def __init__(self,val=None,nxt=None):
        self.value=val
        self.next=nxt

def main():
    L = LinkedList()
    L.insert(10,L.head)
    print('List is: ',L.print())
    L.insert(12,L.head.next)
    print('List is: ',L.print())
    L.insert(2,L.head)
    print('List is: ',L.print())
    print('Size of L is ',L.len())
    L.delete(L.head)
    print('List is: ',L.print())
    L.delete(L.head.next)
    print('List is: ',L.print())
    print('List is empty?',L.isEmpty())
    print('Size of L is ',L.len())
    L.delete(L.head)
    print('List is empty?',L.isEmpty())
    print('Size of L is ',L.len())
    L.insertAtIndex(2,0)
    L.insertAtIndex(1,0)
    L.insertAtIndex(4,2)
    L.insertAtIndex(3,2)
    print('List is: ',L.print())

if __name__ == '__main__':
    main()