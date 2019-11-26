
class Ship(object):
    '''
    Ship model
    x,y - coordinates
    length- <4 and >1
    direction= 'H' or 'V' 
    '''
    def __init__(self, __x,__y,__length,__direction):
        self.__x = __x
        self.__y = __y
        self.__length = __length
        self.__direction = __direction
        
    def get_x(self):
        return self.__x
    def get_y(self):
        return self.__y 
    def get_length(self):
        return self.__length 
    def get_direction(self):
        return self.__direction  
    
    def __eq__(self, other):
        return self.__length==other.__length
    
    x = property(get_x, None, None, None)
    y = property(get_y, None, None, None)
    length = property(get_length, None, None, None)
    direction = property(get_direction, None, None, None)
    

class Hits(object):
    def __init__(self, __destroyer=2,__cruiser=3,__battleship=4):
        self.__destroyer = __destroyer
        self.__cruiser = __cruiser
        self.__battleship = __battleship
    
    def get_dest(self):
        return self.__destroyer
    def get_crui(self):
        return self.__cruiser
    def get_battle(self):
        return self.__battleship
    def set_dest(self,value):
        self.__destroyer=value
    def set_crui(self,value):
        self.__cruiser=value
    def set_battle(self,value):
        self.__battleship=value
    
    destroyer = property(get_dest, set_dest, None, None)
    cruiser = property(get_crui, set_crui, None, None)
    battleship = property(get_battle, set_battle, None, None)