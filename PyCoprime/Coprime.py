from time import time

class MyIterator():

    def __init__(self, size):
        self.hasNext = bool(size)
        self.comb = [False] * size

    def __iter__(self):
        return self

    def next(self):
        if self.hasNext:

            for pos,i in enumerate(self.comb):
                if not i:
                    self.comb[pos] = True
                    break
                else:
                    self.comb[pos] = False  

            if False in self.comb:
                self.hasNext = True

            else :
                self.hasNext = False

            return self.comb
        
        else:
            raise StopIteration

    def getPermutation(self):
        pass


class MyNumbers():

    def __init__(self, items):
        self.items = items

    def getCombination(self):
        obj = MyIterator(len(self.items))
        itert = iter(obj)
        try:
            while True:
                aux = []
                p = next(itert)
                for pos,i in enumerate(p):
                    if i:
                        aux.append(self.items[pos])

                for pos in enumerate(aux):
                    for posNext in range(pos,len(aux)):
                        if self.checkCoprime(aux[pos],aux[posNext]):
                            continue

                print(aux)

        except StopIteration as e:
            print("End")


    def checkCoprime(self,a,b):
        while (b != 0):
            aux = a;
            a = b;
            b = aux % b;
        return a;

class getTime():

    def __init__(self):
        pass


    def getTime():
        arr = getNumbers("numbers5.txt")
        t = time()
        myclass = MyNumbers(arr)
        myclass.getCombination()
        t = time() - t
        print("Tiempo {} ".format((t/1000))

    def getNumbers(self,filename):
        file = open(filename,'r')
        self.numbers = [int(line) for line in file]
        file.close()

ejecutar = getTime()
ejecutar.getNumbers
ejecutar.getTime()
