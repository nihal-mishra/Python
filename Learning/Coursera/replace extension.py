def pig_latin(text):
	say = ""
	i = 1
	# Separate the text into words
	words = text.split(" ")
	for word in words:
		if i != len(words):
			word = word[1:] + word[0] + 'ay'
			say = say + word + " "
			i += 1
		else:
			word = word[1:] + word[0] + 'ay'
			say = say + word

	return say


print(pig_latin("hello how are you"))  # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun"))  # Should be "rogrammingpay niay ythonpay siay unfay"