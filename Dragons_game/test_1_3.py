import dragons, importlib
importlib.reload(dragons)
skynet = dragons.Skynet(dragons.AssaultPlan())
dimensions = (2, 9)
colony = dragons.DragonColony(None, skynet, dragons.dragon_types(), dragons.dry_layout, dimensions)
dragons.terminators_win = lambda: None
# DragonKing Removal
king = dragons.DragonKing()
impostor = dragons.DragonKing()
place = colony.places['tunnel_0_2']
place.add_fighter(impostor)
place.remove_fighter(impostor)
print(place.dragon is None)         # Impostors can be removed
