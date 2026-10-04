from BaseClasses import MultiWorld

def link_areas(multiworld: MultiWorld, player: int):
    for exit, region in sonic_unleashed_connections:
        multiworld.get_entrance(exit, player).connect(multiworld.get_region(region, player))

sonic_unleashed_regions = [
    ("menu", [])
]

sonic_unleashed_connections = [

]