# Sorting Algorithms: Divide and Conquer & Insertion Sort

 ## Description
This repository contains Python implementations of sorting algorithms, including:
1. A divide-and-conquer sorting algorithm (XYZSort).
2. Iterative and recursive versions of the Insertion Sort algorithm.
3. A performance comparison of both insertion sort implementations.

## Question 1: Divide and Conquer Sorting (XYZSort)

### **Correctness**
Yes, XYZSort correctly sorts input arrays.

### **In-Place Sorting**
Yes, XYZSort is in-place because it does not use additional arrays to store values.

### **Time Complexity Recurrence Relation**
T(n) = 2T(n/2) + T(n-1) + c

### **Efficiency**
XYZSort is not efficient. It is slower than traditional sorting algorithms like Insertion Sort and Merge Sort. The function follows an exponential growth pattern.

---

## Question 2: Insertion Sort

### **Implemented Functions**
- **iterative_insertion_sort(arr):** Performs insertion sort iteratively.
- **recursive_insertion_sort(arr):** Performs insertion sort recursively.
- **generate_random_array(size, duplicates):** Generates a random array.
- **print_array(arr):** Displays the generated array.
- **print_results(sorted_arr, comparisons, swaps, time_taken):** Prints sorting metrics.

### **Comparison: Iterative vs. Recursive Insertion Sort**
| Metric            | Iterative Version | Recursive Version |
|------------------|----------------|----------------|
| Comparisons      | Equal          | Equal          |
| Swaps           | Equal          | Equal          |
| Time Complexity | O(n²)          | O(n²)          |
| Performance     | Faster for large inputs | Faster for small inputs |

Recursive insertion sort has additional overhead due to function calls, making it less efficient for larger inputs.

---

## Usage
Run `code.py` and input the desired parameters:

```sh
python code.py
