def _quick(arr: list, left: int, right: int):
    if left >= right:
        return
    p = partition(arr, left, right)
    _quick(arr, left, p - 1)
    _quick(arr, p + 1, right)


def partition(a: list, left: int, right: int) -> int:
    pv = a[left]
    i = left
    j = right
    while i < j:
        while i < j and a[j] >= pv:
            j -= 1
        while i < j and a[i] <= pv:
            i += 1
        a[i], a[j] = a[j], a[i]
    a[left], a[i] = a[i], a[left]
    return i


def quick_sort(arr: list):
    _quick(arr, 0, len(arr) - 1)


if __name__ == '__main__':
    arr = [6, 5, 4, 3, 2, 1]
    quick_sort(arr)
    print(arr)
