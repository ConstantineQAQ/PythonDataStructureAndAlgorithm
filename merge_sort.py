def sort(arr: list):
    a2 = [0] * len(arr)
    split(arr, 0, len(arr) - 1, a2)


def split(a1: list, left: int, right: int, a2: list):
    if right - left <= 32:
        insertion(a1, left, right)
        return
    mid = (left + right) >> 1
    split(a1, left, mid, a2)
    split(a1, mid + 1, right, a2)
    merge(a1, left, mid, mid + 1, right, a2)
    a1[left:right + 1] = a2[left:right + 1]


def merge(a1: list, i: int, iEnd: int, j: int, jEnd: int, a2: list):
    k = i
    while i <= iEnd and j <= jEnd:
        if a1[i] < a1[j]:
            a2[k] = a1[i]
            i += 1
        else:
            a2[k] = a1[j]
            j += 1
        k += 1
    while i <= iEnd:
        a2[k] = a1[i]
        i += 1
        k += 1
    while j <= jEnd:
        a2[k] = a1[j]
        j += 1
        k += 1


def sort_bottom(arr: list):
    arr_len = len(arr)
    a2 = [0] * arr_len
    width = 1
    while width < arr_len:
        for left in range(0, arr_len, width << 1):
            right = min(left + (width << 1) - 1, arr_len - 1)
            mid = min(left + width - 1, arr_len - 1)
            merge(arr, left, mid, mid + 1, right, a2)
        width <<= 1
        arr[0:arr_len] = a2[0:arr_len]


def insertion(arr: list, left: int, right: int):
    for low in range(left, right + 1):
        temp = arr[low]
        i = low - 1
        while i >= 0 and arr[i] > temp:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = temp


if __name__ == '__main__':
    lst = [6, 5, 4, 3, 2, 1]
    sort(lst)
    print(lst)
