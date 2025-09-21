class Rational:
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __add__(self, other):
        p = self.p * other.q + self.q * other.p
        q = self.q * other.q
        addn = Rational(p,q)
        return addn
    
    def __sub__(self, other):
        p = self.p * other.q - self.q * other.p
        q = self.q * other.q
        subtract = Rational(p,q)
        return subtract
    
    def __str__(self):
        return str(self.p) + '/' + str(self.q)
    
r1 = Rational(2,3)
r2 = Rational(1,2)
r3 = r1 + r2
print(r1, '+', r2, '=', r3)