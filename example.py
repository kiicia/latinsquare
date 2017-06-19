from latinsquare import LatinSquare
from alphabet import chars
import random

a = chars('a','z')+chars('0','9')+list('-/:;()$&@".,?!')
s = LatinSquare(len(a)).dictionary(a)
s.mix(lambda cur,size: random.randint(cur,size-1))
print(s)
for i in range(1,10):
	input = 'github.com'+str(i)
	print(input, s.get(input))

