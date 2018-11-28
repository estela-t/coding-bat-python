
# Coding Bat Python Practice Problems

# String-2

#double_char
# Given a string, return a string where for every char in the original, there are two chars.
def double_char(str):
	new_str = ""
	for i in range(len(str)):
		new_str = new_str + (str[i] * 2)
	return new_str

#count_hi
# Return the number of times that the string "hi" appears anywhere in the given string.
def count_hi(str):
	count = 0
	for i in range(len(str) - 1):
		if str[i] == "h" and str[i+1] == "i":
			count += 1
	return count

#cat_dog
# Return True if the string "cat" and "dog" appear the same number of times in the given string.
def cat_dog(str):
	dog = 0
	cat = 0
	for i in range(len(str)):
		if str[i:i+3] == "cat":
			cat += 1
		if str[i:i+3] == "dog":
			dog += 1
	return dog == cat

#count_code
# Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.
def count_code(str):
	count = 0
	for i in range(len(str)-3):
		if str[i:i+2] == "co" and str[i+3] == "e":
			count += 1
	return count

#end_other
# Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). 
def end_other(a, b):
	a = a.lower()
	b = b.lower()
	if a.endswith(b) or b.endswith(a):
		return True 
	return False

#