import random
import time

def iterative_insertion_sort(arr):
    comparisons = 0
    swaps = 0
    start_time = time.time()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            comparisons += 1
            arr[j + 1] = arr[j]
            swaps += 1
            j -= 1
        arr[j + 1] = key
    end_time = time.time()
    return comparisons, swaps, end_time - start_time

def recursive_insertion_sort(arr):
    comparisons = [0]  
    swaps = [0]
    start_time = time.time()
    
    def _recursive_insertion_sort(arr, n):
        if n <= 1:
            return
        _recursive_insertion_sort(arr, n-1)
        key = arr[n-1]
        j = n - 2
        while j >= 0 and arr[j] > key:
            comparisons[0] += 1
            arr[j + 1] = arr[j]
            swaps[0] += 1
            j -= 1
        arr[j + 1] = key

    _recursive_insertion_sort(arr, len(arr))
    
    end_time = time.time()
    return comparisons[0], swaps[0], end_time - start_time

def generate_random_array(size, duplicates=True):
    if duplicates:
        return [random.randint(0, size * 10) for _ in range(size)]
    else:
        return random.sample(range(size * 10), size)

def print_array(arr):
    if len(arr) < 10:
        print("Generated Array:", arr)

def print_results(sorted_arr, comparisons, swaps, time_taken):
    if len(sorted_arr) < 10:
        print("Sorted Array:", sorted_arr)
    print("Comparisons:", comparisons)
    print("Swaps:", swaps)
    print("Time Taken:", time_taken, "seconds")

def main():
    size = int(input("Enter the size of the array: "))
    order = input("Enter sorting order (asc/desc): ").lower()
    duplicates = input("Array contains duplicates? (yes/no): ").lower() == 'yes'
    
    arr = generate_random_array(size, duplicates)
    print_array(arr)
    
    if order == 'asc':
        arr_copy = arr.copy()
        comparisons, swaps, time_taken = iterative_insertion_sort(arr_copy)
        print("\nIterative Insertion Sort (Ascending):")
        print_results(arr_copy, comparisons, swaps, time_taken)

        arr_copy = arr.copy()
        comparisons, swaps, time_taken = recursive_insertion_sort(arr_copy)
        print("\nRecursive Insertion Sort (Ascending):")
        print_results(arr_copy, comparisons, swaps, time_taken)
        
    elif order == 'desc':
        arr_copy = arr.copy()
        comparisons, swaps, time_taken = iterative_insertion_sort(arr_copy)
        print("\nIterative Insertion Sort (Descending):")
        print_results(arr_copy[::-1], comparisons, swaps, time_taken)

        arr_copy = arr.copy()
        comparisons, swaps, time_taken = recursive_insertion_sort(arr_copy)
        print("\nRecursive Insertion Sort (Descending):")
        print_results(arr_copy[::-1], comparisons, swaps, time_taken)
    else:
        print("Invalid sorting order. Please enter 'asc' or 'desc'.")

if __name__ == "__main__":
    main()
