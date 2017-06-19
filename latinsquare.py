class LatinSquare():
	
	def __init__(self,side):
		'''
		>>> s = LatinSquare(3)
		>>> s.side
		3
		>>> s.dic
		
		>>> s.arr
		[[0, 1, 2], [1, 2, 0], [2, 0, 1]]
		'''
		self.side = side
		self.dic = None
		self._generate()
	
	def last(self,col):
		'''
		>>> s = LatinSquare(3)
		>>> s.last(1)
		False
		>>> s.last(2)
		True
		'''
		return col == self.side-1
	
	def __str__(self):
		'''
		>>> s = LatinSquare(3)
		>>> s.__str__()
		'012\\n120\\n201\\n'
		>>> s.dictionary(['a','b','c']).__str__()
		'abc\\nbca\\ncab\\n'
		'''
		s = ''
		for row in range(self.side):
			for col in range(self.side):
				s += self.value(row,col)
				if self.last(col):
					s += '\n'
		return s
	
	def _generate(self):
		self.arr = [[(row+col)%self.side for col in range(self.side)] for row in range(self.side)]
	
	def dictionary(self,dic):
		'''
		>>> s = LatinSquare(3).dictionary(['a','b','c'])
		>>> s.dic
		['a', 'b', 'c']
		'''
		self.dic = dic
		return self
	
	def value(self,row,col):
		'''
		>>> s = LatinSquare(3)
		>>> s.value(1,1)
		'2'
		>>> s.value(0,0)
		'0'
		>>> s = LatinSquare(3).dictionary(['a','b','c'])
		>>> s.value(1,1)
		'c'
		>>> s.value(0,0)
		'a'
		'''
		val = self.arr[row][col]
		return str(val) if not self.dic else self.dic[val]
	
	def swap_rows(self,row1,row2):
		'''
		>>> s = LatinSquare(3)
		>>> s.swap_rows(0,1)
		>>> s.__str__()
		'120\\n012\\n201\\n'
		'''
		self.arr[row1],self.arr[row2] = self.arr[row2],self.arr[row1]
	
	def swap_cols(self,col1,col2):
		'''
		>>> s = LatinSquare(3)
		>>> s.swap_cols(0,1)
		>>> s.__str__()
		'102\\n210\\n021\\n'
		'''
		for row in range(self.side):
			self.arr[row][col1],self.arr[row][col2] = self.arr[row][col2],self.arr[row][col1]
	
	def swap_vals(self,v1,v2):
		'''
		>>> s = LatinSquare(3)
		>>> s.swap_vals(0,1)
		>>> s.__str__()
		'102\\n021\\n210\\n'
		'''
		for (row,col) in [(row,col) for row in range(self.side) for col in range(self.side)]:
			cur = self.arr[row][col]
			self.arr[row][col] = v1 if cur == v2 else v2 if cur == v1 else cur
