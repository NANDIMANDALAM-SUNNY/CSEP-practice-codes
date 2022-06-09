arr =[]
n = int(input("Enter the number of elements in the array: "))
for i in range(n):
    arr.append(int(input("Enter element: ")))
arr.sort()
searchElement = int(input("Enter the element to be searched: "))
def binarySearch(arr, searchElement, start, end):
    if end >= start:
        mid = start + (end - start)//2
        if arr[mid] == searchElement:
            return mid
        elif arr[mid] > searchElement:
            return binarySearch(arr, searchElement, start, mid-1)
        else:
            return binarySearch(arr, searchElement, mid + 1, end)
    else:
        return -1
result = binarySearch(arr, searchElement, 0, len(arr)-1)
if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")