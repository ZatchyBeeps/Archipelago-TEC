from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasFromListUnique, HasFromList

from .locations import misc_locations, get_areas_ranksanities, offset
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
                # Had to do this instead of doing a big set of changes if I changed the names
                if "Sea" in region_name:
                    region = world.get_entrance(f"{region_name} Access")
                    requirement_rule = Has(f"Effect: Playlist (Sea) Mode Unlock")
                    world.set_rule(region, requirement_rule)
                    continue
                elif "Wind" in region_name:
                    region = world.get_entrance(f"{region_name} Access")
                    requirement_rule = Has(f"Effect: Playlist (Wind) Mode Unlock")
                    world.set_rule(region, requirement_rule)
                    continue
                elif "World" in region_name:
                    region = world.get_entrance(f"{region_name} Access")
                    requirement_rule = Has(f"Effect: Playlist (World) Mode Unlock")
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


    # Locations
    for name, data in get_areas_ranksanities(world).items():
        location = world.get_location(name)
        difficulty_increase = 1
        if "A Rank" in name:
            difficulty_increase = 2
        elif "S Rank" in name:
            difficulty_increase = 3
        elif "SS Rank" in name:
            difficulty_increase = 4

        if data.in_area == "Area 1":
            if difficulty_increase == 4: 
                difficulty_increase = 3
            elif difficulty_increase == 1: 
                difficulty_increase = 2 # Prevent it from being 0
            rule = HasFromList('The Deep Unlock','Pharaoh\'s Code Unlock','Karma Wheel Unlock', count=difficulty_increase-1)
        elif data.in_area == "Area 2":
            rule = HasFromList('Jellyfish Chorus Unlock','Da Vinci Unlock','Prayer Circles Unlock','Ritual Passion Unlock', count=difficulty_increase)
        elif data.in_area == "Area 3":
            rule = HasFromList('Deserted Unlock','Dolphin Surf Unlock','Downtown Jazz Unlock','Spirit Canyon Unlock', count=difficulty_increase)
        elif data.in_area == "Area 4":
            rule = HasFromList('Jewel Veil Unlock','Forest Dawn Unlock','Kaleidoscope Unlock','Turtle Dreams Unlock','Celebration Unlock', count=difficulty_increase)
        elif data.in_area == "Area 5":
            rule = HasFromList('Sunset Breeze Unlock','Aurora Peak Unlock','Zen Blossoms Unlock','Ying & Yang Unlock','Hula Soul Unlock', count=difficulty_increase)
        elif data.in_area == "Area 6":
            rule = HasFromList('Starfall Unlock','Balloon High Unlock','Mermaid Cove Unlock','Orbit Unlock','Stratosphere Unlock', count=difficulty_increase)

        if "A Rank" in name or "S Rank" in name or "SS Rank" in name:
            requirement = rule & Has("Zone Unlock")
        else:
            requirement = rule

        
        world.set_rule(location, requirement)

    # Prevents a gigantic sphere 1 from just trick locations by evenly requiring one more stage for every 10 of these location
    for n in range(4, 50):
        for name, data in misc_locations.items():
            try:
                amount_needed = round(n/4)+1
                t_location = world.get_location(world.location_id_to_name[data.location_id + n+offset])
                base_rule = HasFromListUnique('The Deep Unlock','Pharaoh\'s Code Unlock','Karma Wheel Unlock', 'Jellyfish Chorus Unlock','Da Vinci Unlock','Prayer Circles Unlock','Ritual Passion Unlock', 'Deserted Unlock','Dolphin Surf Unlock','Downtown Jazz Unlock','Spirit Canyon Unlock', 'Jewel Veil Unlock','Forest Dawn Unlock','Kaleidoscope Unlock','Turtle Dreams Unlock','Celebration Unlock', 'Sunset Breeze Unlock','Aurora Peak Unlock','Zen Blossoms Unlock','Ying & Yang Unlock','Hula Soul Unlock', 'Starfall Unlock','Balloon High Unlock','Mermaid Cove Unlock','Orbit Unlock','Stratosphere Unlock', count=amount_needed)
                location_r
                if "Zone" in data.identifier:
                    location_r = Has("Zone Unlock") & base_rule
                else:
                    location_r = base_rule
                world.set_rule(t_location, location_r)
            except KeyError:
                continue


    ending_region = world.get_entrance("Metamorphosis Stage Access")
    ending_stage = Has("Metamorphosis Unlock")
    world.set_rule(ending_region, ending_stage)
        

