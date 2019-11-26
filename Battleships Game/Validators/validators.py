from Entities.entities import Ship
from Errors.errors import ValidError

class ShipValidator(object):
    """
        Validate the given ship
        
        input: 
            ship - the ship instance to be validated
        output: 
            None
        raises: 
            ValidError in case of validation error
        """
    def validate(self,ship):
        errors=""
        if ship.x<0 or ship.y<0:
            errors+="x and y should be positive!"
        if ship.get_length()<2 or ship.get_length()>4:
            errors+="length of ship is not accepted."
        if ship.get_direction() != 'H' and ship.get_direction() != 'V':
            errors+="ship direction must be (H)oriziontal or (V)ertical"
        if ship.get_direction() == 'H':
            if ship.get_length() + ship.get_y() > 8:
                errors+="ocean too small for this positioning!"
        if ship.get_direction() == 'V':
            if ship.get_length() + ship.get_x() > 8:
                errors+="ocean too small for this positioning!"
        if len(errors)>0:
            raise ValidError(errors)            

class HitValidator(object):
    pass


