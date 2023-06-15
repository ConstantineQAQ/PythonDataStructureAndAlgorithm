def bubble_sort(arr: list):
    arr_len = len(arr)
    for i in range(arr_len - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def _bubble_sort(arr: list, n: int):
    if n == 0:
        return
    x = 0
    for i in range(n):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            x = i
    _bubble_sort(arr, x)
    return arr


def bubble_sort2(arr: list):
    if len(arr) < 2:
        return arr
    return _bubble_sort(arr, len(arr) - 1)


if __name__ == '__main__':
    arr = [0]
    print(bubble_sort2(arr))
