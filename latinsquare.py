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
		for (row,col) in [(row,col) for row in range(self.side) for col in range(self.side)]:
			s += self.value(row,col)
			s += '\n' if self.last(col) else ''
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
	
	def mix(self,rand):
		for i in range(self.side):
			self.swap_cols(i,rand(i,self.side))
			self.swap_rows(i,rand(i,self.side))
			self.swap_vals(i,rand(i,self.side))
	
	def _reset(self):
		'''
		>>> s = LatinSquare(3)
		>>> s._reset()
		>>> s.row
		0
		>>> s.col
		0
		>>> s.prev
		
		>>> s.last_c
		
		>>> s.by_row
		False
		'''
		self.row = 0
		self.col = 0
		self.prev = None
		self.last_c = None
		self.by_row = False
	
	def find_in_row(self,c):
		'''
		>>> s = LatinSquare(3).dictionary(['a','b','c'])
		>>> s._reset()
		>>> s.find_in_row('c')
		2
		'''
		for i in range(self.side):
			if self.value(self.row,i) == c:
				return i
	
	def find_in_col(self,c):
		'''
		>>> s = LatinSquare(3).dictionary(['a','b','c'])
		>>> s._reset()
		>>> s.find_in_col('b')
		1
		'''
		for i in range(self.side):
			if self.value(i,self.col) == c:
				return i
	
	def vector(self):
		'''
		>>> s = LatinSquare(3)
		>>> s._reset()
		>>> s.by_row = True
		>>> s.prev = 1
		>>> s.col = 2
		>>> s.vector()
		0
		>>> s.by_row = False
		>>> s.prev = 1
		>>> s.row = 0
		>>> s.vector()
		2
		'''
		cur = self.col if self.by_row else self.row
		return ((1 if cur > self.prev else -1) + cur)%self.side
	
	def get(self,text):
		'''
		# a b c
		# c a b
		# b c a
		>>> s = LatinSquare(3).dictionary(['a','b','c'])
		>>> s.swap_rows(1,2)
		>>> s.__str__()
		'abc\\ncab\\nbca\\n'
		>>> s.get('cbaa')
		'bccc'
		'''
		return self._get_raw(text)[len(text):]
	
	def _get_raw(self,text):
		'''
		# a b c
		# c a b
		# b c a
		>>> s = LatinSquare(3).dictionary(['a','b','c'])
		>>> s.swap_rows(1,2)
		>>> s.__str__()
		'abc\\ncab\\nbca\\n'
		>>> s._get_raw('cbaa')
		'aaccbccc'
		'''
		self._reset()
		result = ''
		for c in text+text:
			result += self._get(c)
		return result
	
	def _get(self,c):
		'''
		# a b c
		# c a b
		# b c a
		>>> s = LatinSquare(3).dictionary(['a','b','c'])
		>>> s.swap_rows(1,2)
		>>> s.__str__()
		'abc\\ncab\\nbca\\n'
		>>> s._reset()
		>>> s.last_c
		
		#(a)b<c>
		# c a b
		# b c a
		>>> s._get('c')
		'a'
		>>> s.by_row
		True
		>>> s.row
		0
		>>> s.col
		2
		>>> s.prev
		0
		>>> s.last_c
		'c'
		
		# a b (c)
		# c a <b>
		# b c a
		>>> s._get('b')
		'a'
		>>> s.by_row
		False
		>>> s.row
		1
		>>> s.col
		2
		>>> s.prev
		0
		>>> s.last_c
		'b'
		
		# a b c
		# c<a>b)
		# b c a
		>>> s._get('a')
		'c'
		>>> s.by_row
		True
		>>> s.row
		1
		>>> s.col
		1
		>>> s.prev
		2
		>>> s.last_c
		'a'
		
		# a b c
		# c(a)b
		# b c<a>
		>>> s._get('a')
		'c'
		>>> s.by_row
		False
		>>> s.row
		2
		>>> s.col
		2
		>>> s.prev
		1
		>>> s.last_c
		'a'
		'''
		self.by_row ^= True
		same,self.last_c = 1 if self.last_c == c else 0,c
		if self.by_row:
			self.row = (same+self.row)%self.side
			self.prev,self.col = self.col,self.find_in_row(c)
			return self.value(self.row,self.vector())
		else:
			self.col = (same+self.col)%self.side
			self.prev,self.row = self.row,self.find_in_col(c)
			return self.value(self.vector(),self.col)
	
