class Domino:
    def __init__(self, a, b):
        self.faceA = a
        self.faceB = b

    def show_points(self):
        a = str(self.faceA)
        b = str(self.faceB)
        return "face A : " + a + " / face B : " + b

    def show_total(self):
        total = str(self.faceA + self.faceB)
        return "total : " + total
