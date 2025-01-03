class Queue(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop()
        return None  # Return None if queue is empty

    def size(self):
        return len(self.items)

    def printQueue(self):
        print(self.items)

    def clear(self):
        self.items = []

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        return None

    def isFull(self, max_size):
        return self.size() == max_size

    def reverse(self):
        self.items.reverse()

    def search(self, item):
        return item in self.items

    def toList(self):
        return list(self.items)

    def merge(self, another_queue):
        self.items = another_queue.items + self.items

    def clone(self):
        new_queue = Queue()
        new_queue.items = self.items[:]
        return new_queue

    def rotate(self, k):
        for _ in range(k):
            self.enqueue(self.dequeue())

    def countOccurrences(self, item):
        return self.items.count(item)

    def clearElement(self, item):
        self.items = [x for x in self.items if x != item]

    def printQueue(self):
        return self.items


# Create two queue instances
q1 = Queue()
q2 = Queue()

# 1. isEmpty
print("=====================================================")
print("Is q1 empty?:", q1.isEmpty())  # Output: True

# 2. enqueue
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
q1.enqueue(4)
print("After enqueue operations on q1:", q1.printQueue()) # Output: [4, 3, 2, 1]

# 3. size
print("Size of q1:", q1.size())  # Output: 4

# 4. peek
print("=====================================================")
print("Peek at front of q1:", q1.peek())  # Output: 1

# 5. dequeue
print("Queue before dequeue on q1:", q1.printQueue()) # Output: [4, 3, 2, 1]
print("Dequeue operation on q1:", q1.dequeue())  # Output: 1
print("Queue after dequeue on q1:", q1.printQueue()) # Output: [4, 3, 2]

# 6. reverse
print("=====================================================")
q1.reverse()
print("Queue after reverse on q1: ", q1.printQueue()) # Output: [2, 3, 4]

# 7. search
print("Is 3 in q1?:", q1.search(3))  # Output: True
print("Is 5 in q1?:", q1.search(5))  # Output: False

# 8. toList
queue_list = q1.toList()
print("Queue convert into list on q1:", queue_list) # Output: [2, 3, 4]
print("Type of the converted list:", type(queue_list))

# 9. merge
print("=====================================================")
q2.enqueue(5)
q2.enqueue(6)
print("q1 elements:", q1.printQueue())
print("q2 elements:", q2.printQueue())
q2.merge(q1)
print("Queue after merging q1 into q2:", q2.printQueue()) # Output: [2, 3, 4, 6, 5]

# 10. clone
print("=====================================================")
q3 = q1.clone()
print("Cloned queue q3 from q1:", q3.printQueue()) # Output: [2, 3, 4]

# 11. rotate
q1.rotate(1) # number of elements to be rotate
print("Queue after rotating by 1 element on q1:", q1.printQueue())  # Output: [4, 2, 3]

# 12. countOccurrences
print("Count of 3 in q1:", q1.countOccurrences(3))  # Output: 1

# 13. clearElement
print("=====================================================")
q1.enqueue(3)  # Add another 3
print("Queue before clearing element 3 from q1:", q1.printQueue())  # Output: [3, 4, 2, 3]
q1.clearElement(3)
print("Queue after clearing element 3 from q1:", q1.printQueue())  # Output: [4, 2]

# 14. clear
q1.clear()
print("Queue after clearing all elements from q1:", q1.printQueue())  # Output: []

# 15. isFull (Example with max size)
print("=====================================================")
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
print("Is queue q1 full with max size 3?: ", q1.isFull(3))  # Output: True
print("Is queue q1 full with max size 5?: ", q1.isFull(5))  # Output: False
print("=====================================================")