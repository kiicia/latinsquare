def chars(f,t):
	'''
	>>> chars('1','4')
	['1', '2', '3', '4']
	>>> chars('a','c')
	['a', 'b', 'c']
	'''
	return [chr(i) for i in range(ord(f),ord(t)+1)]

