from Errors.errors import RepositoryError

class ShipRepo(object):
    '''
    This class holds the repo for the ships 
    '''
    def __init__(self):
        self.__elems =[]
    
    def __len__(self):
        return len(self.__elems)
    
    def __eq__(self, otherList):
        return self.__elems == otherList
    
    def __getitem__(self, position):
        return self.__elems[position]
    
    def add(self,ship):
        '''
        Function that adds a ship to the repo, if it is not there, or it does not overlap existing ship
        we have 4 cases
        in:ship, list of ships
        out:list of ships with newly added ship OR RepositoryError, if type of ship already added, or overlaps existing ship
        '''
        if ship in self.__elems:
            raise RepositoryError("This type of ship already exists!")
        
        for i in range(len(self.__elems)):
            repoShip=self.__elems[i]
            if repoShip.direction=='V':
                for j in range(repoShip.length):
                    if ship.direction=='V':
                        for k in range(ship.length):
                            if repoShip.x+j == ship.x+k and repoShip.y == ship.y:
                                raise RepositoryError("Added ship overlaps with existing ship!")
                    elif ship.direction=='H':
                        for k in range(ship.length):
                            if repoShip.x+j == ship.x and repoShip.y == ship.y+k:
                                raise RepositoryError("Added ship overlaps with existing ship!")
            elif repoShip.direction=='H':
                for j in range(repoShip.length):
                    if ship.direction=='V':
                        for k in range(ship.length):
                            if repoShip.x == ship.x+k and repoShip.y+j == ship.y:
                                raise RepositoryError("Added ship overlaps with existing ship!")
                    elif ship.direction=='H':
                        for k in range(ship.length):
                            if repoShip.x == ship.x and repoShip.y+j == ship.y+k:
                                raise RepositoryError("Added ship overlaps with existing ship!")
                            
        self.__elems.append(ship)

    def search(self,elem):
        '''
        Function that searches for a ship in the list of ships
        in:ship, list of ships
        '''
        if elem not in self.__elems:
            raise RepositoryError("This ship was not added!")
        for x in self.__elems:
            if x == elem:
                return x
    
    def remove(self,ship):
        '''
        Function that removes a ship from the repo
        in:ship, list of ships
        out:list of ships, without the ship that was deleted, OR RepositoryError if the given ship is not there
        '''
        if ship not in self.__elems:
            raise RepositoryError("This ship was not added yet!")
        for i in range(len(self.__elems)):
            if self.__elems[i]==ship:
                del self.__elems[i]
                return
    
    def clear(self):
        '''
        Function that clears the repo
        in:list of ships
        out:empty list
        '''
        return self.__elems.clear()
    
    def getAll(self):
        '''
        Function that return the list of ships
        '''
        return self.__elems[:]


