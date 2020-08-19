def ThreeLargestNumbers(nums):
	largest = float('-inf')
	second_largest = float('-inf')
	third_largest = float('-inf')

	for element in nums:
		if element > largest:
			largest = element

	for element in nums:
		if largest > element > second_largest:
			second_largest = element

	for element in nums:
		if second_largest > element > third_largest:
			third_largest = element

	return third_largest, second_largest, largest


print(ThreeLargestNumbers([141, 1, 7, 17, -7, -17, 27, 18, 541, 8, 7]))
