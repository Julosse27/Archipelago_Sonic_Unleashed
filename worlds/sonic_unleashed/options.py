from dataclasses import dataclass
from Options import PerGameCommonOptions, Range

class TotalMedals(Range):
    """
    Le nombre de médailes nécéssaires pour terminer l'archipelago
    """
    range_start = 1
    range_end = 8
    default = 6

@dataclass
class SonicUnleashedOptions(PerGameCommonOptions):
    total_medals: TotalMedals