def swap(a, b, arr):
    arr[a], arr[b] = arr[b], arr[a]


def partitions(num, start, end):
    pivot_index = start
    pivot = num[pivot_index]

    while start < end:
        while start < len(num) and num[start] <= pivot:
            start += 1

        while num[end] > pivot:
            end -= 1
        if start < end:
            swap(start, end, num)
    swap(pivot_index, end, num)

    return end

def quick_sort(num, start, end):
    if start < end:
        p = partitions(num, start, end)
        quick_sort(num, start, p-1)
        quick_sort(num, p+1, end)
        return num


if __name__ == '__main__':
    numbers = [11, 9, 29, 7, 2, 15, 28]
    print(quick_sort(numbers, 0, len(numbers) - 1))
