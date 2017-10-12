import re

def is_isogram(phrase):
	phrase = phrase.lower()
	words = re.findall(r'(\w+)', phrase)

	chars = {}
	for w in words:
		for ch in w:
			if chars.has_key(ch):
				return False
			else:
				chars[ch] = True

	return True 
