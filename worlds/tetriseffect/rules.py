from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, Rule

from .options import EnableRanksanity
from .locations import base_locations, effect_mode_locations, zen_ranksanity_locations, effect_ranksanity_locations
from .regions import zen_regions, get_effect_regions

if TYPE_CHECKING:
    from . import TECWorld

def create_rules(world: TECWorld):
    if world.options.unlock_method == 0:
        for region_name, _ in zen_regions.items():
            entrance = world.get_entrance(f"{region_name} Stage Access")
            requirement_rule = Has(f"{region_name} Unlock")
            world.set_rule(entrance, requirement_rule)

        if world.options.is_include_effect:
            for region_name, _ in get_effect_regions(world).items():
                if "Sea" in region_name:
                    region = world.get_entrance(f"{region_name} Access")
                    requirement_rule = Has(f"Effect: Playlist (Sea) Mode Unlock")
                    world.set_rule(region, requirement_rule)
                    print(f"Created rule for sea on {region_name} Access")
                    continue
                elif "Wind" in region_name:
                    region = world.get_entrance(f"{region_name} Access")
                    requirement_rule = Has(f"Effect: Playlist (Wind) Mode Unlock")
                    print(f"Created rule for wind on {region_name} Access")
                    world.set_rule(region, requirement_rule)
                    continue
                elif "World" in region_name:
                    region = world.get_entrance(f"{region_name} Access")
                    requirement_rule = Has(f"Effect: Playlist (World) Mode Unlock")
                    print(f"Created rule for world on {region_name} Access")
                    world.set_rule(region, requirement_rule)
                    continue
                region = world.get_entrance(f"{region_name} Access")
                requirement_rule = Has(f"Effect: {region_name} Unlock")
                world.set_rule(region, requirement_rule)

    else:
        area_one = world.get_entrance("Area 1 Area Access")
        area_two = world.get_entrance("Area 2 Area Access")
        area_three = world.get_entrance("Area 3 Area Access")
        area_four = world.get_entrance("Area 4 Area Access")
        area_five = world.get_entrance("Area 5 Area Access")
        area_six = world.get_entrance("Area 6 Area Access")

        world.set_rule(area_one, Has("Area 1 Unlock"))
        world.set_rule(area_two, Has("Area 2 Unlock"))
        world.set_rule(area_three, Has("Area 3 Unlock"))
        world.set_rule(area_four, Has("Area 4 Unlock"))
        world.set_rule(area_five, Has("Area 5 Unlock"))
        world.set_rule(area_six, Has("Area 6 Unlock"))

        if world.options.is_include_effect:
            group_list = [name for name in ["Classic", "Relax", "Focus", "Adventorous"] if not name in world.options.excluded_modes]
            for group in group_list:
                region = world.get_entrance(f"{group} Modes Access")
                requirement_rule = Has(f"Effect: {group} Modes Unlock")

