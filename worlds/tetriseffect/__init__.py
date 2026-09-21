from worlds.AutoWorld import World
from Options import OptionError
from .options import HiTheseAreGameOptions, tec_option_groups
from . import locations, regions
from rule_builder.rules import Has

from .items import TECItem, item_table, itemlist, zen_levels, zen_areas, effect_adventure_levels, effect_classic_levels, effect_focus_levels, effect_relax_levels, effect_groups, traps, tetrimino_items, garbage

class TECWorld(World):
    game = "Tetris Effect: Connected"
    options_dataclass = HiTheseAreGameOptions
    options: HiTheseAreGameOptions
    location_name_to_id = locations.get_location_table()
    item_name_to_id = item_table
    option_groups = tec_option_groups
    origin_region_name = "Menu"

    #def generate_early(self):
    #    return super().generate_early()

    def create_item(self, name):
        return TECItem(name, itemlist[name].priority, itemlist[name].item_id, self.player)


    def get_filler_item_name(self):
        if self.random.randint(0, 99) >= self.options.traps_perc:
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

        if self.options.is_start_zone:
            items_to_create += ["Zone Unlock"]
        else:
            self.push_precollected(self.create_item("Zone Unlock"))

        if self.options.is_minosanity:
            items_to_create += tetrimino_items

        pre_filled_items = len(items_to_create)
        empty_spaces = len(self.multiworld.get_unfilled_locations(self.player))
        if pre_filled_items > empty_spaces:
            raise OptionError(f"{self.player}, your Tetris Effect world contains too little locations for the items required. Consider enabling ranksanity or increasing the number of trick locations")

        self.multiworld.itempool += [self.create_item(item) for item in items_to_create]

        self.multiworld.itempool += [self.create_filler() for _ in range(empty_spaces - pre_filled_items)]

    def create_regions(self):
        regions.make_regions(self)
        locations.create_locations(self)

    def set_rules(self):
        self.set_completion_rule(Has("Victory"))

    def fill_slot_data(self):
        return self.options.as_dict("unlock_method", "is_include_effect", "excluded_modes", "death_link", "is_ranksanity")
