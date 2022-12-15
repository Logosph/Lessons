class SixAngleNum:
    def __init__(self, maximum):
        self.maximum = maximum

    def __iter__(self):
        self.num = 1
        self.iteration = 0
        return self

    def __next__(self):
        if self.iteration >= self.maximum:
            raise StopIteration
        self.num += self.iteration * 6
        self.iteration += 1
        return self.num


for i in SixAngleNum(5):
    print(i)
