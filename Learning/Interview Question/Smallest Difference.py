def Smallest_Difference(nums1, nums2):
	nums1.sort()
	nums2.sort()
	lowest_difference = float('inf')
	pointer1 = pointer2 = 0
	difference1 = difference2 = float('inf')
	while pointer1 < len(nums1) and pointer2 < len(nums2):
		current_difference = abs(nums1[pointer1] - nums2[pointer2])
		if current_difference < lowest_difference:
			lowest_difference = current_difference
			difference1 = nums1[pointer1]
			difference2 = nums2[pointer2]

		if nums1[pointer1] == nums2[pointer2]:
			return nums1[pointer1], nums2[pointer2]
		else:
			if nums1[pointer1] < nums2[pointer2]:
				pointer1 += 1
			elif nums1[pointer1] > nums2[pointer2]:
				pointer2 += 1

	return difference1, difference2


d1, d2 = Smallest_Difference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17])
print(f"\n1st -> {d1}\n2nd -> {d2}\nDifference -> {abs(d1-d2)}\n")
