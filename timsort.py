import time

MIN_MERGE = 16

def calcMinRun(n):
	r = 0
	while n >= MIN_MERGE:
		r |= n & 1
		n >>= 1
	return n + r


# This function sorts array from left index to
# to right index which is of size atmost RUN
def insertionSort(data, drawdata, timeTick, left, right):
	for i in range(left + 1, right + 1):
		j = i
		while j > left and data[j] < data[j - 1]:
			data[j], data[j - 1] = data[j - 1], data[j]
			drawdata(data,['yellow' if x<j else "#A90042" for x in range(len(data)) ])
			j -= 1
			time.sleep(timeTick)


# Merge function merges the sorted runs
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


# Iterative Timsort function to sort the
# array[0...n-1] (similar to merge sort)
def timSort(data, drawData, timeTick):
	n = len(data)
	minRun = calcMinRun(n)
	
	# Sort individual subarrays of size RUN
	for start in range(0, n, minRun):
		end = min(start + minRun - 1, n - 1)
		insertionSort(data, drawData, timeTick, start, end)

	# Start merging from size RUN (or 32). It will merge
	# to form size 64, then 128, 256 and so on ....
	size = minRun
	while size < n:
		
		# Pick starting point of left sub array. We
		# are going to merge arr[left..left+size-1]
		# and arr[left+size, left+2*size-1]
		# After every merge, we increase left by 2*size
		for left in range(0, n, 2 * size):

			# Find ending point of left sub array
			# mid+1 is starting point of right sub array
			mid = min(n - 1, left + size - 1)
			right = min((left + 2 * size - 1), (n - 1))

			# Merge sub array arr[left.....mid] &
			# arr[mid+1....right]
			if mid < right:
				merge(data, left, mid, right, drawData, timeTick)

		size = 2 * size

def timSort_algorithm(data, drawData, timeTick):
	start = time.time()
	timSort(data, drawData, timeTick)
	elapsed_time_fl = (time.time() - start)
	return round(elapsed_time_fl,2)



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


# Driver program to test above function
# if __name__ == "__main__":

# 	arr = [-2, 7, 15, -14, 0, 15, 0,
# 		7, -7, -4, -13, 5, 8, -14, 12]

# 	print("Given Array is")
# 	print(arr)

# 	# Function Call
# 	timSort(arr)

# 	print("After Sorting Array is")
# 	print(arr)
# 	# [-14, -14, -13, -7, -4, -2, 0, 0, 5, 7, 7, 8, 12, 15, 15]
