# Dragons-vs-Terminators
A tower defense game

(download the .rar file, extract it and run 'python3 gui.py' from that directory to start the game's webUI)

Note: Don't press restart in the webUI to play again (causing glitches in the UI making terminators move invisibly).
To restart, refresh the browser.

Storyline of the game:

The terminator robots are trying to steal the Dragon eggs and heart of the dragon king. 
Dragons win if all of the terminators are destroyed. 
Terminators win if they reach the end of the tunnel or kill the dragon king. 
The player is expected to place different types of Dragons in the path to protect the dragon colony and destroy the terminators.

Instructions:

Each dragon has a food_cost attribute that indicates how much it costs to summon one unit of that type of dragon.
Terminators arise from Skynet.
Terminator either moves to the forward if no dragon blocks its path or attack a dragon that blocks its path.

Dragon types:

1. HarvesterDragon: Food=2, Armor=1
(adds one food to the colony food total as its action)

2. ThrowerDragon: Food=3, Armor=1
(It throws a stone which deals damage=1 to the nearest terminator in front of it that is not still in the Skynet)

3. LongThrower: Food=2, Armor=1
(It is subclass of ThrowerDragon that throws at the nearest terminator atleat 5 steps away)

4. ShortThrower: Food=2, Armor=1
(It is subclass of ThrowerDragon that throws at the nearest terminator atmost 3 steps away)

5. FireDragon: Foos=5, Armor=3
(If it is damaged by x armor units, and does not die, it does a damage of x to all terminators in it's place (reflected damage). If it dies, it does an additional damage=3)

6. HungryDragon: Food=4, Armor=1
(It will select a random Terminator from its place and eat it whole. After eating a Terminator, it must spend 3 turns digesting before eating again. If there is no terminator available to eat, it will do nothing)

7. NinjaDragon: Food=5, Armor=1
(It does not block the path of a Terminator that flies by but deals damage=1to all that fly past)

Note: By default, all dragons block the path of a Terminator that flies by.

8. EarthDragon: Food=4, Armor=4
(It does nothing! It is useful because it has a large armor value)

9. BodyguardDragon: Food=4, Armor=2
(It can contain another dragon(which is not a BodyguardDragon) and protect it, all in one Place)

10. TankDragon: Food=6, Armor=2
(It is subclass of BodyguardDragon that also deals 1 damage to all terminators in its place each turn)

11. DragonKing: Food=7, Armor=1
(King doubles the damage of all the dragons behind him each time he performs an action. Once a dragon's damage has been doubled, it is not doubled again for subsequent turns.)

There can be only one true king. Any king instantiated beyond the first one is an impostor, and should have its armor reduced to 0 upon taking its first action, without doubling any dragon's damage or throwing anything. If an impostor dies, the game should still continue as normal.
