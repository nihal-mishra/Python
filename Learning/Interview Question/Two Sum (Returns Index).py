def twoSum(array, target):
	number_index = {}
	i = 0
	for element in array:
		temp = target - element
		if temp in number_index:
			return [i, number_index[temp]]
		number_index[element] = i
		i += 1

	return []


tar = input("Enter the sum target : ")
print(twoSum([2, 5, 9, 10, 11], int(tar)))
