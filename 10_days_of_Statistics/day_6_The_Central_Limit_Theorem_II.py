# Enter your code here. Read input from STDIN. Print output to STDOUT

import math


def central_limit(x, u, o):
    return round(0.5*(1+math.erf((x-u)/(o*(2**0.5)))), 4)


print(central_limit(250, 100*2.4, (100**0.5)*2.0))
