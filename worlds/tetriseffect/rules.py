from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, Rule, CanReachRegion, HasFromList

from .options import EnableRanksanity
from .locations import base_locations, effect_mode_locations, zen_ranksanity_locations, effect_ranksanity_locations
from .regions import zen_regions, get_effect_regions
from .items import zen_levels

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
        for area_num in range(1, 6):
            entrance = world.get_entrance(f"Area {area_num} Area Access")
            rule = Has(f"Area {area_num} Unlock")

        if world.options.is_include_effect:
            group_list = [name for name in ["Classic", "Relax", "Focus", "Adventorous"] if not name in world.options.excluded_modes]
            for group in group_list:
                region = world.get_entrance(f"{group} Modes Access")
                requirement_rule = Has(f"Effect: {group} Modes Unlock")


    for name, data in base_locations.items():
        location = world.get_location(name)
        rule = CanReachRegion(data.region)
        world.set_rule(location, rule)


    ending_region = world.get_entrance("Metamorphosis Stage Access")
    ending_rule = Has("Stage Cleared", count=10)
    ending_stage = Has("Metamorphosis Unlock")
    completion_rule = ending_rule & ending_stage
    world.set_rule(ending_region, completion_rule)
        

