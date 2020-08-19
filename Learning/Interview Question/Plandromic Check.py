def plandromic_check(string):
	right = len(string)-1
	left = 0
	lenBy2 = len(string)/2

	for i in range(int(lenBy2)):
		if string[left] == string[right]:
			left += 1
			right -= 1
		else:
			return False

	return True


if plandromic_check("ABCDnDCBA"):
	print("String is Plandromic")
else:
	print("String is not Plandromic")