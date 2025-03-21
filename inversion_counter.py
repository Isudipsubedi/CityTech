"""
Count array inversions using merge sort
Inversion: A pair (i, j) where i < j and arr[i] > arr[j]
"""

def count_inversions(arr):
    """Main function to count total inversions"""
    return _merge_sort(arr)[1]

def _merge_sort(arr):
    """Recursive merge sort with inversion counting"""
    if len(arr) <= 1:
        return arr, 0
    
    mid = len(arr) // 2
    left, left_count = _merge_sort(arr[:mid])
    right, right_count = _merge_sort(arr[mid:])
    merged, merge_count = _merge(left, right)
    
    return merged, left_count + right_count + merge_count

def _merge(left, right):
    """Merge two sorted arrays and count split inversions"""
    merged = []
    i = j = count = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            # All remaining left elements form inversions
            count += len(left) - i
    
    merged += left[i:]
    merged += right[j:]
    return merged, count

if __name__ == "__main__":
    # Verify functionality with sample input
    sample = [1, 20, 6, 4, 5]
    print(f"Sample array: {sample}")
    print(f"Total inversions: {count_inversions(sample)}")  # Output: 5