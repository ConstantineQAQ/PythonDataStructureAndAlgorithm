# InsertSort
def insert_sort(arr: list):
    _insert_sort(arr, 0)


def _insert_sort(arr: list, n: int):
    if n == len(arr):
        return
    temp = arr[n]
    i = n - 1
    while i >= 0 and arr[i] > temp:
        arr[i + 1] = arr[i]
        i -= 1
    arr[i + 1] = temp
    _insert_sort(arr, n + 1)


def insertion(arr: list):
    arr_len = len(arr)
    for low in range(arr_len):
        temp = arr[low]
        i = low - 1
        while i >= 0 and arr[i] > temp:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = temp


if __name__ == '__main__':
    arr = [19, 2, 3, 4, 0, 87, 12, 22, 8, 9]
    insertion(arr)
    print(arr)
