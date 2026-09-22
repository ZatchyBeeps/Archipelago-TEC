from __future__ import annotations

from typing import TYPE_CHECKING, NamedTuple

from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from . import TECWorld

zen_regions = {
    'The Deep':             1,
    'Pharaoh\'s Code':      1,
    'Karma Wheel':          1,
    'Jellyfish Chorus':     2,
    'Da Vinci':             2,
    'Prayer Circles':       2,
    'Ritual Passion':       2,
    'Deserted':             3,
    'Dolphin Surf':         3,
    'Downtown Jazz':        3,
    'Spirit Canyon':        3,
    'Jewel Veil':           4,
    'Forest Dawn':          4,
    'Kaleidoscope':         4,
    'Turtle Dreams':        4,
    'Celebration':          4,
    'Sunset Breeze':        5,
    'Aurora Peak':          5,
    'Zen Blossoms':         5,
    'Ying & Yang':          5,
    'Hula Soul':            5,
    'Starfall':             6,
    'Balloon High':         6,
    'Mermaid Cove':         6,
    'Orbit':                6,
    'Stratosphere':         6,
    'Metamorphosis':        7
}

effect_regions = {
    'Marathon':             1, 
    'Zone Marathon':        1,
    'Ultra':                1,
    'Sprint':               1,
    'Master':               1,
    'Classic Score Attack': 1,
    'Chill Marathon':       2,
    'Quick Play':           2,
    'Sea Playlist':         2,
    'Wind Playlist':        2,
    'World Playlist':       2,
    'All Clear':            3,
    'Combo':                3,
    'Target':               3,
    'Countdown':            4,
    'Purity':               4,
    'Mystery':              4,
}

def get_effect_regions(world: TECWorld) -> dict[str, int]:
    return {f"{name} Mode": area for name, area in effect_regions.items() if not name in world.options.excluded_modes}

def make_regions(world: TECWorld):
    root = Region("Menu", world.player, world.multiworld)
    world.multiworld.regions += [root]

    zen_area_one = Region("Area 1", world.player, world.multiworld)
    zen_area_two = Region("Area 2", world.player, world.multiworld)
    zen_area_three = Region("Area 3", world.player, world.multiworld)
    zen_area_four = Region("Area 4", world.player, world.multiworld)
    zen_area_five = Region("Area 5", world.player, world.multiworld)
    zen_area_six = Region("Area 6", world.player, world.multiworld)

    # This is honestly kinda messy
    zen_created_regions = {Region(name, world.player, world.multiworld): reg for name, reg in zen_regions.items()}
    zen_areas = [zen_area_one, zen_area_two, zen_area_three, zen_area_four, zen_area_five, zen_area_six]
    zen_total_regions = zen_areas
    zen_total_regions += [region for region, _ in zen_created_regions.items()]
    world.multiworld.regions += zen_total_regions

    # Set up areas first
    
    if world.options.unlock_method == 1:
        for region_area in zen_areas:
            root.connect(region_area, f"{region_area.name} Area Access", lambda state: state.has(f"{region_area.name} Unlock", world.player))
    else:
        for region_area in [zen_area_one, zen_area_two, zen_area_three, zen_area_four, zen_area_five, zen_area_six]:
            print(f"Connecting {region_area.name} to root")
            root.connect(region_area, f"{region_area.name} Area Access")


    # Then stages
    for region, area in zen_created_regions.items():
        match area:
            case 1:
                if world.options.unlock_method == 0: zen_area_one.connect(region, f"{region.name} Stage Access", lambda state: state.has(f"{region.name} Unlock", world.player))
                else: zen_area_one.connect(region, f"{region.name} Stage Access")
            case 2:
                if world.options.unlock_method == 0: zen_area_two.connect(region, f"{region.name} Stage Access", lambda state: state.has(f"{region.name} Unlock", world.player))
                else: zen_area_two.connect(region, f"{region.name} Stage Access")
            case 3:
                if world.options.unlock_method == 0: zen_area_three.connect(region, f"{region.name} Stage Access", lambda state: state.has(f"{region.name} Unlock", world.player))
                else: zen_area_three.connect(region, f"{region.name} Stage Access")
            case 4:
                if world.options.unlock_method == 0: zen_area_four.connect(region, f"{region.name} Stage Access", lambda state: state.has(f"{region.name} Unlock", world.player))
                else: zen_area_four.connect(region, f"{region.name} Stage Access")
            case 5:
                if world.options.unlock_method == 0: zen_area_five.connect(region, f"{region.name} Stage Access", lambda state: state.has(f"{region.name} Unlock", world.player))
                else: zen_area_five.connect(region, f"{region.name} Stage Access")
            case 6:
                if world.options.unlock_method == 0: zen_area_six.connect(region, f"{region.name} Stage Access", lambda state: state.has(f"{region.name} Unlock", world.player))
                else: zen_area_six.connect(region, f"{region.name} Stage Access")
            case 7:
                root.connect(region, f"{region.name} Stage Access", lambda state: state.has(f"{region.name} Unlock", world.player))

    # Repeat for effect mode (if enabled)
    if world.options.is_include_effect:
        classic_region: Region = None
        relax_region: Region = None
        focus_region: Region = None
        adventure_region: Region = None
        if not "Classic" in world.options.excluded_modes:
            classic_region = Region("Classic Modes", world.player, world.multiworld, "Classic Effects")
        if not "Relax" in world.options.excluded_modes:
            relax_region = Region("Relax Modes", world.player, world.multiworld, "Relax Effects")
        if not "Focus" in world.options.excluded_modes:
            focus_region = Region("Focus Modes", world.player, world.multiworld, "Focus Effects")
        if not "Adventorous" in world.options.excluded_modes:
            adventure_region = Region("Adventorous Modes", world.player, world.multiworld, "Adventorous Effects")
        group_regions = [classic_region, relax_region, focus_region, adventure_region]

        for region in group_regions:
            if region is None: continue
            world.multiworld.regions += [region]
            if world.options.unlock_method == 0:
                root.connect(region, f"{region.name} Access")
            else:
                root.connect(region, f"{region.name} Access", lambda state: state.has(f"Effect: {region.name} Unlock", world.player))
            


        created_effec_regions = {Region(name, world.player, world.multiworld): area for name, area in get_effect_regions(world).items() if group_regions[area-1] is not None}
        world.multiworld.regions += [region for region, _ in created_effec_regions.items()]

        for region, area in created_effec_regions.items():
            if world.options.unlock_method == 0:
                group_regions[area-1].connect(region, f"{region.name} Access")
            else:
                group_regions[area-1].connect(region, f"{region.name} Access")



