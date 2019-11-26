from Validators.validators import ShipValidator
from Repository.shipRepository import ShipRepo
from Entities.entities import Ship

class ShipService(object):
    
    def __init__(self,__ShipValidator,__ShipRepo):
        self.__shipValidator = __ShipValidator
        self.__ShipRepo = __ShipRepo
    
    def add_ship(self,x,y,length,direction):
        '''
        Function that adds a ship to the shipRepo
        in:x,y<9 - coord, 1<length<5, direction='H' or 'V', shipRepo
        out:shipRepo' with newly added ship or Error
        '''
        ship=Ship(x,y,length,direction)
        self.__shipValidator.validate(ship)
        self.__ShipRepo.add(ship)
    
    def remove_ship(self,length):
        '''
        Function that removes a ship from the shipRepo
        in:1<length<5, shipRepo
        out:shipRepo' with deleted ship or Error
        '''
        ship=Ship(None,None,length,None)
        self.__ShipRepo.remove(ship)