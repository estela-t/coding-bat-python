
# Coding Bat Python Practice Problems

# Logic-1

#cigar_party
# When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars. Return True if the party with the given values is successful, or False otherwise.
def cigar_party(cigars, is_weekend):
	if (is_weekend and cigars >= 40) or (cigars >= 40 and cigars <= 60):
		return True
	return False

#date_fashion
# You and your date are trying to get a table at a restaurant. The parameter "you" is the stylishness of your clothes, in the range 0..10, and "date" is the stylishness of your date's clothes. The result getting the table is encoded as an int value with 0=no, 1=maybe, 2=yes. If either of you is very stylish, 8 or more, then the result is 2 (yes). With the exception that if either of you has style of 2 or less, then the result is 0 (no). Otherwise the result is 1 (maybe).
def date_fashion(you, date):
	if you <= 2 or date <= 2:
		return 0
	elif you >= 8 or date >= 8:
		return 2
	else:
		return 1

#squirrel_play
# The squirrels in Palo Alto spend most of the day playing. In particular, they play if the temperature is between 60 and 90 (inclusive). Unless it is summer, then the upper limit is 100 instead of 90. Given an int temperature and a boolean is_summer, return True if the squirrels play and False otherwise.
def squirrel_play(temp, is_summer):
	if is_summer:
		return temp in range(60,101)
	else:
		return temp in range(60,91)

#sorta_sum
# Given 2 ints, a and b, return their sum. However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20.
def sorta_sum(a, b):
	if 10 <= (a + b) <= 19:
		return 20
	else:
		return a + b

#love6
# The number 6 is a truly great number. Given two int values, a and b, return True if either one is 6. Or if their sum or difference is 6.
def love6(a, b):
	return a == 6 or b == 6 or (a + b == 6) or (abs(a - b) == 6)

#in1to10
# Given a number n, return True if n is in the range 1..10, inclusive. Unless outside_mode is True, in which case return True if the number is less or equal to 1, or greater or equal to 10.
def in1to10(n, outside_mode):
	if outside_mode and (n <= 1 or n >= 10):
		return True
	else:
		return not outside_mode and n in range(1,11)