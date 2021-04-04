print(f"Hello World!")

from eulerlib.operations import *

def len_hypotenuse(a, b):
	""" Returns the (int) length of the hypotenuse """
	c2 = (a**2) + (b**2)
	c = int(c2**(1/2))
	return c

def perimeter(a,b):
	""" Returns perimeter of right triangle with sides a and b """
	return a + b + len_hypotenuse(a,b)

def candidate_list(p):
	""" Returns list of integer right triangle solutions [a,b] such that a <= b <= p """
	solution = []
	for a in range(1, p):
		for b in range(a, p):
			if is_perfect_square((a**2) + (b**2)):
				print(f"a = {a} and b = {b} is a candidate")
				solution.append([a, b])
	return solution


p = 500
candidate_list = candidate_list(p)
perimeter_list = []

for candidate in candidate_list:
	perimeter_list.append(perimeter(candidate[0], candidate[1]))

print(perimeter_list)

occurences = 1
answer = 0

for perimeter in perimeter_list:
	if perimeter_list.count(perimeter) > occurences:
		occurences = perimeter_list.count(perimeter)
		answer = perimeter

print(f"Answer = {answer} as it occurs {occurences} times")


# print(is_perfect_square(40))