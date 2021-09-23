def peak_finding_1d(ar: list[int], start: int, end: int) -> int:
    middle = (start + end) // 2
    if (middle == 0 or ar[middle] >= ar[middle - 1]) and (middle == end or ar[middle] >= ar[middle + 1]):
        return middle
    elif ar[middle - 1] >= ar[middle]:
        return peak_finding_1d(ar, start, middle - 1)
    else:
        return peak_finding_1d(ar, middle + 1, end)


def peak_finding_2d(ar: list[list[int]], m: int, s: int, e: int):
    i = 0  # row iterator
    j = (s + e) // 2  # column iterator
    global_max_row = 0

    for i in range(m):
        if ar[global_max_row][j] <= ar[i][j]:
            global_max_row = i

    if (j == s or ar[global_max_row][j] >= ar[global_max_row][j - 1]) \
            and (j == e or ar[global_max_row][j] >= ar[global_max_row][j + 1]):
        return global_max_row, j
    elif ar[global_max_row][j] <= ar[global_max_row][j - 1]:
        return peak_finding_2d(ar, m, s, j - 1)

    else:
        return peak_finding_2d(ar, m, j + 1, e)


def intersect(nums1, nums2):
    if len(nums2) > len(nums1):
        nums1, nums2 = nums2, nums1
    nums1.sort()
    nums2.sort()
    i = 0
    j = 0
    a = []
    while i < len(nums1):
        if nums1[i] == nums2[j]:
            a.append(nums1[i])
            j += 1
        i += 1
    return a
