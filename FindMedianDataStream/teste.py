class MedianFinder(object):

    def __init__(self):
        self.lista = []

    def addNum(self, num):
        
        self.lista.append(num)
        print(f"numero adicionado: {num}")
        print(f"lista atual: {self.lista}")

    def findMedian(self):

        n = len(self.lista)
        if n % 2 == 1:
            return float(self.lista[n // 2])
        else:
            return (self.lista[n // 2 - 1] + self.lista[n // 2]) / 2.0

obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
print(obj.findMedian()) 
obj.addNum(3)
print(obj.findMedian()) 
