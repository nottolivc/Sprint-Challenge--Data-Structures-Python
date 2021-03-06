#from doubly_linked_list import doubly_linked_list
# import not working, declare function class DLL below for use

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None # init storage to be overwritten to limit w dll
        self.storage = DoublyLinkedList()
    
    def __str__(self):
        return f"{self.storage}"

    def append(self, item):
        # if list length is less than capacity
        if self.storage.length == 0:
            # append item to storage
            self.storage.add_to_tail(item)
            # set current item to the dll head
            self.current = self.storage.head
        # if the storage capacity is 
        elif self.storage.length < self.capacity:
            # then link tail to head
            self.storage.add_to_tail(item)
            self.storage.tail.next = self.storage.head
        # set current to the item input while tail linked to head 
        else:
            self.current.value = item
            self.current = self.current.next

    def get(self):
        buffer_size = []
        current = self.storage.head
        # until current item reaches tail of dll
        while current is not self.storage.tail:
            buffer_size.append(current.value)
        # add item
            current = current.next
        # append the tail to the storage list and return it 
        buffer_size.append(self.storage.tail.value)
        return buffer_size

"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""

class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next
    
    def __str__(self):
        return f"value: {self.value}"
        
    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            next_node = self.next
            next_node.prev = self.prev

class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def __str__(self):
        return f"head: {self.head}, tail: {self.tail}, length: {self.length}"
    
    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1
        
        # if list is currently empty
        if self.head is None and self.tail is None:
            # set the head and tail to equal the new node
            self.head = new_node
            self.tail = new_node
        else:
            # the list already has elements in it
            # make new node's next value point to current head 
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        if self.head is None:
            return None
        head_value = self.head.value
        self.delete(self.head)
        return head_value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1
        if not self.tail and not self.head:
            self.tail = new_node
            self.head = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        if self.tail is None:
            return None
        tail_value = self.tail.value
        self.delete(self.tail)
        return tail_value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        if node is self.head:
            return
        old_value = node.value
        self.delete(node)
        self.add_to_head(old_value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if node is self.tail:
            return
        old_value = node.value
        self.delete(node)
        self.add_to_tail(old_value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        # the list is empty -> do nothing
        if self.head is None and self.tail is None:
            return
        # the list is only one node 
        self.length -= 1
        if self.head == self.tail:
            self.head = None                
            self.tail = None
        # the node is the HEAD node (so make sure we handle the head pointer correctly)
        elif self.head == node:
            self.head = node.next        
            node.delete()
        # the node is the TAIL node (make sure tail is handled correctly)
        elif self.tail == node:
            self.tail = node.prev        
            node.delete()
        # the node is just some node in the list
        else:
            node.delete()

    """Returns the highest value currently in the list"""
    def get_max(self):
        if not self.head:
            return None
        max_val = self.head.value
        current = self.head
        while current:
            if current.value > max_val:
                max_val = current.value
            current = current.next
        return max_val

buffer = RingBuffer(3)
print(buffer)
# buffer.get()   # should return []

# buffer.append('a')
# buffer.append('b')
# buffer.append('c')

# buffer.get()   # should return ['a', 'b', 'c']

# # 'd' overwrites the oldest value in the ring buffer, which is 'a'
# buffer.append('d')

# buffer.get()   # should return ['d', 'b', 'c']

# buffer.append('e')
# buffer.append('f')

# buffer.get()   # should return ['d', 'e', 'f']

# # declare classes of dll and node for use in above function