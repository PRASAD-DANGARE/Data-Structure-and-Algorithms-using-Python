class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if not self.isEmpty() else None

    def peek(self):
        return self.items[-1] if not self.isEmpty() else None

    def size(self):
        return len(self.items)

    def clear(self):
        self.items = []

    def search(self, item):
        return item in self.items

    def PrintStack(self):
        return self.items[:]

    def reverse(self):
        self.items.reverse()

    def clone(self):
        new_stack = Stack()
        new_stack.items = self.items[:]
        return new_stack

    def countOccurrences(self, item):
        return self.items.count(item)

    def sort(self, reverse=False):
        self.items.sort(reverse=reverse)

    def merge(self, another_stack):
        self.items.extend(another_stack.items)

    def rotate(self, k):
        if k > 0:
            k = k % len(self.items)  # Ensure k doesn't exceed stack size
            self.items = self.items[-k:] + self.items[:-k]

    def minElement(self):
        return min(self.items) if self.items else None

    def maxElement(self):
        return max(self.items) if self.items else None

    def sum(self):
        return sum(self.items) if all(isinstance(i, (int, float)) for i in self.items) else None


# Demonstration of all operations
s = Stack()

# 1. Stack push operation
print("=====================================================")
print("Is stack empty?:", s.isEmpty()) # Output: True
s.push(1)
s.push(2)
s.push(3)
s.push(4)
print("Stack after push operation:", s.PrintStack()) # Output: [1, 2, 3, 4]
print("Peek element:", s.peek()) # Output: 4
print("Stack size:", s.size()) # Output: 4

# 2 Stack pop operation
print("=====================================================")
print("Stack before pop operation:", s.PrintStack()) # Output: [1, 2, 3, 4]
print("Pop element:", s.pop()) # Output: 4
print("Stack after pop operation:", s.PrintStack()) # Output: [1, 2, 3]
print("Stack size:", s.size()) # Output: 3

# 3. Clear the stack
print("=====================================================")
print("Stack before clear operation:", s.PrintStack()) # Output: [1, 2, 3]
s.clear()
print("Stack after clear operation:", s.PrintStack()) # Output: []
print("Stack size:", s.size()) # Output: 0
print("Is stack empty?:", s.isEmpty()) # Output: True

# 4. Search and reverse
print("=====================================================")
s.push(5)
s.push(6)
s.push(7)
print("Is stack empty?:", s.isEmpty()) # Output: False
print("Stack elements:", s.PrintStack()) # Output: [5, 6, 7]
print("Search 6 in stack:", s.search(6)) # Output: True
s.reverse()
print("Stack after reverse:", s.PrintStack()) # Output: [7, 6, 5]

# 5. Clone and merge
print("=====================================================")
cloned_stack = s.clone()
print("Cloned stack:", cloned_stack.PrintStack()) # Output: [7, 6, 5]
s2 = Stack()
s2.push(8)
s2.push(9)
print("Stack 1 elements:", s.PrintStack()) # Output: [7, 6, 5]
print("Stack 2 elements:", s2.PrintStack()) # Output: [8, 9]
s.merge(s2)
print("Stack after merging s1 and s2:", s.PrintStack()) # Output: [7, 6, 5, 8, 9]
print("Stack size:", s.size()) # Output: 5

# 6. Rotate
print("=====================================================")
print("Stack before rotating:", s.PrintStack()) # Output: [7, 6, 5, 8, 9]
s.rotate(2)
print("Stack after rotating by 2:", s.PrintStack()) # Output: [8, 9, 7, 6, 5]

# 7. Count occurrences
print("=====================================================")
s.push(7)
print("Original stack:", s.PrintStack()) # Output: [8, 9, 7, 6, 5]
print("Count of 7:", s.countOccurrences(7)) # Output: 2
print("Count of 2:", s.countOccurrences(2)) # Output: 0

# 8. Sort
print("=====================================================")
print("Stack before sorting:", s.PrintStack()) # Output: [8, 9, 7, 6, 5, 7]
s.sort()
print("Stack after sorting:", s.PrintStack()) # Output: [5, 6, 7, 7, 8, 9]

# 9. Min, Max, and Sum
print("=====================================================")
print("Original stack:", s.PrintStack()) # Output: [5, 6, 7, 7, 8, 9]
print("Minimum element:", s.minElement()) # Output: 5
print("Maximum element:", s.maxElement()) # Output: 9
print("Sum of elements:", s.sum()) # Output: 42
print("=====================================================")