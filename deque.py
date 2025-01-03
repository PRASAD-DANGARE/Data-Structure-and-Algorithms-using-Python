class Deque(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop() if not self.isEmpty() else None

    def removeRear(self):
        return self.items.pop(0) if not self.isEmpty() else None

    def peekFront(self):
        return self.items[-1] if not self.isEmpty() else None

    def peekRear(self):
        return self.items[0] if not self.isEmpty() else None

    def size(self):
        return len(self.items)

    def clear(self):
        self.items = []

    def rotate(self, k):
        k = k % len(self.items) if self.items else 0
        self.items = self.items[-k:] + self.items[:-k]

    def countOccurrences(self, item):
        return self.items.count(item)

    def contains(self, item):
        return item in self.items

    def printDeque(self):
        return self.items[:]

    def reverse(self):
        self.items.reverse()

    def merge(self, anotherDeque):
        self.items.extend(anotherDeque.items)

    def removeItem(self, item):
        if item in self.items:
            self.items.remove(item)


# Create deque and demonstrate all functions
d = Deque()

# 1. Basic add and remove operations
print("=====================================================")
d.addFront(10)
d.addRear(20)
d.addFront(30)
d.addRear(40)
print("Adding Deque contents:", d.printDeque()) # Output: [40, 20, 10, 30]

# 2. Size and emptiness check
print("Size of deque:", d.size()) # Output: 4
print("Is deque empty?:", d.isEmpty()) # Output: False

# 3. Peek front and rear
print("Front element:", d.peekFront()) # Output: 30
print("Rear element:", d.peekRear()) # Output: 40

# 4. Remove front and rear
print("=====================================================")
print("Before removing front:", d.printDeque()) # Output: [40, 20, 10, 30]
d.removeFront()
print("After removing front:", d.printDeque()) # Output: [40, 20, 10]
print("Before removing rear:", d.printDeque()) # Output: [40, 20, 10]
d.removeRear()
print("After removing rear:", d.printDeque()) # Output: [20, 10]

# 5. Clear the deque
d.clear()
print("Deque after clearing:", d.printDeque()) # Output: []
print("Is deque empty?:", d.isEmpty()) # Output: True
print("Size of deque:", d.size()) # Output: 0

# 6. Add elements for further operations
print("=====================================================")
d.addFront(50)
d.addRear(60)
d.addFront(70)
d.addRear(70)
d.addRear(80)
print("Deque contents:", d.printDeque()) # Output: [80, 70, 60, 50, 70]

# 7. Rotate the deque
d.rotate(2)
print("After rotating right by 2:", d.printDeque()) # Output: [50, 70, 80, 70, 60]

# 8. Reverse the deque
d.reverse()
print("After reversing:", d.printDeque()) # Output: [60, 70, 80, 70, 50]

# 9. Count occurrences
print("Occurrences of 70:", d.countOccurrences(70)) # Output: 2
print("Occurrences of 10:", d.countOccurrences(10)) # Output: 0

# 10. Check if an element exists
print("Does 80 exist in deque?:", d.contains(80)) # Output: True

# 11. Remove a specific item
print("=====================================================")
print("Before removing 70:", d.printDeque()) # Output: [60, 70, 80, 70, 50]
d.removeItem(70)
print("After removing 70:", d.printDeque()) # Output: [60, 80, 70, 50]

# 12. Merge another deque
d2 = Deque()
d2.addFront(90)
d2.addRear(100)
print("d1 contents:", d.printDeque()) # Output: [60, 80, 70, 50]
print("d2 contents:", d2.printDeque()) # Output: [100, 90]
d.merge(d2)
print("After merging d1 and d2:", d.printDeque()) # Output: [60, 80, 50, 70, 100, 90]
print("=====================================================")