class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize the circular queue with a fixed size k.
        :type k: int
        """
        self.size = k
        self.queue = [None] * k
        self.head = -1
        self.tail = -1

    def enQueue(self, value):
        """
        Insert an element into the circular queue.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        if self.head == -1:  # First insertion
            self.head = 0
        self.tail = (self.tail + 1) % self.size
        self.queue[self.tail] = value
        return True

    def deQueue(self):
        """
        Delete an element from the circular queue.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        if self.head == self.tail:  # Only one element left
            self.head = -1
            self.tail = -1
        else:
            self.head = (self.head + 1) % self.size
        return True

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.queue[self.tail]

    def isEmpty(self):
        """
        Check whether the circular queue is empty.
        :rtype: bool
        """
        return self.head == -1

    def isFull(self):
        """
        Check whether the circular queue is full.
        :rtype: bool
        """
        return (self.tail + 1) % self.size == self.head