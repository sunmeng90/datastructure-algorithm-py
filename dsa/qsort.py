def qsort(arr):
    if not arr:
        return []
    elif len(arr) == 1:
        return arr
    left = []
    right = []
    for num in arr[1:]:
        if num <= arr[0]:
            left.append(num)
        else:
            right.append(num)
    return qsort(left) + [arr[0]] + qsort(right)


if __name__ == '__main__':
    print('hello')
