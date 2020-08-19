def Three_Number_Sum(numbers, target):
	result_lists = []
	numbers.sort()
	for i in range(len(numbers)):
		left = i + 1
		right = len(numbers) - 1
		current_num = numbers[i]

		while left < right:
			current_sum = current_num + numbers[left] + numbers[right]
			if current_sum == target:
				left += 1
				right -= 1
				result_lists.append([current_num, numbers[left], numbers[right]])
			elif current_sum > target:
				right -= 1
			elif current_sum < target:
				left += 1

	return result_lists


numbers = [12, 3, 1, 2, -6, 5, -8, 6]
target = 0
print(Three_Number_Sum(numbers, target))