from worlds.AutoWorld import World
from BaseClasses import Item, ItemClassification, Location, Region
from .options import SonicUnleashedOptions
import typing

typing.NamedTuple

BASE_ID = 5_500_000
item_table = {
    "Medal": BASE_ID,
    "filler": BASE_ID + 1
}

location_table = {
    "zone 1": BASE_ID,
    "zone 2": BASE_ID + 1,
    "zone 3": BASE_ID + 2,
    "zone 4": BASE_ID + 3,
    "zone 5": BASE_ID + 4,
    "zone 6": BASE_ID + 5,
    "zone 7": BASE_ID + 6,
    "zone 8": BASE_ID + 7
}

class SonicUnleashedItem(Item):
    game = "Sonic Unleashed"

class SonicUnleashedLocation(Location):
    game = "Sonic Unleashed"

class SonicUnleashedWorld(World):
    game = "Sonic Unleashed"
    options_dataclass = SonicUnleashedOptions
    options: SonicUnleashedOptions
    item_name_to_id = item_table
    location_name_to_id = location_table

    def create_item(self, name: str) -> SonicUnleashedItem:
        """
        Permet de créer un item archipelago à partir de son nom
        """
        return SonicUnleashedItem(name, ItemClassification.progression, self.item_name_to_id[name], self.player)

    def create_regions(self) -> None:
        """
        Créé les régions pour le jeu.
        """
        menu = Region("Menu", self.player, self.multiworld)
        for name, code in location_table.items():
            menu.locations.append(SonicUnleashedLocation(self.player, name, code, menu))
        self.multiworld.regions.append(menu)

    def create_items(self) -> None:
        """
        Créé tout les items du jeu.
        """
        pool = [self.create_item("Medal") for _ in range(self.options.total_medals.value)]

        while len(pool) < len(location_table):
            pool.append(SonicUnleashedItem("Filler", ItemClassification.filler, self.item_name_to_id["filler"], self.player))

        self.multiworld.itempool += pool

    def set_rules(self) -> None:
        self.multiworld.completion_condition[self.player] = lambda state: True