def merge_sort(arr):
    # Base case: an array with one element is already sorted
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])  # Left half
    right = merge_sort(arr[mid:])  # Right half

    # Merge the two sorted halves
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    # Merge both sorted arrays
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add the remaining elements from either left or right
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Example with a small array
arr = [4, 2, 7, 1, 3]
sorted_arr = merge_sort(arr)
print(sorted_arr)

"""
Logarithmic o(log n): Shrinks the problem size by dividing it (e.g., halving).
Linear o(n): Processes all elements of the input once.
Log-linear O(nlogn): Combines these two—process the input (n) while repeatedly reducing the problem size (log n)

used where dividing and conquering is involved.
"""