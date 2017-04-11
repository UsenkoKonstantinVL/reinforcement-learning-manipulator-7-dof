

class PID:
    def __init__(self, P=1, I=1, D=1):
        self.P = P
        self.I = I
        self.D = D

        self.I_d = 0
        self.D_d = 0

    def calculate(self, error):
        self.I_d += error
        res = self.P * error + self.I * (self.I_d) + self.D * (error - self.D_d)
        self.D_d = error
        return res
