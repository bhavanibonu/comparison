import time
start = time.time()
class FindOdd:
 def __init__(self,end):
     self.__start = 1
     self.__end = end
 def __iter__(self):
     return OddsIterator(self.__end)
class OddsIterator:
    def __init__(self,finish):
     self.__current = 0
     self.__step = 1
     self.__end = finish
def __next__(self):
     x = None
     if self.__current > self.__end:
         raise StopIteration
     else:
        self.__current += self.__step
        if (self.__current - self.__step + 1) % 2 != 0:
            x = self.__current - self.__step + 1
if x != None:
         return x
odds = FindOdd(2)
print(list(odds))
end = time.time()
print(f"Runtime of the program is {end - start}")
