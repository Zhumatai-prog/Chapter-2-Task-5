students = []
def number_of_students(a, b, c):
	if a % 2 == 1:
		a = a + 1
	if b % 2 == 1:
		b = b + 1
	if c % 2 == 1:
		c = c + 1

	return(int(a/2), int(b/2), int(c/2))

print(number_of_students(20,21,22))