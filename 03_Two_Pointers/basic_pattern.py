arr = [1, 2, 3, 4, 5]
left = 0
right = len(arr) - 1

while left < right:
    print(arr[left], arr[right])

    left += 1
    right -= 1