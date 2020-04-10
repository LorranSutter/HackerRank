class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    # Add your code here
    def computeDifference(self):
        sortedElements = sorted(self.__elements)
        self.maximumDifference = abs(sortedElements[0] - sortedElements[-1])
