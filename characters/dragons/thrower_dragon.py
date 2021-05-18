from .dragon import Dragon
from utils import random_or_none


class ThrowerDragon(Dragon):
    """ThrowerDragon throws a stone each turn at the nearest Terminator in its range."""

    name = 'Thrower'
    implemented = True
    damage = 1
    # ADD/OVERRIDE CLASS ATTRIBUTES HERE
    food_cost = 3
    min_range=0
    max_range=float('inf')

    def nearest_terminator(self, skynet):
        """Return the nearest Terminator in a Place that is not the SKYNET, connected to
        the ThrowerDragon's Place by following entrances.

        This method returns None if there is no such Terminator (or none in range).
        """
        # BEGIN 1.3 and 2.1
        poi=self.place      #place of interest
        i = 0
        while i<self.max_range and poi!=skynet.exit:
            #print(i)
            if poi==None: return None
            if i<self.min_range:
                i=i+1
                poi=poi.entrance
                continue
            if poi.terminators!=[]:
                break
            else:
                 poi=poi.entrance
                 i=i+1
        if poi==None: return None
        return random_or_none(poi.terminators)  # REPLACE THIS LINE
        # END 1.3 and 2.1

    def throw_at(self, target):
        """Throw a stone at the TARGET Terminator, reducing its armor."""
        if target is not None:
            target.reduce_armor(self.damage)

    def action(self, colony):
        """Throw a stone at the nearest Terminator in range."""
        self.throw_at(self.nearest_terminator(colony.skynet))
