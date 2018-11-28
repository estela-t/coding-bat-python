
# Coding Bat Python Practice Problems

# Logic-2

#make_bricks
# We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each). Return True if it is possible to make the goal by choosing from the given bricks. 
def make_bricks(small, big, goal):
	sm_needed = goal - (big * 5)
	if small >= sm_needed and goal % 5 <= small:
		return True
	return False

#lone_sum
# Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values, it does not count towards the sum.
def lone_sum(a, b, c):
	if a == b and b == c:
		return 0
	if a == b:
		return c
	if b == c:
		return a
	if a == c:
		return b
	return a + b + c

#lucky_sum
# Given 3 int values, a b c, return their sum. However, if one of the values is 13 then it does not count towards the sum and values to its right do not count.
def lucky_sum(a, b, c):
	if a == 13:
		return 0
	if b == 13:
		return a
	if c == 13:
		return a + b
	else:
		return a + b + c

#no_teen_sum
# Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- in the range 13..19 inclusive -- then that value counts as 0, except 15 and 16 do not count as a teens. 
def no_teen_sum(a, b, c):
	return fix_teen(a) + fix_teen(b) + fix_teen(c)

def fix_teen(n):
	if n in range(13,15) or n in range(17,20):
		return 0
	return n

#close_far
# Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1), while the other is "far", differing from both other values by 2 or more.
def close_far(a, b, c):
	diff_ab = abs(a - b)
	diff_ac = abs(a - c)
	diff_bc = abs(b - c)
	if diff_ab <= diff_ac and diff_ac >= 2 and diff_bc >=2:
		return True
	else:
		return diff_ac <= diff_ab and diff_ab >= 2 and diff_bc >=2
	return False

#make_chocolate
# We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each). Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't be done.
def make_chocolate(small, big, goal):
	b = min(big, goal // 5)
	sm_needed = goal - (b * 5)
	if sm_needed <= small:
		return sm_needed
	return -1

	