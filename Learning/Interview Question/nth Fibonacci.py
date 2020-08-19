def fibonacci(target):
	first = 0
	second = 1

	for i in range(target):
		new = first + second
		first, second = second, new

	return second


print(fibonacci(10))