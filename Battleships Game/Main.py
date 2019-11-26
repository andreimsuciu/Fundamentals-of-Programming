from Repository.shipRepository import ShipRepo
from Repository.hitRepository import HitRepo
from Controllers.shipService import ShipService
from Controllers.gameService import GameService
from Validators.validators import ShipValidator
from Validators.validators import HitValidator
from UI.ui import Console
from Entities.entities import Hits

"""
BATTLESHIPS
"""

shipRepoPlayer=ShipRepo()
shipRepoAI=ShipRepo()
hitRepoPlayer=HitRepo()
hitRepoAI=HitRepo()

shipValidator=ShipValidator()

hitValidator=HitValidator()

shipServicePlayer=ShipService(shipValidator,shipRepoPlayer)
shipServiceAI=ShipService(shipValidator,shipRepoAI)

hitsAI=Hits()
hitsPlayer=Hits()

gameService=GameService(hitValidator,hitRepoPlayer,hitRepoAI,shipRepoPlayer,shipRepoAI,hitsAI,hitsPlayer)


#playerBoard=Board()
#aiBoard=Board()

console=Console(shipServicePlayer,shipServiceAI,gameService)

console.run()