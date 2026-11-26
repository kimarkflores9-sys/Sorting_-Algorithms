# Assessment 3.7: Sorting Algorithms
# Sorting method: Bubble Sort

full_name = "kimark flores"

# 1. Build the unsorted array (letters only, no duplicates)
unsorted_array = []
for ch in full_name.lower():
    if ch.isalpha() and ch not in unsorted_array:
        unsorted_array.append(ch)

# 2. Copy the array, then sort the copy using Bubble Sort
sorted_array = unsorted_array.copy()
n = len(sorted_array)

for i in range(n - 1):
    for j in range(n - 1 - i):
        if sorted_array[j] > sorted_array[j + 1]:
            sorted_array[j], sorted_array[j + 1] = sorted_array[j + 1], sorted_array[j]

# 3. Display both arrays
print("Full Name:", full_name)
print("Unsorted array:", unsorted_array)
print("Sorted array:  ", sorted_array)