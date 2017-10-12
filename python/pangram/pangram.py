import string

def is_pangram(text):
	for ch in string.ascii_lowercase:
		if ch not in text and chr(ord('A') + ord(ch) - ord('a')) not in text:
			return False

	return True
