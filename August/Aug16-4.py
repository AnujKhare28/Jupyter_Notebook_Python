class Angle:
    def __init__(self, deg):
        self.deg = deg

    def __add__(self, ang):
        Sum = Angle(self.deg + ang.deg)
        return Sum
    
    def __str__(self):
        return 'Degree' + str(self.deg)
    
a1 = Angle(30)
a2 = Angle(45)
a3 = a1 + a2
print(a3)