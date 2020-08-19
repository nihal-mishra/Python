def Two_Sum_Sorting(array, target):  # Sorting Method --- Time - O(NlogN), Space - O(1)
	array.sort()
	right = len(array) - 1
	left = 0

	while left < right:
		Sum = array[left] + array[right]
		if Sum == target:
			return [array[left], array[right]]
		elif Sum > target:
			right -= 1
		else:
			left += 1

	return []


def Two_Sum_Hash(array, target):  # Hash Method --- Time - O(N), Space - O(N)
	number_bool = {}
	for element in array:
		Sum = target - element
		if Sum in number_bool:
			return [element, Sum]
		number_bool[element] = True

	return []


print(Two_Sum_Sorting([3, 5, -4, 8, 11, 1, -1, 6], 10))
print(Two_Sum_Hash([3, 5, -4, 8, 11, 1, -1, 6], 10))
