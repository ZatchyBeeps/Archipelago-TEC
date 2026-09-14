from dataclasses import dataclass

from Options import Toggle, Range, Choice, PerGameCommonOptions

class IncludeEffectMode(Toggle):
    display_name = "Include Effect Mode"

class EnableRanksanity(Toggle):
    display_name = "Ranksanity"

class RanksanityMaxRank(Choice):
    display_name = "Ranksanity "