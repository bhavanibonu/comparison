def binary_search(arr, l, h, x):
    if h >= l:
        m = (h + l) // 2
        if arr[m] == x:
            return m
        elif arr[m] > x:
            return binary_search(arr, l, m - 1, x)
        else:
            return binary_search(arr, m + 1, h, x)
    else:
        return -1
arr = [2,4,10,22,40,48,55,59,63,67,70,75,81,86,90,99]
x = 67

result = binary_search(arr, 0, len(arr) - 1, x)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
#
import time

start = time.time()

a = [1, 2, 3, 4]
print(a)
a.insert(4, 5)
print(a)
a.pop(0)
print(a)
l = len(a)
print(a)

end = time.time()
print(f"Runtime of the program is {end - start} seconds")
