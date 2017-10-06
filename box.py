
def space(string):
	return ' '.join(string)

def rotate(string, i):
	return string[i:] + string [:i]

def box(string):
	for i in range(len(string)):
		print(space(rotate(string, i)))
