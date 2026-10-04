from BaseClasses import Item, ItemClassification
import typing

next_ap_id = 500000

class ItemData(typing.NamedTuple):
    id: typing.Optional[int]
    classification: ItemClassification

def get_data(item_classification: ItemClassification) -> ItemData:
    global next_ap_id
    data = ItemData(next_ap_id, item_classification)
    next_ap_id += 1
    return data

class SonicUnleashedItem(Item):
    game = "Sonic Unleashed"

item_table = {
    "Moon medal":  get_data(ItemClassification.progression),
    "Sun medal": get_data(ItemClassification.progression),
    "CD 1": get_data(ItemClassification.filler),
    "CD 2": get_data(ItemClassification.filler),
    "CD 3": get_data(ItemClassification.filler),
    "ArtWork 1": get_data(ItemClassification.filler),
    "ArtWork 2": get_data(ItemClassification.filler),
    "ArtWork 3": get_data(ItemClassification.filler),
    "Video": get_data(ItemClassification.filler)
}

key_items = {
    "Moon medal": 200,
    "Sun medal": 200
}

filler_items_weight = {
    "CD 1": 1,
    "CD 2": 1,
    "CD 3": 1,
    "ArtWork 1": 1,
    "ArtWork 2": 1,
    "ArtWork 3": 1,
    "Video": 1
}