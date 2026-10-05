from BaseClasses import Location
import typing

next_ap_id = 500000

class LocationData(typing.NamedTuple):
    id: int | None
    region: str
    upgrade_need: tuple[
            typing.Literal["Any", "All"],
            list[
                typing.Literal[
                "Air Boost",
                "Light Speed",
                "Stomping",
                "Wall Jump"
                ]
            ]
        ]

def get_data(region_name: str, conditions: tuple[typing.Literal["Any", "All"], list[typing.Literal["Air Boost", "Light Speed", "Stomping", "Wall Jump"]]], no_id: bool = False) -> LocationData:
    global next_ap_id
    if no_id:
        data = LocationData(None, region_name, conditions)
    else:
        data = LocationData(next_ap_id, region_name, conditions)
        next_ap_id += 1
        
    return data

class SonicUnleashedLocation(Location):
    game: str = "Sonic Unleashed"

location_table = {
    "colectable zone 1": get_data("Menu"),
    "zone 2": get_data("Menu"),
    "zone 3": get_data("Menu"),
    "zone 4": get_data("Menu"),
    "zone 5": get_data("Menu"),
    "zone 6": get_data("Menu"),
    "zone 7": get_data("Menu"),
    "zone 8": get_data("Menu")
}