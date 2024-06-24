```markdown
# Usage Guide

Here is how you can use the sorting algorithms from this package.

## Example Usage

```python
from sorting_algorithms import bubble_sort, insertion_sort, merge_sort, quick_sort, selection_sort, radix_sort

arr = [64, 34, 25, 12, 22, 11, 90]

print("Bubble Sort:", bubble_sort(arr.copy()))
print("Insertion Sort:", insertion_sort(arr.copy()))
print("Merge Sort:", merge_sort(arr))