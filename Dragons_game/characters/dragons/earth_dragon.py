class EarthDragon:
    # ADD/OVERRIDE CLASS ATTRIBUTES HERE
    food_cost = 4
    implemented = True
    name="Earth"
    is_dragon = True
    blocks_path = True

    def __init__(self):
        self.armor=4
        pass
    def action(self, colony):
        pass
    def reduce_armor(self, amount):
        self.armor-= amount
    pass
