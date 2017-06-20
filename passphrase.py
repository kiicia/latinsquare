class Passphrase():
	
	def __init__(self,p,d):
		self.p = p
		self.i = -1
		self.d = d
	
	def roll_one(self,x,y):
		self.i = (self.i+1)%len(self.p)
		return self.d.index(self.p[self.i])
	
	def gen_lambda(self):
		'''
		>>> p = Passphrase('aab',['a','b','c'])
		>>> l = p.gen_lambda()
		>>> l(None,None)
		0
		>>> p.i
		0
		>>> l(None,None)
		0
		>>> p.i
		1
		>>> l(None,None)
		1
		>>> p.i
		2
		>>> l(None,None)
		0
		>>> p.i
		0
		'''
		return lambda x,y: self.roll_one(x,y)

