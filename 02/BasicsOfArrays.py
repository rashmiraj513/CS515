import numpy as np

# Sum of Two Arrays
array_1 = np.array([23, 12, 22, -9, 87])
array_2 = np.array([45, 43, 12, 11, 98])
ans = array_1 + array_2
print(ans)

# Reverse the array elements
arr = [23, 12, 22, -9, 87, -12]
size = len(arr)
print("The original array is: {}.".format(arr))
# # Reverse the array by using two pointers approach with while loop
start, end = 0, size - 1
while(start < end):
    temp = arr[start]
    arr[start] = arr[end]
    arr[end] = temp
    start += 1
    end -= 1
print("The array after reversal is: {}.".format(arr))

# Reverse the array by using two pointers approach with for loop
for i in range(size // 2):
    temp = arr[i]
    arr[i] = arr[size - i - 1]
    arr[size - i - 1] = temp
print("The array after reversal is: {}.".format(arr))