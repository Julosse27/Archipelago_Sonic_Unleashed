from collections.abc import Mapping
from typing import Any

from worlds.AutoWorld import World
from BaseClasses import Item, ItemClassification, Location, Region, Entrance
from .options import SonicUnleashedOptions
from .Locations import location_table, SonicUnleashedLocation
from .Items import item_table, SonicUnleashedItem, key_items, filler_items_weight
from .Regions import sonic_unleashed_regions, link_areas

class SonicUnleashedWorld(World):
    game = "Sonic Unleashed"
    options_dataclass = SonicUnleashedOptions
    options: SonicUnleashedOptions
    item_name_to_id = {name: location.id for name, location in item_table.items()} # type: ignore
    location_name_to_id = {name: location.id for name, location in location_table.items()} # type: ignore

    def create_item(self, name: str) -> SonicUnleashedItem:
        """
        Permet de créer un item archipelago à partir de son nom
        """
        item_data = item_table[name]
        return SonicUnleashedItem(name, item_data.classification, item_data.id, self.player)

    def create_regions(self) -> None:
        """
        Créé les régions pour l'archipelago.
        """
        def create_region(region_name: str, exits:list[str] = []):
            """
            Créé la région avec ses attributs.
            """
            region = Region(region_name, self.player, self.multiworld)

            region.locations += [
                SonicUnleashedLocation(self.player, loc_name, loc_data.id, region)
                for loc_name, loc_data in location_table.items()
                if loc_data.region == region_name
            ]

            for exit in exits:
                region.exits.append(Entrance(self.player, exit, region))

            return region
        
        self.multiworld.regions += [create_region(name, exits) for name, exits in sonic_unleashed_regions]
        link_areas(self.multiworld, self.player)

    def get_filler_item_name(self):
        return self.random.choices(list(filler_items_weight.keys()), list(filler_items_weight.values()))[0]

    def create_items(self) -> None:
        """
        Créé tout les items du jeu.
        """
        pool = []

        for item_name, nb_item in key_items.items():
            pool += [item_name] * nb_item
        
        while len(pool) < len(self.multiworld.get_unfilled_locations(self.player)):
            pool.append(self.create_filler())

        self.multiworld.itempool += pool

    def set_rules(self) -> None:
        self.multiworld.completion_condition[self.player] = lambda state: True

    def fill_slot_data(self) -> Mapping[str, Any]:
        return {
            "seed_name": self.multiworld.seed_name,
            "player_name": self.multiworld.get_player_name(self.player),
            "player_id": self.player,
            "client_version": self.required_client_version,
            "item_name_to_id": self.item_name_to_id.copy(),
            "item_id_to_name": {code: name for name, code in self.item_name_to_id.items()},
            "total_medals": (self.options.total_sun_medals, self.options.total_moon_medals)
        }