from .dragon import Dragon
from utils import random_or_none

class HungryDragon(Dragon):
    """HungryDragon will take three turns to digest a Terminator in its place.
    While digesting, the HungryDragon can't eat another Terminator.
    """
    name = 'Hungry'
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN 2.3
    implemented = True  # Change to True to view in the GUI
    food_cost = 4
    armor=1
    time_to_digest=3
    # END 2.3

    def __init__(self, armor=1):
        # BEGIN 2.3
        "*** YOUR CODE HERE ***"
        self.digesting=0
        # END 2.3

    def eat_terminator(self, terminator):
        # BEGIN 2.3
        "*** YOUR CODE HERE ***"
        if terminator!=None:
            amount=terminator.armor
            terminator.reduce_armor(amount)
        # END 2.3

    def action(self, colony):
        # BEGIN 2.3
        "*** YOUR CODE HERE ***"
        terminator=random_or_none(self.place.terminators)
        if self.digesting!=0:
            self.digesting-=1
        elif terminator!=None:
            self.digesting=self.time_to_digest
            self.eat_terminator(terminator)
