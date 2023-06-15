def insert_sort(arr: list):
    arr_len = len(arr)
    for low in range(arr_len):
        temp = arr[low]
        i = low - 1
        while i >= 0 and arr[i] > temp:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = temp


def shell_sort(arr: list):
    gap = len(arr) >> 1
    while gap > 0:
        for low in range(gap, len(arr)):
            temp = arr[low]
            i = low - gap
            while i >= 0 and arr[i] > temp:
                arr[i + gap] = arr[i]
                i -= gap
            arr[i + gap] = temp
        gap >>= 1


def selection_sort(arr: list):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


if __name__ == '__main__':
    arr = [5, 2, 3, 1]
    shell_sort(arr)
    print(arr)
