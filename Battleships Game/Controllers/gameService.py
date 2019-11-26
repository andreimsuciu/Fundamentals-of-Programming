from Entities.entities import Ship
import random
from Errors.errors import GameServiceError


class GameService(object):
    def __init__(self,__hitValidator,__hitRepoPlayer,__hitRepoAI,__shipRepoPlayer,__shipRepoAI,__hitsAI,__hitsPlayer):
        self.__hitValidator = __hitValidator
        self.__hitRepoPlayer = __hitRepoPlayer
        self.__hitRepoAI= __hitRepoAI
        self.__shipRepoPlayer = __shipRepoPlayer
        self.__shipRepoAI = __shipRepoAI
        self.__hitsAI=__hitsAI
        self.__hitsPlayer=__hitsPlayer
    
    def get_shipRepoPlayer(self):
        return self.__shipRepoPlayer
    
    def get_shipRepoAI(self):
        return self.__shipRepoAI
    
    def get_hitRepoPlayer(self):
        return self.__hitRepoPlayer
    
    def get_hitRepoAI(self):
        return self.__hitRepoAI
          
    def ai_place_ships(self):
        '''
        function that generates random ship-type values
        in:-
        out:ship
        '''
        x = random.randint(0,7)
        y = random.randint(0,7)
        d = random.randint(0,1)
        if d == 1:
            direction='V'
        elif d== 0:
            direction='H'
        return x,y,direction        
    
    def check_ship_coord_player(self,x,y):
        '''
        Function that checks whether a ship is on the given coordinates 
        in:x,y
        out:ship-the type of ship hit, false-if it isn't 
        '''
        l=self.__shipRepoPlayer.getAll()
        for i in range(len(l)):
            if l[i].direction=="V":
                xRepo=l[i].x
                yRepo=l[i].y
                for j in range(l[i].length+1):
                    if xRepo+j==x and yRepo==y:
                        x=self.hit_player_ship(l[i].length)
                        return x
            elif l[i].direction=="H":
                xRepo=l[i].x
                yRepo=l[i].y
                for j in range(l[i].length+1):
                    if xRepo==x and yRepo==y+j:
                        x=self.hit_player_ship(l[i].length)
                        return x
        x="-"
        return x
    
    def hit_player_ship(self,length):
        '''
        Function that tracks which ships are hit
        in:length
        '''
        if length==2:
            self.__hitsPlayer.destroyer-=1
            return "D"
            if self.__hitsPlayer.destroyer==0:
                return "d"
        elif length==3:
            self.__hitsPlayer.cruiser-=1
            return "C"
            if self.__hitsPlayer.cruiser==0:
                return "c"
        elif length==4:
            self.__hitsPlayer.battleship-=1
            return "B"
            if self.__hitsPlayer.battleship==0:
                return "b"
            
    def ai_hit(self):
        x = random.randint(0,7)
        y = random.randint(0,7)
        if self.__hitRepoPlayer.search(x,y)=="-":
            ship=self.check_ship_coord_player(x, y)
            if ship=="D" or ship =="C" or ship =="B":
                self.__hitRepoPlayer.update(x,y,"X")
                return ship
            elif ship=="d" or ship =="c" or ship =="b":
                self.__hitRepoAI.update(x,y,"X")
                return ship
            else:
                self.__hitRepoPlayer.update(x,y,"O")
                ship="N"
                return ship
        else:
            self.ai_hit()
        
    def hit_ai_ship(self,length):
        '''
        Function that tracks which ships are hit
        in:length
        '''
        if length==2:
            self.__hitsAI.destroyer-=1
            return "D"
            if self.__hitsAI.destroyer==0:
                return "d"
        elif length==3:
            self.__hitsAI.cruiser-=1
            return "C"
            if self.__hitsAI.cruiser==0:
                return "c"
        elif length==4:
            self.__hitsAI.battleship-=1
            return "B"
            if self.__hitsAI.battleship==0:
                return "b"
            
    def check_ship_coord_ai(self,x,y):
        '''
        Function that checks whether a ship is on the given coordinates 
        in:x,y
        out:ship-the type of ship hit, false-if it isn't 
        '''
        l=self.__shipRepoAI.getAll()
        for i in range(len(l)):
            if l[i].direction=="V":
                xRepo=l[i].x
                yRepo=l[i].y
                for j in range(l[i].length+1):
                    if xRepo+j==x and yRepo==y:
                        x=self.hit_ai_ship(l[i].length)
                        return x
            elif l[i].direction=="H":
                xRepo=l[i].x
                yRepo=l[i].y
                for j in range(l[i].length+1):
                    if xRepo==x and yRepo==y+j:
                        x=self.hit_ai_ship(l[i].length)
                        return x
        x="-"
        return x
    
    def check_win_player(self):
        if self.__hitsAI.destroyer==0 and self.__hitsAI.cruiser==0 and self.__hitsAI.battleship==0:
            return True
        else:
            return False
    
    def check_win_ai(self):
        if self.__hitsPlayer.destroyer==0 and self.__hitsPlayer.cruiser==0 and self.__hitsPlayer.battleship==0:
            return True
        else:
            return False
    
    def player_hit(self,x,y):
        '''
        function that takes care of player hits
        in:shiprepoAI,hitrepoAI, x,y
        out:hitrepoAI', type of ship if it hit, "N" if not hit
        '''
        x-=1
        y-=1
        if self.__hitRepoAI.search(x,y)=="-":
            ship=self.check_ship_coord_ai(x, y)
            if ship=="D" or ship =="C" or ship =="B":
                self.__hitRepoAI.update(x,y,"X")
                return ship
            elif ship=="d" or ship =="c" or ship =="b":
                self.__hitRepoAI.update(x,y,"X")
                return ship
            else:
                self.__hitRepoAI.update(x,y,"O")
                ship="N"
                return ship
        else:
            raise GameServiceError("Already hit there!")
                     
        
                    
    hitRepoPlayer=property(get_hitRepoPlayer,None,None,None)   
    hitRepoAI=property(get_hitRepoAI,None,None,None)
    shipRepoAI=property(get_shipRepoAI,None,None,None)
    shipRepoPlayer=property(get_shipRepoPlayer,None,None,None)            