'''Check if a series of arrays are symmetric'''


def is_symmetric(arr):
    mid = int(len(arr) / 2)

    for k in range(mid):
        if not arr[k] == arr[-k-1]:
            return 'No'

    return 'Yes'


number_of_arrays = int(input())

for _ in range(number_of_arrays):
    curr_arr = input().split()

    print(is_symmetric(curr_arr))
