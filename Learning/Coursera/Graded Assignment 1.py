def calculate_frequencies(file_contents):
	# Here is a list of punctuations and uninteresting words you can use to process your text
	punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
	uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
						   "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its",
						   "they", "them", \
						   "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be",
						   "been", "being", \
						   "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when",
						   "where", "how", \
						   "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very",
						   "can", "will", "just"]

	# LEARNER CODE START HERE
	dic = {}
	split_content = file_contents.lower().split()
	for word in split_content:
		if word.isalpha():
			if word in uninteresting_words:
				continue
			if word not in dic:
				dic[word] = 1
			else:
				dic[word] += 1
		else:
			for text in word:
				if text in punctuations:
					word = text.replace(text, "")
					continue

	return dic


print(calculate_frequencies("Thank you so much sir for all the encouraging words. Your kindness will inspire everyone to come forward and help the needy.  Under your guidance millions will find a way to achieve their dreams. Keep inspiring sir. I look forward meeting you soon."))