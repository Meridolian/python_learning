class MultiplicationTable:

    def __init__(self, number):
        self.number = number
        self.generator = (self.number * x for x in range(10))

    def next(self):
        return next(self.generator)
