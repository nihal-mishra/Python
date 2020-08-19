def initials(full_form):
	words = full_form.split()
	result = ""
	for word in words:
		result += word[0].upper()
	return result


print(initials("Universal Serial Bus"))
print(initials("central processing unit"))
print(initials("local area NETWORK"))
print(initials("OPERATING SYSTEM"))