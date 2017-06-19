from latinsquare import LatinSquare
from alphabet import chars
import random

a = chars('a','z')+chars('0','9')+list('[]{}#%^*+=')
s = LatinSquare(len(a)).dictionary(a)
s.mix(lambda cur,size: random.randint(cur,size-1))
print(s)

