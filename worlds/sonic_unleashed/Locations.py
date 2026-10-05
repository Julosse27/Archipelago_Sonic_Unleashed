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

    # Apotos / Windmill Isle
    "Apotos Town Day - Moon Medal Behind Church": get_data("Apotos - Day",("Any",[])),
    "Apotos Town Day - Moon Medal Behind Tree": get_data("Apotos - Day",("Any",[])),

    "Apotos Town Night - Sun Medal Behind Table": get_data("Apotos - Night",("Any",[])),
    "Apotos Town Night - Left to the Shop": get_data("Apotos - Night",("Any",[])),

    "Apotos Town Shop - Record 15 (vs. Titan & Big Mother)": get_data("Apotos",("Any",[])),
    "Apotos Town Shop - Record 40 (Apotos - Day)": get_data("Apotos",("Any",[])),
    "Apotos Town Shop - Record 41 (Apotos - Night)": get_data("Apotos",("Any",[])),

    "Apotos Entrance Stage - Record 4 (Windmill Isle Suburbs - Day)": get_data("Apotos",("Any",[])),
    "Apotos Entrance Stage - Art Book 25 (Anastasia)": get_data("Apotos",("Any",[])),
    "Apotos Entrance Stage - Blue Tea": get_data("Apotos - Day",("Any",[])),
    "Apotos Entrance Stage - Sun Medal Under Crates": get_data("Apotos - Day",("Any",[])),
    "Apotos Entrance Stage - Moon Medal In Crates": get_data("Apotos",("Any",[])),
    "Apotos Entrance Stage - Sun Medal Windmill Isle Day Act 3 Platform": get_data("Apotos - Day",("Any",[])),
    "Apotos Entrance Stage - Moon Medal Far East Platform": get_data("Apotos",("Any",[])),
    "Apotos Entrance Stage - Art Book 21 (Opening #1)": get_data("Apotos",("Any",[])),
    "Apotos Entrance Stage - Record 29 (Intro: Skyscraper Scamper - Night)": get_data("Apotos",("Any",[])),
    "Apotos Entrance Stage - Maiden Statue": get_data("Apotos",("Any",[])),

    "Windmill Isle Day Act 1 - Act Clear": get_data("WI-D-1",("Any",[])),
    "Windmill Isle Day Act 1 - S Rank": get_data("WI-D-1",("Any",[])),

    "Windmill Isle Day Act 2 - Sun Medal Upper Path": get_data("WI-D-2",("Any",[])),
    "Windmill Isle Day Act 2 - Moon Medal Left Green Platform": get_data("WI-D-2",("Any",[])),
    "Windmill Isle Day Act 2 - Moon Medal Before Checkpoint": get_data("WI-D-2",("Any",[])),
    "Windmill Isle Day Act 2 - Moon Medal After Checkpoint": get_data("WI-D-2",("Any",[])),
    "Windmill Isle Day Act 2 - Moon Medal Secret Mini Restaurant Plaza": get_data("WI-D-2",("Any",[])),
    "Windmill Isle Day Act 2 - Moon Medal Before Rails": get_data("WI-D-2",("Any",[])),
    "Windmill Isle Day Act 2 - Moon Medal After Rails": get_data("WI-D-2",("Any",[])),
    "Windmill Isle Day Act 2 - Record 5 (Windmill Isle - Day)": get_data("WI-D-2",("Any",[])),
    "Windmill Isle Day Act 2 - Sun Medal Behind Rail Platform (2D Section)": get_data("WI-D-2",("Any",[])),
    "Windmill Isle Day Act 2 - Record 1 (Ochestral Theme - World Adventure)": get_data("WI-D-2",("Any",[])),
    "Windmill Isle Day Act 2 - Sun Medal Right Upper Path": get_data("WI-D-2",("Any",[])),
    "Windmill Isle Day Act 2 - Moon Medal Before Last 2D Section": get_data("WI-D-2",("Any",[])),
    "Windmill Isle Day Act 2 - Videotape 1 (Opening)": get_data("WI-D-2",("Any",[])),
    "Windmill Isle Day Act 2 - Art Book 1 (Apotos #1)": get_data("WI-D-2",("Any",[])),
    "Windmill Isle Day Act 2 - Act Clear": get_data("WI-D-2",("Any",[])),
    "Windmill Isle Day Act 2 - S Rank": get_data("WI-D-2",("Any",[])),

    "Windmill Isle Day Act 3 - Moon Medal #1": get_data("WI-D-3",("Any",[])),
    "Windmill Isle Day Act 3 - Sun Medal": get_data("WI-D-3",("Any",[])),
    "Windmill Isle Day Act 3 - Art Book 2 (Apotos #1)":get_data("WI-D-3",("Any",[])),
    "Windmill Isle Day Act 3 - Moon Medal #2": get_data("WI-D-3",("Any",[])),
    "Windmill Isle Day Act 3 - Art Book 22 (Opening #2)": get_data("WI-D-3",("Any",[])),
    "Windmill Isle Day Act 3 - Act Clear": get_data("WI-D-3",("Any",[])),
    "Windmill Isle Day Act 3 - S Rank": get_data("WI-D-3",("Any",[])),

    "Windmill Isle Night Act 1 - Sun Medal Right Wooden Door": get_data("WI-N-1",("Any",[])),
    "Windmill Isle Night Act 1 - Moon Medal Behind Barrel": get_data("WI-N-1",("Any",[])),
    "Windmill Isle Night Act 1 - Sun Medal Left Wooden Door": get_data("WI-N-1",("Any",[])),
    "Windmill Isle Night Act 1 - Moon Medal Right Wooden Door Pots": get_data("WI-N-1",("Any",[])),
    "Windmill Isle Night Act 1 - Record 16 (Windmill Isle - Night)": get_data("WI-N-1",("Any",[])),
    "Windmill Isle Night Act 1 - Moon Medal Platform": get_data("WI-N-1",("Any",[])),
    "Windmill Isle Night Act 1 - Sun Medal Beside Barrels": get_data("WI-N-1",("Any",[])),
    "Windmill Isle Night Act 1 - Sun Medal Left Wooden Door After Checkpoint": get_data("WI-N-1",("Any",[])),
    "Windmill Isle Night Act 1 - Moon Medal Behind Pots Before Checkpoint": get_data("WI-N-1",("Any",[])),
    "Windmill Isle Night Act 1 - Sun Medal Behind Stairs": get_data("WI-N-1",("Any",[])),
    "Windmill Isle Night Act 1 - Above Water": get_data("WI-N-1",("Any",[])),
    "Windmill Isle Night Act 1 - Art Book 64 (Dark Bat Sniper)": get_data("WI-N-1",("Any",[])),
    "Windmill Isle Night Act 1 - Sun Medal Right After Checkpoint": get_data("WI-N-1",("Any",[])),
    "Windmill Isle Night Act 1 - Moon Medal Right Stairs": get_data("WI-N-1",("Any",[])),
    "Windmill Isle Night Act 1 - Art Book 26 (People of Apotos #2)": get_data("WI-N-1",("Any",[])),
    "Windmill Isle Night Act 1 - Sun Medal Down Right Wooden Door": get_data("WI-N-1",("Any",[])),
    "Windmill Isle Night Act 1 - Sun Medal Stairs Behind Up Right Wooden Door": get_data("WI-N-1",("Any",[])),
    "Windmill Isle Night Act 1 - Art Book 24 (People of Apotos #1)": get_data("WI-N-1",("Any",[])),
    "Windmill Isle Night Act 1 - Sun Medal Far Left Balcony": get_data("WI-N-1",("Any",[])),
    "Windmill Isle Night Act 1 - Moon Medal Balancing Bar": get_data("WI-N-1",("Any",[])),
    "Windmill Isle Night Act 1 - Record 61 (Opening Movie-First Half)": get_data("WI-N-1",("Any",[])),
    "Windmill Isle Night Act 1 - Act Clear": get_data("WI-N-1",("Any",[])),
    "Windmill Isle Night Act 1 - S Rank": get_data("WI-N-1",("Any",[])),

    "Windmill Isle Night Act 2 - Sun Medal 3rd Room": get_data("WI-N-2",("Any",[])),
    "Windmill Isle Night Act 2 - Sun Medal 10th Room": get_data("WI-N-2",("Any",[])),
    "Windmill Isle Night Act 2 - Sun Medal 12th Room": get_data("WI-N-2",("Any",[])),
    "Windmill Isle Night Act 2 - Moon Medal Behind Green Key Pedestal": get_data("WI-N-2",("Any",[])),
    "Windmill Isle Night Act 2 - Art Book 54 (Ice Cream Vendor)": get_data("WI-N-2",("Any",[])),
    "Windmill Isle Night Act 2 - Record 17 (Intro: Windmill Isl - Night)": get_data("WI-N-2",("Any",[])),
    "Windmill Isle Night Act 2 - Sun Medal Behind Down Right Pot": get_data("WI-N-2",("Any",[])),
    "Windmill Isle Night Act 2 - Act Clear": get_data("WI-N-2",("Any",[])),
    "Windmill Isle Night Act 2 - S Rank": get_data("WI-N-2",("Any",[])),

    # Spagonia / Rooftop Run

    # Mazuri / Savannah Citadel

    # Holoska / Cool Edge

    # Chun-nan / Dragon Road

    # Shamar / Arid Sands

    # Empire City / Skyscraper Scamper

    # Adabat / Jungle Joyride

    # Eggmanland

    # Apotos & Shamar DLC 
    "Windmill Isle Day Act 1 Hard - Act Clear": get_data("WI-D-1H",("Any",[])),
    "Windmill Isle Day Act 1 Hard - S Rank": get_data("WI-D-1H",("Any",[])),
    "Windmill Isle Day Act 2 Hard - Act Clear": get_data("WI-D-2H",("Any",["Wall Jump", "Light Speed"])),
    "Windmill Isle Day Act 2 Hard - S Rank": get_data("WI-D-2H",("Any",["Wall Jump", "Light Speed"])),
    "Windmill Isle Day Act 4 - Act Clear": get_data("WI-D-4",("Any",[])),
    "Windmill Isle Day Act 4 - S Rank": get_data("WI-D-4",("Any",[])),

    "Windmill Isle Night Act 1 Hard - Act Clear": get_data("WI-N-1H",("Any",[])),
    "Windmill Isle Night Act 1 Hard - S Rank": get_data("WI-N-1H",("Any",[])),
    "Windmill Isle Night Act 1 Hard Bis - Act Clear": get_data("WI-N-1HB",("Any",[])),
    "Windmill Isle Night Act 1 Hard Bis - S Rank": get_data("WI-N-1HB",("Any",[])),


    # Empire City & Adabat DLC

    # Holoska DLC

    # Chun-nan DLC

    # Mazuri DLC

    # Spagonia DLC

    
}