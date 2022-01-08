import time


def merge_sort(data, drawData, timeTick):
    start = time.time()
    merge_sort_algorithm(data, 0, len(data) - 1, drawData, timeTick)
    elapsed_time_fl = (time.time() - start)
    return round(elapsed_time_fl, 2)

def merge_sort_algorithm(data, left, right, drawData, timeTick):

    if left < right:
        middle = (left + right) // 2
        merge_sort_algorithm(data, left, middle, drawData, timeTick)
        merge_sort_algorithm(data, middle + 1, right, drawData, timeTick)
        merge(data, left, middle, right, drawData, timeTick)


def merge(data, left, middle, right, drawData, timeTick):
    drawData(data, colors(len(data), left, middle, right))
    time.sleep(timeTick)

    left_side = data[left:middle + 1]
    right_side = data[middle + 1: right + 1]

    leftIdx = rightIdx = 0

    for dataIdx in range(left, right + 1):
        if leftIdx < len(left_side) and rightIdx < len(right_side):
            if left_side[leftIdx] <= right_side[rightIdx]:
                data[dataIdx] = left_side[leftIdx]
                leftIdx += 1
            else:
                data[dataIdx] = right_side[rightIdx]
                rightIdx += 1

        elif leftIdx < len(left_side):
            data[dataIdx] = left_side[leftIdx]
            leftIdx += 1
        else:
            data[dataIdx] = right_side[rightIdx]
            rightIdx += 1

    drawData(data, ["green" if x >= left and x <= right else "#FFFFF0" for x in range(len(data))])
    time.sleep(timeTick)


def colors(length, left, middle, right):
    colors_list = []

    for i in range(length):
        if i >= left and i <= right:
            if i >= left and i <= middle:
                colors_list.append("#FFD700")
            else:
                colors_list.append("#FF1493")
        else:
            colors_list.append("#FFFFF0")

    return colors_list