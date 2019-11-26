
import unittest
from Repository.shipRepository import ShipRepo
from Entities.entities import Ship,Hits
from Controllers.shipService import ShipService
from Validators.validators import ShipValidator, HitValidator
from Errors.errors import RepositoryError, ValidError
from UI.ui import Console
from Controllers.gameService import GameService
from Repository.hitRepository import HitRepo

class test_stuff(unittest.TestCase):

    def setUp(self):
        self.__repo=ShipRepo()
        self.__validator=ShipValidator()
        self.__shipService=ShipService(ShipValidator,ShipRepo)
        self.__repoAI=ShipRepo()
        self.__hitRepoPlayer=HitRepo()
        self.__hitRepoAI=HitRepo()
        self.__hitValidator=HitValidator()
        self.__hitsAI=Hits()
        self.__hitsPlayer=Hits()
        self.__gameService=GameService(self.__hitValidator,self.__hitRepoPlayer,self.__hitRepoAI,self.__repo,self.__repoAI,self.__hitsAI,self.__hitsPlayer)
        
    def tearDown(self):
        pass
    
    def test_add(self):
        ship=Ship(1,2,4,'V')
        self.__validator.validate(ship)
        self.__repo.add(ship)
        #self.__shipService.add_ship(1,2,4,'V')
        ship2=Ship(2,2,3,'H')
        with self.assertRaises(RepositoryError):
            self.__repo.add(ship2)
        ship3=Ship(4,2,3,'V')
        with self.assertRaises(RepositoryError):
            self.__repo.add(ship3)
            
    def test_remove(self):
        ship1=Ship(1,2,4,'V')
        self.__repo.add(ship1)
        length=4
        ship2=Ship(None,None,length,None)
        self.__repo.remove(ship2)
    
    def test_ai_add(self):
        x,y,d=self.__gameService.ai_place_ships()
        ship=Ship(x,y,2,d)
        
        try:
            self.__validator.validate(ship)
        except:
            pass
            
        self.__repoAI.add(ship)
        assert len(self.__repoAI) == 1
        
        
        
        