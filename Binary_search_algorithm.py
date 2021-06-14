def binary_search(array, start, end, var):
    if start<=end:
        mid = (start+end)//2
        if array[mid]==var:
            return mid
        elif array[mid]>var:
            return binary_search(array, start, mid, var)
        else:
            return binary_search(array, mid, end, var)
    else:
        return -1


input_array = input('Enter the array: ')
array_0 = input_array.split(' ')
array = []
for element in array_0:
    array.append(int(element))
var = int(input('Enter the number to find: '))
array.sort()
print('Sorted Array:')
print(array)
result = binary_search(array, 0, len(array)-1, var)

if result != -1:
    print(f"Element is present in the array at index {result}")
else:
    print("Element is not present in array")
