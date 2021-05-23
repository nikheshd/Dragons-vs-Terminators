from .dragon import Dragon
from .thrower_dragon import ThrowerDragon
from utils import random_or_none
from utils import terminators_win

class DragonKing(ThrowerDragon):  # You should change this line
    # END 4.3
    """The King of the colony. The game is over if a terminator enters his place."""

    name = 'King'
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN 4.3
    implemented = True  # Change to True to view in the GUI
    instantiated = False
    food_cost = 7
    armor=1
    is_watersafe=False
    # END 4.3

    def __init__(self, armor=1):
        # BEGIN 4.3
        "*** YOUR CODE HERE ***"
        self.instantiated = not DragonKing.instantiated
        DragonKing.instantiated = True
        if self.instantiated==False:
            self.name = 'imposter'
            DragonKing.instantiated = True
        # END 4.3

    def action(self, colony):
        """A dragon king throws a stone, but also doubles the damage of dragons
        in his tunnel.

        Impostor kings do only one thing: reduce their own armor to 0.
        """
        # BEGIN 4.3
        "*** YOUR CODE HERE ***"
        if self.name == 'imposter':
            self.armor=0
            imp_place = self.place
            if imp_place.dragon.is_container==True:
                imp_place.dragon.contained_dragon=None
            else:
                imp_place.dragon=None
            self.place=None
            self.death_callback()
            return
        poi = self.place.exit   #place of interest
        while poi!=None:
            if poi.dragon and poi.dragon.is_buffed==False:
                poi.dragon.damage*= 2
                poi.dragon.is_buffed=True
                if poi.dragon.is_container==True:
                    if poi.dragon.contained_dragon and poi.dragon.contained_dragon.is_buffed==False:
                        poi.dragon.contained_dragon.damage*= 2
                        poi.dragon.contained_dragon.is_buffed=True
            elif poi.dragon and poi.dragon.is_container==True:
                if poi.dragon.contained_dragon and poi.dragon.contained_dragon.is_buffed==False:
                    poi.dragon.contained_dragon.damage*= 2
                    poi.dragon.contained_dragon.is_buffed=True
            poi = poi.exit
        #ThrowerDragon.action(DragonKing, colony)
        poi = self.place
        while poi!=None:
            if poi.terminators==[]:
                poi=poi.entrance
            else: break
        if poi!=None:
            target = random_or_none(poi.terminators)
            if target!=None:
                target.reduce_armor(1)
        # END 4.3

    def reduce_armor(self, amount):
        """Reduce armor by AMOUNT, and if the True DragonKing has no armor
        remaining, signal the end of the game.
        """
        # BEGIN 4.3
        "*** YOUR CODE HERE ***"
        if self.name=="King":
            self.armor-=amount
            if self.armor<=0:
                terminators_win()
