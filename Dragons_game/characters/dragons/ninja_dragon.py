from .dragon import Dragon


class NinjaDragon(Dragon):
    """NinjaDragon does not block the path and damages all terminators in its place."""

    name = 'Ninja'
    damage = 1
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN 2.4
    implemented = True  # Change to True to view in the GUI
    food_cost = 5
    blocks_path = False
    # END 2.4

    def action(self, colony):
        # BEGIN 2.4
        "*** YOUR CODE HERE ***"
        targets = self.place.terminators.copy()
        for target in targets:
            target.reduce_armor(self.damage)
