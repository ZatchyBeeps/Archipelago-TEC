import settings
import typing
from worlds.AutoWorld import World
from .options import HiTheseAreGameOptions
from BaseClasses import Region, Location, Entrance, Item, RegionType, ItemClassification

class MyGameWorld(World):
    game = "Tetris Effect: Connected"
    options_dataclass = HiTheseAreGameOptions
    options: HiTheseAreGameOptions