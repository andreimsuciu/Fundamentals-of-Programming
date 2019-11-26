from Errors.Errors import RepositoryError
class Repository(object):
    '''
    This class holds the repos 
    '''
    def __init__(self):
        self.__elems =[]
    
    def __len__(self):
        return len(self.__elems)
    
    def __eq__(self, otherList):
        return self.__elems == otherList
    
    def __getitem__(self, position):
        return self.__elems[position]
    
    def add(self,elem):
        if elem in self.__elems:
            raise RepositoryError("The element already exists!")
        self.__elems.append(elem)

    def search(self,elem):
        if elem not in self.__elems:
            raise RepositoryError("inexisting elem!")
        for x in self.__elems:
            if x == elem:
                return x
   
    def update(self,elem):
        if elem not in self.__elems:
            raise RepositoryError("inexisting elem!")
        for i in range(len(self.__elems)):
            if self.__elems[i]==elem:
                self.__elems[i]=elem
                return
    
    def remove(self,elem):
        if elem not in self.__elems:
            raise RepositoryError("inexisting elem!")
        for i in range(len(self.__elems)):
            if self.__elems[i]==elem:
                del self.__elems[i]
                return
    
    def clear(self):
        return self.__elems.clear()
    
    def getAll(self):
        return self.__elems[:]