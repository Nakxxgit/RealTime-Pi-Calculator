from decimal import *

getcontext().prec = 1000

#arctan(x) = sum (n = 0 to infinity) (-1)^n * (x^(2n+1))/(2n+1)
#So to calculate pi, compute (arctan (1)) = pi/4 = 1 - 1/3 + 1/5 - 1/7 +…
quarterpi = Decimal(0)
n = 0

while True:
    quarterpi = quarterpi + Decimal(-1)**n / (Decimal(2*n + 1))
    if (n % 10000 == 0):
        print(quarterpi*Decimal(4))
        with open('filename','w') as f:
            f.write(str(quarterpi*Decimal(4)))
    n += 1
f.close
