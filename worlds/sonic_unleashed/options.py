from dataclasses import dataclass
from Options import PerGameCommonOptions, Range, Toggle, Choice

class TotalSunMedals(Range):
    """
    Le nombre de médailles de soleil nécéssaires pour terminer l'archipelago
    """
    range_start = 50
    range_end = 200
    default = 120

class TotalMoonMedals(Range):
    """
    Le nombre de médailles de lune pour terminer l'archipelago
    """
    range_start = 50
    range_end = 200
    default = 80

@dataclass
class SonicUnleashedOptions(PerGameCommonOptions):
    total_sun_medals: TotalSunMedals
    total_moon_medals: TotalMoonMedals