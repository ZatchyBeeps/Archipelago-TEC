import settings
import typing
from worlds.AutoWorld import World
from Options import OptionError
from .options import HiTheseAreGameOptions
from .items import TECItem, itemlist, zen_levels, zen_areas, effect_adventure_levels, effect_classic_levels, effect_focus_levels, effect_relax_levels, effect_groups, traps, tetrimino_items, garbage
from BaseClasses import Region, Location, Entrance, Item, RegionType, ItemClassification

class MyGameWorld(World):
    game = "Tetris Effect: Connected"
    options_dataclass = HiTheseAreGameOptions
    options: HiTheseAreGameOptions

    #def generate_early(self):
    #    return super().generate_early()

    def create_item(self, name):
        return TECItem(name, itemlist[name].priority, itemlist[name].item_id, self.player)


    def get_filler_item_name(self):
        if self.random.randint(0, 100) >= self.options.traps_perc:
            return self.random.choice(garbage)
        else:
            return self.random.choice(traps)

    def create_items(self):
        items_to_create: list
        if self.options.unlock_method == 0:
            items_to_create = zen_levels
            self.push_precollected(self.create_item(items_to_create.pop(self.random.randint(0, 25))))
            if self.options.is_include_effect:
                if not self.options.excluded_modes.__contains__("Classic"):
                    items_to_create += effect_classic_levels
                if not self.options.excluded_modes.__contains__("Relax"):
                    items_to_create += effect_relax_levels
                if not self.options.excluded_modes.__contains__("Focus"):
                    items_to_create += effect_focus_levels
                if not self.options.excluded_modes.__contains__("Adventorous"):
                    items_to_create += effect_adventure_levels
        else:
            items_to_create = zen_areas
            self.push_precollected(self.create_item(items_to_create.pop(self.random.randint(0, 4))))
            if self.options.is_include_effect:
                effect_items = effect_groups
                for value in self.options.excluded_modes:
                    effect_items.remove(value) # This will need some kind of validation
                items_to_create += effect_items # I am realizing now, how will the client know what modes to exclude specifically? I'll have to investigate

        if self.options.is_zonesanity:
            items_to_create += ["Zone Unlock"]

        if self.options.is_minosanity:
            items_to_create += tetrimino_items

        pre_filled_items = len(items_to_create)
        empty_spaces = len(self.get_region("Menu").locations)
        if pre_filled_items > empty_spaces:
            raise OptionError(f"{self.player}, your Tetris Effect world contains too little locations for the items required. Consider enabling ranksanity or increasing the number of trick locations")


        # add the fillers and traps