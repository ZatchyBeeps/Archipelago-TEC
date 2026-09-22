from __future__ import annotations

from typing import NamedTuple, TYPE_CHECKING, Dict

from BaseClasses import Location

if TYPE_CHECKING:
    from .__init__ import TECWorld

from . import items

class TECLocation(Location):
    game = "Tetris Effect: Connected"


offset = 57000


class TECLoc_Data(NamedTuple):
    location_id: int
    region: str | None
    in_area: str | None
    identifier: list[str]

    
def create_locations(world: TECWorld):
    root = world.get_region("Menu")
    for name, data in base_locations.items():
        region = world.get_region(data.region)
        region.locations.append(TECLocation(world.player, name, data.location_id + offset, region))

    if world.options.is_include_effect:
        for name, data in effect_mode_locations.items():
            if not can_location_exist(world, name, 0): continue
            region = world.get_region(data.region)
            region.locations.append(TECLocation(world.player, name, data.location_id + offset, region))

    if world.options.is_ranksanity:
        for name, data in get_available_ranksanities(world).items():
            region = world.get_region(data.region)
            region.locations.append(TECLocation(world.player, name, data.location_id + offset, region))

        if world.options.is_include_effect:
            for name, data in get_available_effect_ranksanities(world).items():
                if not can_location_exist(world, name, 1): continue
                region = world.get_region(data.region)
                region.locations.append( TECLocation(world.player, name, data.location_id + offset, region))

    trick_locations: Dict[str, int]
    # Add trick locations
    # Maybe...? 
    trick_locations = {f"Perform {10 * world.options.tspins_n} T-Spins": 1000 + n + offset for n in range(world.options.tspins_n-1)}

    root.locations += [TECLocation(world.player, name, data, root) for name, data in trick_locations.items()]


    world.get_region("Metamorphosis").add_event("Zen Mode Cleared", "Victory", lambda state: state.has("Metamorphosis Unlock", world.player), TECLocation, items.TECItem)


def can_location_exist(world: TECWorld, location: str, type: int = 0):
    match (type):
        case 0: # Effect mode exclusions
            for mode in world.options.excluded_modes:
                #print(f"Comparing {mode} with {location} containing {effect_mode_locations[location].identifier}")
                if mode in effect_mode_locations[location].identifier or mode == effect_mode_locations[location].in_area:
                    return False
            return True
        case 1: # Ranksanity max rank
            for mode in world.options.excluded_modes:
                if mode in effect_ranksanity_locations[location].identifier or mode == effect_ranksanity_locations[location].in_area:
                    return False
            return True

    return False


def get_available_ranksanities(world: TECWorld) -> Dict[str, TECLoc_Data]:
    locations = zen_areas_ranksanity_basis
    if world.options.ranksanity_limit >= 1: locations.update( zen_areas_ranksanity_B)
    if world.options.ranksanity_limit >= 2: locations.update( zen_areas_ranksanity_A)
    if world.options.ranksanity_limit >= 3: locations.update( zen_areas_ranksanity_S)
    if world.options.ranksanity_limit >= 4: locations.update( zen_areas_ranksanity_SS)
    return locations

def get_available_effect_ranksanities(world: TECWorld) -> dict[str, TECLoc_Data]:
    locations = {name: data for name, data in effect_ranksanity_locations.items() if "E Rank" in data.identifier or "D Rank" in data.identifier or "C Rank" in data.identifier}
    if world.options.ranksanity_limit >= 1: locations.update( {name: data for name, data in effect_ranksanity_locations.items() if "B Rank" in data.identifier})
    if world.options.ranksanity_limit >= 2: locations.update( {name: data for name, data in effect_ranksanity_locations.items() if "A Rank" in data.identifier})
    if world.options.ranksanity_limit >= 3: locations.update( {name: data for name, data in effect_ranksanity_locations.items() if "S Rank" in data.identifier})
    if world.options.ranksanity_limit >= 4: locations.update( {name: data for name, data in effect_ranksanity_locations.items() if "SS Rank" in data.identifier})
    return locations


def get_location_table() -> dict[str, int]:
    result_table = {name: data.location_id + offset for name, data in base_locations.items()}
    result_table.update( {name: data.location_id + offset for name, data in effect_mode_locations.items()})
    result_table.update( {name: data.location_id + offset for name, data in zen_ranksanity_locations.items()})
    result_table.update( {name: data.location_id + offset for name, data in effect_ranksanity_locations.items()})
    result_table.update( {"Perform 10 T-spins": 1000 + n + offset for n in range(49)})
    # Add the rest of the trick locations later
    return result_table



# We use the location data to set on which level the location belongs to, and to what area said location goes into
# Through rule definition the multiworld will know if the levels are reachable by having an area, or individually by having the level
base_locations = {
    'The Deep Stage Cleared':             TECLoc_Data( 10, "The Deep", "Area 1", {}),
    'Pharaoh\'s Code Stage Cleared':      TECLoc_Data( 11, "Pharaoh\'s Code", "Area 1", {}),
    'Karma Wheel Stage Cleared':          TECLoc_Data( 12, "Karma Wheel", "Area 1", {}),
    'Jellyfish Chorus Stage Cleared':     TECLoc_Data( 13, "Jellyfish Chorus", "Area 2", {}),
    'Da Vinci Stage Cleared':             TECLoc_Data( 14, "Da Vinci", "Area 2", {}),
    'Prayer Circles Stage Cleared':       TECLoc_Data( 15, "Prayer Circles", "Area 2", {}),
    'Ritual Passion Stage Cleared':       TECLoc_Data( 16, "Ritual Passion", "Area 2", {}),
    'Deserted Stage Cleared':             TECLoc_Data( 17, "Deserted", "Area 3", {}),
    'Dolphin Surf Stage Cleared':         TECLoc_Data( 18, "Dolphin Surf", "Area 3", {}),
    'Downtown Jazz Stage Cleared':        TECLoc_Data( 19, "Downtown Jazz", "Area 3", {}),
    'Spirit Canyon Stage Cleared':        TECLoc_Data( 20, "Spirit Canyon", "Area 3", {}),
    'Jewel Veil Stage Cleared':           TECLoc_Data( 21, "Jewel Veil", "Area 4", {}),
    'Forest Dawn Stage Cleared':          TECLoc_Data( 22, "Forest Dawn", "Area 4", {}),
    'Kaleidoscope Stage Cleared':         TECLoc_Data( 23, "Kaleidoscope", "Area 4", {}),
    'Turtle Dreams Stage Cleared':        TECLoc_Data( 24, "Turtle Dreams", "Area 4", {}),
    'Celebration Stage Cleared':          TECLoc_Data( 25, "Celebration", "Area 4", {}),
    'Sunset Breeze Stage Cleared':        TECLoc_Data( 26, "Sunset Breeze", "Area 5", {}),
    'Aurora Peak Stage Cleared':          TECLoc_Data( 27, "Aurora Peak", "Area 5", {}),
    'Zen Blossoms Stage Cleared':         TECLoc_Data( 28, "Zen Blossoms", "Area 5", {}),
    'Ying & Yang Stage Cleared':          TECLoc_Data( 29, "Ying & Yang", "Area 5", {}),
    'Hula Soul Stage Cleared':            TECLoc_Data( 30, "Hula Soul", "Area 5", {}),
    'Starfall Stage Cleared':             TECLoc_Data( 31, "Starfall", "Area 6", {}),
    'Balloon High Stage Cleared':         TECLoc_Data( 32, "Balloon High", "Area 6", {}),
    'Mermaid Cove Stage Cleared':         TECLoc_Data( 33, "Mermaid Cove", "Area 6", {}),
    'Orbit Stage Cleared':                TECLoc_Data( 34, "Orbit", "Area 6", {}),
    'Stratosphere Stage Cleared':         TECLoc_Data( 35, "Stratosphere", "Area 6", {}),
    'Metamorphosis Stage Cleared':        TECLoc_Data( 36, "Metamorphosis", None, {})
}

effect_mode_locations = {
    'Marathon Mode Cleared':             TECLoc_Data( 40, "Marathon Mode", "Classic Effect Modes", {"Marathon"}),
    'Zone Marathon Mode Cleared':        TECLoc_Data( 41, "Zone Marathon Mode", "Classic Effect Modes", {"Zone Marathon"}),
    'Ultra Mode Cleared':                TECLoc_Data( 42, "Ultra Mode", "Classic Effect Modes", {"Ultra"}),
    'Sprint Mode Cleared':               TECLoc_Data( 43, "Sprint Mode", "Classic Effect Modes", {"Sprint"}),
    'Master Mode Cleared':               TECLoc_Data( 44, "Master Mode", "Classic Effect Modes", {"Master"}),
    'Classic Score Attack Mode Cleared': TECLoc_Data( 45, "Classic Score Attack Mode", "Classic Effect Modes", {"Classic Score Attack"}),
    'Chill Marathon Mode Cleared':       TECLoc_Data( 46, "Chill Marathon Mode", "Relax Effect Modes", {"Chill Marathon"}),
    'Quick Play Mode Cleared':           TECLoc_Data( 47, "Quick Play Mode", "Relax Effect Modes", {"Quick Play"}),
    'Playlist (Sea) Mode Cleared':       TECLoc_Data( 48, "Sea Playlist Mode", "Relax Effect Modes", {"Playlist (Sea)"}),
    'Playlist (Wind) Mode Cleared':      TECLoc_Data( 49, "Wind Playlist Mode", "Relax Effect Modes", {"Playlist (Wind)"}),
    'Playlist (World) Mode Cleared':     TECLoc_Data( 50, "World Playlist Mode", "Relax Effect Modes", {"Playlist (World)"}),
    'All Clear Mode Cleared':            TECLoc_Data( 51, "All Clear Mode", "Focus Effect Modes", {"All Clear"}),
    'Combo Mode Cleared':                TECLoc_Data( 52, "Combo Mode", "Focus Effect Modes", {"Combo"}),
    'Target Mode Cleared':               TECLoc_Data( 53, "Target Mode", "Focus Effect Modes", {"Focus"}),
    'Countdown Mode Cleared':            TECLoc_Data( 54, "Countdown Mode", "Adventorous Effect Modes", {"Countdown"}),
    'Purity Mode Cleared':               TECLoc_Data( 55, "Purity Mode", "Adventorous Effect Modes", {"Purity"}),
    'Mystery Mode Cleared':              TECLoc_Data( 56, "Mystery Mode", "Adventorous Effect Modes", {"Mystery"}),
}

# This one is just for reference, we wanna dynamically create these
# Location id is the start for each one, with a limit of 50 locations each
misc_locations = {
    "Perform 10 T-spins":                  TECLoc_Data( 1000, "Menu", None, {}), 
    "Perform 10 back-to-backs":            TECLoc_Data( 1050, "Menu", None, {}), 
    "Perform 15 Tetris line clears":       TECLoc_Data( 1100, "Menu", None, {}), 
    "Perform a 10 line combo":             TECLoc_Data( 1150, "Menu", None, {}), 
    "Earn an all clear":                   TECLoc_Data( 1200, "Menu", None, {}), 
    "Perform 4 consecutive back-to-backs": TECLoc_Data( 1250, "Menu", None, {}), 
    "Earn a T-spin triple":                TECLoc_Data( 1300, "Menu", None, {}), 
    "Earn an octotris":                    TECLoc_Data( 1350, "Menu", None, {}), 
    "Earn a dodecatris":                   TECLoc_Data( 1400, "Menu", None, {}), 
    "Earn a decahexatris":                 TECLoc_Data( 1450, "Menu", None, {}), 
    "Earn a perfectris":                   TECLoc_Data( 1500, "Menu", None, {}), 
    "Earn a ultimatris":                   TECLoc_Data( 1550, "Menu", None, {}), 
    "Earn a kirbtris":                     TECLoc_Data( 1600, "Menu", None, {})
}


zen_ranksanity_locations = {
    'The Deep: E Rank':              TECLoc_Data(100, "The Deep", "Area 1",{"E Rank"}),
    'The Deep: D Rank':              TECLoc_Data(101, "The Deep", "Area 1", {"D Rank"}),
    'The Deep: C Rank':              TECLoc_Data(102, "The Deep", "Area 1", {"C Rank"}),
    'The Deep: B Rank':              TECLoc_Data(103, "The Deep", "Area 1", {"B Rank"}),
    'The Deep: A Rank':              TECLoc_Data(104, "The Deep", "Area 1", {"A Rank"}),
    'The Deep: S Rank':              TECLoc_Data(105, "The Deep", "Area 1", {"S Rank"}),
    'The Deep: SS Rank':             TECLoc_Data(106, "The Deep", "Area 1", {"SS Rank"}),
    'Pharaoh\'s Code: E Rank':       TECLoc_Data(110, "Pharaoh\'s Code", "Area 1",{"E Rank"}),
    'Pharaoh\'s Code: D Rank':       TECLoc_Data(111, "Pharaoh\'s Code", "Area 1", {"D Rank"}),
    'Pharaoh\'s Code: C Rank':       TECLoc_Data(112, "Pharaoh\'s Code", "Area 1", {"C Rank"}),
    'Pharaoh\'s Code: B Rank':       TECLoc_Data(113, "Pharaoh\'s Code", "Area 1", {"B Rank"}),
    'Pharaoh\'s Code: A Rank':       TECLoc_Data(114, "Pharaoh\'s Code", "Area 1", {"A Rank"}),
    'Pharaoh\'s Code: S Rank':       TECLoc_Data(115, "Pharaoh\'s Code", "Area 1", {"S Rank"}),
    'Pharaoh\'s Code: SS Rank':      TECLoc_Data(116, "Pharaoh\'s Code", "Area 1", {"SS Rank"}),
    'Karma Wheel: E Rank':           TECLoc_Data(120, "Karma Wheel", "Area 1",{"E Rank"}),
    'Karma Wheel: D Rank':           TECLoc_Data(121, "Karma Wheel", "Area 1", {"D Rank"}),
    'Karma Wheel: C Rank':           TECLoc_Data(122, "Karma Wheel", "Area 1", {"C Rank"}),
    'Karma Wheel: B Rank':           TECLoc_Data(123, "Karma Wheel", "Area 1", {"B Rank"}),
    'Karma Wheel: A Rank':           TECLoc_Data(124, "Karma Wheel", "Area 1", {"A Rank"}),
    'Karma Wheel: S Rank':           TECLoc_Data(125, "Karma Wheel", "Area 1", {"S Rank"}),
    'Karma Wheel: SS Rank':          TECLoc_Data(126, "Karma Wheel", "Area 1", {"SS Rank"}),
    'Jellyfish Chorus: E Rank':      TECLoc_Data(130, "Jellyfish Chorus", "Area 2",{"E Rank"}),
    'Jellyfish Chorus: D Rank':      TECLoc_Data(131, "Jellyfish Chorus", "Area 2", {"D Rank"}),
    'Jellyfish Chorus: C Rank':      TECLoc_Data(132, "Jellyfish Chorus", "Area 2", {"C Rank"}),
    'Jellyfish Chorus: B Rank':      TECLoc_Data(133, "Jellyfish Chorus", "Area 2", {"B Rank"}),
    'Jellyfish Chorus: A Rank':      TECLoc_Data(134, "Jellyfish Chorus", "Area 2", {"A Rank"}),
    'Jellyfish Chorus: S Rank':      TECLoc_Data(135, "Jellyfish Chorus", "Area 2", {"S Rank"}),
    'Jellyfish Chorus: SS Rank':     TECLoc_Data(136, "Jellyfish Chorus", "Area 2", {"SS Rank"}),
    'Da Vinci: E Rank':              TECLoc_Data(140, "Da Vinci", "Area 2",{"E Rank"}),
    'Da Vinci: D Rank':              TECLoc_Data(141, "Da Vinci", "Area 2", {"D Rank"}),
    'Da Vinci: C Rank':              TECLoc_Data(142, "Da Vinci", "Area 2", {"C Rank"}),
    'Da Vinci: B Rank':              TECLoc_Data(143, "Da Vinci", "Area 2", {"B Rank"}),
    'Da Vinci: A Rank':              TECLoc_Data(144, "Da Vinci", "Area 2", {"A Rank"}),
    'Da Vinci: S Rank':              TECLoc_Data(145, "Da Vinci", "Area 2", {"S Rank"}),
    'Da Vinci: SS Rank':             TECLoc_Data(146, "Da Vinci", "Area 2", {"SS Rank"}),
    'Prayer Circles: E Rank':        TECLoc_Data(150, "Prayer Circles", "Area 2",{"E Rank"}),
    'Prayer Circles: D Rank':        TECLoc_Data(151, "Prayer Circles", "Area 2", {"D Rank"}),
    'Prayer Circles: C Rank':        TECLoc_Data(152, "Prayer Circles", "Area 2", {"C Rank"}),
    'Prayer Circles: B Rank':        TECLoc_Data(153, "Prayer Circles", "Area 2", {"B Rank"}),
    'Prayer Circles: A Rank':        TECLoc_Data(154, "Prayer Circles", "Area 2", {"A Rank"}),
    'Prayer Circles: S Rank':        TECLoc_Data(155, "Prayer Circles", "Area 2", {"S Rank"}),
    'Prayer Circles: SS Rank':       TECLoc_Data(156, "Prayer Circles", "Area 2", {"SS Rank"}),
    'Ritual Passion: E Rank':        TECLoc_Data(160, "Ritual Passion", "Area 2",{"E Rank"}),
    'Ritual Passion: D Rank':        TECLoc_Data(161, "Ritual Passion", "Area 2", {"D Rank"}),
    'Ritual Passion: C Rank':        TECLoc_Data(162, "Ritual Passion", "Area 2", {"C Rank"}),
    'Ritual Passion: B Rank':        TECLoc_Data(163, "Ritual Passion", "Area 2", {"B Rank"}),
    'Ritual Passion: A Rank':        TECLoc_Data(164, "Ritual Passion", "Area 2", {"A Rank"}),
    'Ritual Passion: S Rank':        TECLoc_Data(165, "Ritual Passion", "Area 2", {"S Rank"}),
    'Ritual Passion: SS Rank':       TECLoc_Data(166, "Ritual Passion", "Area 2", {"SS Rank"}),
    'Deserted: E Rank':              TECLoc_Data(170, "Deserted", "Area 3",{"E Rank"}),
    'Deserted: D Rank':              TECLoc_Data(171, "Deserted", "Area 3", {"D Rank"}),
    'Deserted: C Rank':              TECLoc_Data(172, "Deserted", "Area 3", {"C Rank"}),
    'Deserted: B Rank':              TECLoc_Data(173, "Deserted", "Area 3", {"B Rank"}),
    'Deserted: A Rank':              TECLoc_Data(174, "Deserted", "Area 3", {"A Rank"}),
    'Deserted: S Rank':              TECLoc_Data(175, "Deserted", "Area 3", {"S Rank"}),
    'Deserted: SS Rank':             TECLoc_Data(176, "Deserted", "Area 3", {"SS Rank"}),
    'Dolphin Surf: E Rank':          TECLoc_Data(180, "Dolphin Surf", "Area 3",{"E Rank"}),
    'Dolphin Surf: D Rank':          TECLoc_Data(181, "Dolphin Surf", "Area 3", {"D Rank"}),
    'Dolphin Surf: C Rank':          TECLoc_Data(182, "Dolphin Surf", "Area 3", {"C Rank"}),
    'Dolphin Surf: B Rank':          TECLoc_Data(183, "Dolphin Surf", "Area 3", {"B Rank"}),
    'Dolphin Surf: A Rank':          TECLoc_Data(184, "Dolphin Surf", "Area 3", {"A Rank"}),
    'Dolphin Surf: S Rank':          TECLoc_Data(185, "Dolphin Surf", "Area 3", {"S Rank"}),
    'Dolphin Surf: SS Rank':         TECLoc_Data(186, "Dolphin Surf", "Area 3", {"SS Rank"}),
    'Downtown Jazz: E Rank':         TECLoc_Data(190, "Downtown Jazz", "Area 3",{"E Rank"}),
    'Downtown Jazz: D Rank':         TECLoc_Data(191, "Downtown Jazz", "Area 3", {"D Rank"}),
    'Downtown Jazz: C Rank':         TECLoc_Data(192, "Downtown Jazz", "Area 3", {"C Rank"}),
    'Downtown Jazz: B Rank':         TECLoc_Data(193, "Downtown Jazz", "Area 3", {"B Rank"}),
    'Downtown Jazz: A Rank':         TECLoc_Data(194, "Downtown Jazz", "Area 3", {"A Rank"}),
    'Downtown Jazz: S Rank':         TECLoc_Data(195, "Downtown Jazz", "Area 3", {"S Rank"}),
    'Downtown Jazz: SS Rank':        TECLoc_Data(196, "Downtown Jazz", "Area 3", {"SS Rank"}),
    'Spirit Canyon: E Rank':         TECLoc_Data(200, "Spirit Canyon", "Area 3",{"E Rank"}),
    'Spirit Canyon: D Rank':         TECLoc_Data(201, "Spirit Canyon", "Area 3", {"D Rank"}),
    'Spirit Canyon: C Rank':         TECLoc_Data(202, "Spirit Canyon", "Area 3", {"C Rank"}),
    'Spirit Canyon: B Rank':         TECLoc_Data(203, "Spirit Canyon", "Area 3", {"B Rank"}),
    'Spirit Canyon: A Rank':         TECLoc_Data(204, "Spirit Canyon", "Area 3", {"A Rank"}),
    'Spirit Canyon: S Rank':         TECLoc_Data(205, "Spirit Canyon", "Area 3", {"S Rank"}),
    'Spirit Canyon: SS Rank':        TECLoc_Data(206, "Spirit Canyon", "Area 3", {"SS Rank"}),
    'Jewel Veil: E Rank':            TECLoc_Data(210, "Jewel Veil", "Area 4",{"E Rank"}),
    'Jewel Veil: D Rank':            TECLoc_Data(211, "Jewel Veil", "Area 4", {"D Rank"}),
    'Jewel Veil: C Rank':            TECLoc_Data(212, "Jewel Veil", "Area 4", {"C Rank"}),
    'Jewel Veil: B Rank':            TECLoc_Data(213, "Jewel Veil", "Area 4", {"B Rank"}),
    'Jewel Veil: A Rank':            TECLoc_Data(214, "Jewel Veil", "Area 4", {"A Rank"}),
    'Jewel Veil: S Rank':            TECLoc_Data(215, "Jewel Veil", "Area 4", {"S Rank"}),
    'Jewel Veil: SS Rank':           TECLoc_Data(216, "Jewel Veil", "Area 4", {"SS Rank"}),
    'Forest Dawn: E Rank':           TECLoc_Data(220, "Forest Dawn", "Area 4",{"E Rank"}),
    'Forest Dawn: D Rank':           TECLoc_Data(221, "Forest Dawn", "Area 4", {"D Rank"}),
    'Forest Dawn: C Rank':           TECLoc_Data(222, "Forest Dawn", "Area 4", {"C Rank"}),
    'Forest Dawn: B Rank':           TECLoc_Data(223, "Forest Dawn", "Area 4", {"B Rank"}),
    'Forest Dawn: A Rank':           TECLoc_Data(224, "Forest Dawn", "Area 4", {"A Rank"}),
    'Forest Dawn: S Rank':           TECLoc_Data(225, "Forest Dawn", "Area 4", {"S Rank"}),
    'Forest Dawn: SS Rank':          TECLoc_Data(226, "Forest Dawn", "Area 4", {"SS Rank"}),
    'Kaleidoscope: E Rank':          TECLoc_Data(230, "Kaleidoscope", "Area 4",{"E Rank"}),
    'Kaleidoscope: D Rank':          TECLoc_Data(231, "Kaleidoscope", "Area 4", {"D Rank"}),
    'Kaleidoscope: C Rank':          TECLoc_Data(232, "Kaleidoscope", "Area 4", {"C Rank"}),
    'Kaleidoscope: B Rank':          TECLoc_Data(233, "Kaleidoscope", "Area 4", {"B Rank"}),
    'Kaleidoscope: A Rank':          TECLoc_Data(234, "Kaleidoscope", "Area 4", {"A Rank"}),
    'Kaleidoscope: S Rank':          TECLoc_Data(235, "Kaleidoscope", "Area 4", {"S Rank"}),
    'Kaleidoscope: SS Rank':         TECLoc_Data(236, "Kaleidoscope", "Area 4", {"SS Rank"}),
    'Turtle Dreams: E Rank':         TECLoc_Data(240, "Turtle Dreams", "Area 4",{"E Rank"}),
    'Turtle Dreams: D Rank':         TECLoc_Data(241, "Turtle Dreams", "Area 4", {"D Rank"}),
    'Turtle Dreams: C Rank':         TECLoc_Data(242, "Turtle Dreams", "Area 4", {"C Rank"}),
    'Turtle Dreams: B Rank':         TECLoc_Data(243, "Turtle Dreams", "Area 4", {"B Rank"}),
    'Turtle Dreams: A Rank':         TECLoc_Data(244, "Turtle Dreams", "Area 4", {"A Rank"}),
    'Turtle Dreams: S Rank':         TECLoc_Data(245, "Turtle Dreams", "Area 4", {"S Rank"}),
    'Turtle Dreams: SS Rank':        TECLoc_Data(246, "Turtle Dreams", "Area 4", {"SS Rank"}),
    'Celebration: E Rank':           TECLoc_Data(250, "Celebration", "Area 4",{"E Rank"}),
    'Celebration: D Rank':           TECLoc_Data(251, "Celebration", "Area 4", {"D Rank"}),
    'Celebration: C Rank':           TECLoc_Data(252, "Celebration", "Area 4", {"C Rank"}),
    'Celebration: B Rank':           TECLoc_Data(253, "Celebration", "Area 4", {"B Rank"}),
    'Celebration: A Rank':           TECLoc_Data(254, "Celebration", "Area 4", {"A Rank"}),
    'Celebration: S Rank':           TECLoc_Data(255, "Celebration", "Area 4", {"S Rank"}),
    'Celebration: SS Rank':          TECLoc_Data(256, "Celebration", "Area 4", {"SS Rank"}),
    'Sunset Breeze: E Rank':         TECLoc_Data(260, "Sunset Breeze", "Area 5",{"E Rank"}),
    'Sunset Breeze: D Rank':         TECLoc_Data(261, "Sunset Breeze", "Area 5", {"D Rank"}),
    'Sunset Breeze: C Rank':         TECLoc_Data(262, "Sunset Breeze", "Area 5", {"C Rank"}),
    'Sunset Breeze: B Rank':         TECLoc_Data(263, "Sunset Breeze", "Area 5", {"B Rank"}),
    'Sunset Breeze: A Rank':         TECLoc_Data(264, "Sunset Breeze", "Area 5", {"A Rank"}),
    'Sunset Breeze: S Rank':         TECLoc_Data(265, "Sunset Breeze", "Area 5", {"S Rank"}),
    'Sunset Breeze: SS Rank':        TECLoc_Data(266, "Sunset Breeze", "Area 5", {"SS Rank"}),
    'Aurora Peak: E Rank':           TECLoc_Data(270, "Aurora Peak", "Area 5",{"E Rank"}),
    'Aurora Peak: D Rank':           TECLoc_Data(271, "Aurora Peak", "Area 5", {"D Rank"}),
    'Aurora Peak: C Rank':           TECLoc_Data(272, "Aurora Peak", "Area 5", {"C Rank"}),
    'Aurora Peak: B Rank':           TECLoc_Data(273, "Aurora Peak", "Area 5", {"B Rank"}),
    'Aurora Peak: A Rank':           TECLoc_Data(274, "Aurora Peak", "Area 5", {"A Rank"}),
    'Aurora Peak: S Rank':           TECLoc_Data(275, "Aurora Peak", "Area 5", {"S Rank"}),
    'Aurora Peak: SS Rank':          TECLoc_Data(276, "Aurora Peak", "Area 5", {"SS Rank"}),
    'Zen Blossoms: E Rank':          TECLoc_Data(280, "Zen Blossoms", "Area 5",{"E Rank"}),
    'Zen Blossoms: D Rank':          TECLoc_Data(281, "Zen Blossoms", "Area 5", {"D Rank"}),
    'Zen Blossoms: C Rank':          TECLoc_Data(282, "Zen Blossoms", "Area 5", {"C Rank"}),
    'Zen Blossoms: B Rank':          TECLoc_Data(283, "Zen Blossoms", "Area 5", {"B Rank"}),
    'Zen Blossoms: A Rank':          TECLoc_Data(284, "Zen Blossoms", "Area 5", {"A Rank"}),
    'Zen Blossoms: S Rank':          TECLoc_Data(285, "Zen Blossoms", "Area 5", {"S Rank"}),
    'Zen Blossoms: SS Rank':         TECLoc_Data(286, "Zen Blossoms", "Area 5", {"SS Rank"}),
    'Ying & Yang: E Rank':           TECLoc_Data(290, "Ying & Yang", "Area 5",{"E Rank"}),
    'Ying & Yang: D Rank':           TECLoc_Data(291, "Ying & Yang", "Area 5", {"D Rank"}),
    'Ying & Yang: C Rank':           TECLoc_Data(292, "Ying & Yang", "Area 5", {"C Rank"}),
    'Ying & Yang: B Rank':           TECLoc_Data(293, "Ying & Yang", "Area 5", {"B Rank"}),
    'Ying & Yang: A Rank':           TECLoc_Data(294, "Ying & Yang", "Area 5", {"A Rank"}),
    'Ying & Yang: S Rank':           TECLoc_Data(295, "Ying & Yang", "Area 5", {"S Rank"}),
    'Ying & Yang: SS Rank':          TECLoc_Data(296, "Ying & Yang", "Area 5", {"SS Rank"}),
    'Hula Soul: E Rank':             TECLoc_Data(300, "Hula Soul", "Area 5",{"E Rank"}),
    'Hula Soul: D Rank':             TECLoc_Data(301, "Hula Soul", "Area 5", {"D Rank"}),
    'Hula Soul: C Rank':             TECLoc_Data(302, "Hula Soul", "Area 5", {"C Rank"}),
    'Hula Soul: B Rank':             TECLoc_Data(303, "Hula Soul", "Area 5", {"B Rank"}),
    'Hula Soul: A Rank':             TECLoc_Data(304, "Hula Soul", "Area 5", {"A Rank"}),
    'Hula Soul: S Rank':             TECLoc_Data(305, "Hula Soul", "Area 5", {"S Rank"}),
    'Hula Soul: SS Rank':            TECLoc_Data(306, "Hula Soul", "Area 5", {"SS Rank"}),
    'Starfall: E Rank':              TECLoc_Data(310, "Starfall", "Area 6",{"E Rank"}),
    'Starfall: D Rank':              TECLoc_Data(311, "Starfall", "Area 6", {"D Rank"}),
    'Starfall: C Rank':              TECLoc_Data(312, "Starfall", "Area 6", {"C Rank"}),
    'Starfall: B Rank':              TECLoc_Data(313, "Starfall", "Area 6", {"B Rank"}),
    'Starfall: A Rank':              TECLoc_Data(314, "Starfall", "Area 6", {"A Rank"}),
    'Starfall: S Rank':              TECLoc_Data(315, "Starfall", "Area 6", {"S Rank"}),
    'Starfall: SS Rank':             TECLoc_Data(316, "Starfall", "Area 6", {"SS Rank"}),
    'Balloon High: E Rank':          TECLoc_Data(320, "Balloon High", "Area 6",{"E Rank"}),
    'Balloon High: D Rank':          TECLoc_Data(321, "Balloon High", "Area 6", {"D Rank"}),
    'Balloon High: C Rank':          TECLoc_Data(322, "Balloon High", "Area 6", {"C Rank"}),
    'Balloon High: B Rank':          TECLoc_Data(323, "Balloon High", "Area 6", {"B Rank"}),
    'Balloon High: A Rank':          TECLoc_Data(324, "Balloon High", "Area 6", {"A Rank"}),
    'Balloon High: S Rank':          TECLoc_Data(325, "Balloon High", "Area 6", {"S Rank"}),
    'Balloon High: SS Rank':         TECLoc_Data(326, "Balloon High", "Area 6", {"SS Rank"}),
    'Mermaid Cove: E Rank':          TECLoc_Data(330, "Mermaid Cove", "Area 6",{"E Rank"}),
    'Mermaid Cove: D Rank':          TECLoc_Data(331, "Mermaid Cove", "Area 6", {"D Rank"}),
    'Mermaid Cove: C Rank':          TECLoc_Data(332, "Mermaid Cove", "Area 6", {"C Rank"}),
    'Mermaid Cove: B Rank':          TECLoc_Data(333, "Mermaid Cove", "Area 6", {"B Rank"}),
    'Mermaid Cove: A Rank':          TECLoc_Data(334, "Mermaid Cove", "Area 6", {"A Rank"}),
    'Mermaid Cove: S Rank':          TECLoc_Data(335, "Mermaid Cove", "Area 6", {"S Rank"}),
    'Mermaid Cove: SS Rank':         TECLoc_Data(336, "Mermaid Cove", "Area 6", {"SS Rank"}),
    'Orbit: E Rank':                 TECLoc_Data(340, "Orbit", "Area 6",{"E Rank"}),
    'Orbit: D Rank':                 TECLoc_Data(341, "Orbit", "Area 6", {"D Rank"}),
    'Orbit: C Rank':                 TECLoc_Data(342, "Orbit", "Area 6", {"C Rank"}),
    'Orbit: B Rank':                 TECLoc_Data(343, "Orbit", "Area 6", {"B Rank"}),
    'Orbit: A Rank':                 TECLoc_Data(344, "Orbit", "Area 6", {"A Rank"}),
    'Orbit: S Rank':                 TECLoc_Data(345, "Orbit", "Area 6", {"S Rank"}),
    'Orbit: SS Rank':                TECLoc_Data(346, "Orbit", "Area 6", {"SS Rank"}),
    'Stratosphere: E Rank':          TECLoc_Data(350, "Stratosphere", "Area 6",{"E Rank"}),
    'Stratosphere: D Rank':          TECLoc_Data(351, "Stratosphere", "Area 6", {"D Rank"}),
    'Stratosphere: C Rank':          TECLoc_Data(352, "Stratosphere", "Area 6", {"C Rank"}),
    'Stratosphere: B Rank':          TECLoc_Data(353, "Stratosphere", "Area 6", {"B Rank"}),
    'Stratosphere: A Rank':          TECLoc_Data(354, "Stratosphere", "Area 6", {"A Rank"}),
    'Stratosphere: S Rank':          TECLoc_Data(355, "Stratosphere", "Area 6", {"S Rank"}),
    'Stratosphere: SS Rank':         TECLoc_Data(356, "Stratosphere", "Area 6", {"SS Rank"}),
    'Metamorphosis: E Rank':         TECLoc_Data(360, "Metamorphosis", None, {"E Rank"}),
    'Metamorphosis: D Rank':         TECLoc_Data(361, "Metamorphosis", None,  {"D Rank"}),
    'Metamorphosis: C Rank':         TECLoc_Data(362, "Metamorphosis", None,  {"C Rank"}),
    'Metamorphosis: B Rank':         TECLoc_Data(363, "Metamorphosis", None,  {"B Rank"}),
    'Metamorphosis: A Rank':         TECLoc_Data(364, "Metamorphosis", None,  {"A Rank"}),
    'Metamorphosis: S Rank':         TECLoc_Data(365, "Metamorphosis", None,  {"S Rank"}),
    'Metamorphosis: SS Rank':        TECLoc_Data(366, "Metamorphosis", None,  {"SS Rank"}),

    'Area 1: E Rank':                TECLoc_Data(540, "Menu", "", {"E Rank"}),
    'Area 1: D Rank':                TECLoc_Data(541, "Menu", "", {"D Rank"}),
    'Area 1: C Rank':                TECLoc_Data(542, "Menu", "", {"C Rank"}),
    'Area 1: B Rank':                TECLoc_Data(543, "Menu", "", {"B Rank"}),
    'Area 1: A Rank':                TECLoc_Data(544, "Menu", "", {"A Rank"}),
    'Area 1: S Rank':                TECLoc_Data(545, "Menu", "", {"S Rank"}),
    'Area 1: SS Rank':               TECLoc_Data(546, "Menu", "", {"SS Rank"}),
    'Area 2: E Rank':                TECLoc_Data(550, "Menu", "", {"E Rank"}),
    'Area 2: D Rank':                TECLoc_Data(551, "Menu", "", {"D Rank"}),
    'Area 2: C Rank':                TECLoc_Data(552, "Menu", "", {"C Rank"}),
    'Area 2: B Rank':                TECLoc_Data(553, "Menu", "", {"B Rank"}),
    'Area 2: A Rank':                TECLoc_Data(554, "Menu", "", {"A Rank"}),
    'Area 2: S Rank':                TECLoc_Data(555, "Menu", "", {"S Rank"}),
    'Area 2: SS Rank':               TECLoc_Data(556, "Menu", "", {"SS Rank"}),
    'Area 3: E Rank':                TECLoc_Data(560, "Menu", "", {"E Rank"}),
    'Area 3: D Rank':                TECLoc_Data(561, "Menu", "", {"D Rank"}),
    'Area 3: C Rank':                TECLoc_Data(562, "Menu", "", {"C Rank"}),
    'Area 3: B Rank':                TECLoc_Data(563, "Menu", "", {"B Rank"}),
    'Area 3: A Rank':                TECLoc_Data(564, "Menu", "", {"A Rank"}),
    'Area 3: S Rank':                TECLoc_Data(565, "Menu", "", {"S Rank"}),
    'Area 3: SS Rank':               TECLoc_Data(566, "Menu", "", {"SS Rank"}),
    'Area 4: E Rank':                TECLoc_Data(570, "Menu", "", {"E Rank"}),
    'Area 4: D Rank':                TECLoc_Data(571, "Menu", "", {"D Rank"}),
    'Area 4: C Rank':                TECLoc_Data(572, "Menu", "", {"C Rank"}),
    'Area 4: B Rank':                TECLoc_Data(573, "Menu", "", {"B Rank"}),
    'Area 4: A Rank':                TECLoc_Data(574, "Menu", "", {"A Rank"}),
    'Area 4: S Rank':                TECLoc_Data(575, "Menu", "", {"S Rank"}),
    'Area 4: SS Rank':               TECLoc_Data(576, "Menu", "", {"SS Rank"}),
    'Area 5: E Rank':                TECLoc_Data(580, "Menu", "", {"E Rank"}),
    'Area 5: D Rank':                TECLoc_Data(581, "Menu", "", {"D Rank"}),
    'Area 5: C Rank':                TECLoc_Data(582, "Menu", "", {"C Rank"}),
    'Area 5: B Rank':                TECLoc_Data(583, "Menu", "", {"B Rank"}),
    'Area 5: A Rank':                TECLoc_Data(584, "Menu", "", {"A Rank"}),
    'Area 5: S Rank':                TECLoc_Data(585, "Menu", "", {"S Rank"}),
    'Area 5: SS Rank':               TECLoc_Data(586, "Menu", "", {"SS Rank"}),
    'Area 6: E Rank':                TECLoc_Data(590, "Menu", "", {"E Rank"}),
    'Area 6: D Rank':                TECLoc_Data(591, "Menu", "", {"D Rank"}),
    'Area 6: C Rank':                TECLoc_Data(592, "Menu", "", {"C Rank"}),
    'Area 6: B Rank':                TECLoc_Data(593, "Menu", "", {"B Rank"}),
    'Area 6: A Rank':                TECLoc_Data(594, "Menu", "", {"A Rank"}),
    'Area 6: S Rank':                TECLoc_Data(595, "Menu", "", {"S Rank"}),
    'Area 6: SS Rank':               TECLoc_Data(596, "Menu", "", {"SS Rank"})
}

effect_ranksanity_locations = {
    'Marathon: E Rank':              TECLoc_Data(370, "Marathon Mode", "Classic Effect Modes", {"E Rank", "Marathon"}),
    'Marathon: D Rank':              TECLoc_Data(371, "Marathon Mode", "Classic Effect Modes", {"D Rank", "Marathon"}),
    'Marathon: C Rank':              TECLoc_Data(372, "Marathon Mode", "Classic Effect Modes", {"C Rank", "Marathon"}),
    'Marathon: B Rank':              TECLoc_Data(373, "Marathon Mode", "Classic Effect Modes", {"B Rank", "Marathon"}),
    'Marathon: A Rank':              TECLoc_Data(374, "Marathon Mode", "Classic Effect Modes", {"A Rank", "Marathon"}),
    'Marathon: S Rank':              TECLoc_Data(375, "Marathon Mode", "Classic Effect Modes", {"S Rank", "Marathon"}),
    'Marathon: SS Rank':             TECLoc_Data(376, "Marathon Mode", "Classic Effect Modes", {"SS Rank", "Marathon"}),
    'Zone Marathon: E Rank':         TECLoc_Data(380, "Zone Marathon Mode", "Classic Effect Modes", {"E Rank", "Zone Marathon"}),
    'Zone Marathon: D Rank':         TECLoc_Data(381, "Zone Marathon Mode", "Classic Effect Modes", {"D Rank", "Zone Marathon"}),
    'Zone Marathon: C Rank':         TECLoc_Data(382, "Zone Marathon Mode", "Classic Effect Modes", {"C Rank", "Zone Marathon"}),
    'Zone Marathon: B Rank':         TECLoc_Data(383, "Zone Marathon Mode", "Classic Effect Modes", {"B Rank", "Zone Marathon"}),
    'Zone Marathon: A Rank':         TECLoc_Data(384, "Zone Marathon Mode", "Classic Effect Modes", {"A Rank", "Zone Marathon"}),
    'Zone Marathon: S Rank':         TECLoc_Data(385, "Zone Marathon Mode", "Classic Effect Modes", {"S Rank", "Zone Marathon"}),
    'Zone Marathon: SS Rank':        TECLoc_Data(386, "Zone Marathon Mode", "Classic Effect Modes", {"SS Rank", "Zone Marathon"}),
    'Ultra: E Rank':                 TECLoc_Data(390, "Ultra Mode", "Classic Effect Modes", {"E Rank", "Ultra"}),
    'Ultra: D Rank':                 TECLoc_Data(391, "Ultra Mode", "Classic Effect Modes", {"D Rank", "Ultra"}),
    'Ultra: C Rank':                 TECLoc_Data(392, "Ultra Mode", "Classic Effect Modes", {"C Rank", "Ultra"}),
    'Ultra: B Rank':                 TECLoc_Data(393, "Ultra Mode", "Classic Effect Modes", {"B Rank", "Ultra"}),
    'Ultra: A Rank':                 TECLoc_Data(394, "Ultra Mode", "Classic Effect Modes", {"A Rank", "Ultra"}),
    'Ultra: S Rank':                 TECLoc_Data(395, "Ultra Mode", "Classic Effect Modes", {"S Rank", "Ultra"}),
    'Ultra: SS Rank':                TECLoc_Data(396, "Ultra Mode", "Classic Effect Modes", {"SS Rank", "Ultra"}),
    'Sprint: E Rank':                TECLoc_Data(400, "Sprint Mode", "Classic Effect Modes", {"E Rank", "Sprint"}),
    'Sprint: D Rank':                TECLoc_Data(401, "Sprint Mode", "Classic Effect Modes", {"D Rank", "Sprint"}),
    'Sprint: C Rank':                TECLoc_Data(402, "Sprint Mode", "Classic Effect Modes", {"C Rank", "Sprint"}),
    'Sprint: B Rank':                TECLoc_Data(403, "Sprint Mode", "Classic Effect Modes", {"B Rank", "Sprint"}),
    'Sprint: A Rank':                TECLoc_Data(404, "Sprint Mode", "Classic Effect Modes", {"A Rank", "Sprint"}),
    'Sprint: S Rank':                TECLoc_Data(405, "Sprint Mode", "Classic Effect Modes", {"S Rank", "Sprint"}),
    'Sprint: SS Rank':               TECLoc_Data(406, "Sprint Mode", "Classic Effect Modes", {"SS Rank", "Sprint"}),
    'Master: E Rank':                TECLoc_Data(410, "Master Mode", "Classic Effect Modes", {"E Rank", "Master"}),
    'Master: D Rank':                TECLoc_Data(411, "Master Mode", "Classic Effect Modes", {"D Rank", "Master"}),
    'Master: C Rank':                TECLoc_Data(412, "Master Mode", "Classic Effect Modes", {"C Rank", "Master"}),
    'Master: B Rank':                TECLoc_Data(413, "Master Mode", "Classic Effect Modes", {"B Rank", "Master"}),
    'Master: A Rank':                TECLoc_Data(414, "Master Mode", "Classic Effect Modes", {"A Rank", "Master"}),
    'Master: S Rank':                TECLoc_Data(415, "Master Mode", "Classic Effect Modes", {"S Rank", "Master"}),
    'Master: SS Rank':               TECLoc_Data(416, "Master Mode", "Classic Effect Modes", {"SS Rank", "Master"}),
    'Classic Score Attack: E Rank':  TECLoc_Data(420, "Classic Score Attack Mode", "Classic Effect Modes", {"E Rank", "Classic Score Attack"}),
    'Classic Score Attack: D Rank':  TECLoc_Data(421, "Classic Score Attack Mode", "Classic Effect Modes", {"D Rank", "Classic Score Attack"}),
    'Classic Score Attack: C Rank':  TECLoc_Data(422, "Classic Score Attack Mode", "Classic Effect Modes", {"C Rank", "Classic Score Attack"}),
    'Classic Score Attack: B Rank':  TECLoc_Data(423, "Classic Score Attack Mode", "Classic Effect Modes", {"B Rank", "Classic Score Attack"}),
    'Classic Score Attack: A Rank':  TECLoc_Data(424, "Classic Score Attack Mode", "Classic Effect Modes", {"A Rank", "Classic Score Attack"}),
    'Classic Score Attack: S Rank':  TECLoc_Data(425, "Classic Score Attack Mode", "Classic Effect Modes", {"S Rank", "Classic Score Attack"}),
    'Classic Score Attack: SS Rank': TECLoc_Data(426, "Classic Score Attack Mode", "Classic Effect Modes", {"SS Rank", "Classic Score Attack"}),
    'Chill Marathon: E Rank':        TECLoc_Data(430, "Chill Marathon Mode", "Relax Effect Modes", {"E Rank", "Chill Marathon"}),
    'Chill Marathon: D Rank':        TECLoc_Data(431, "Chill Marathon Mode", "Relax Effect Modes", {"D Rank", "Chill Marathon"}),
    'Chill Marathon: C Rank':        TECLoc_Data(432, "Chill Marathon Mode", "Relax Effect Modes", {"C Rank", "Chill Marathon"}),
    'Chill Marathon: B Rank':        TECLoc_Data(433, "Chill Marathon Mode", "Relax Effect Modes", {"B Rank", "Chill Marathon"}),
    'Chill Marathon: A Rank':        TECLoc_Data(434, "Chill Marathon Mode", "Relax Effect Modes", {"A Rank", "Chill Marathon"}),
    'Chill Marathon: S Rank':        TECLoc_Data(435, "Chill Marathon Mode", "Relax Effect Modes", {"S Rank", "Chill Marathon"}),
    'Chill Marathon: SS Rank':       TECLoc_Data(436, "Chill Marathon Mode", "Relax Effect Modes", {"SS Rank", "Chill Marathon"}),
    'Quick Play: E Rank':            TECLoc_Data(440, "Quick Play Mode", "Relax Effect Modes", {"E Rank", "Quick Play"}),
    'Quick Play: D Rank':            TECLoc_Data(441, "Quick Play Mode", "Relax Effect Modes", {"D Rank", "Quick Play"}),
    'Quick Play: C Rank':            TECLoc_Data(442, "Quick Play Mode", "Relax Effect Modes", {"C Rank", "Quick Play"}),
    'Quick Play: B Rank':            TECLoc_Data(443, "Quick Play Mode", "Relax Effect Modes", {"B Rank", "Quick Play"}),
    'Quick Play: A Rank':            TECLoc_Data(444, "Quick Play Mode", "Relax Effect Modes", {"A Rank", "Quick Play"}),
    'Quick Play: S Rank':            TECLoc_Data(445, "Quick Play Mode", "Relax Effect Modes", {"S Rank", "Quick Play"}),
    'Quick Play: SS Rank':           TECLoc_Data(446, "Quick Play Mode", "Relax Effect Modes", {"SS Rank", "Quick Play"}),
    'Playlist (Sea): E Rank':        TECLoc_Data(450, "Sea Playlist Mode", "Relax Effect Modes", {"E Rank", "Playlist (Sea)"}),
    'Playlist (Sea): D Rank':        TECLoc_Data(451, "Sea Playlist Mode", "Relax Effect Modes", {"D Rank", "Playlist (Sea)"}),
    'Playlist (Sea): C Rank':        TECLoc_Data(452, "Sea Playlist Mode", "Relax Effect Modes", {"C Rank", "Playlist (Sea)"}),
    'Playlist (Sea): B Rank':        TECLoc_Data(453, "Sea Playlist Mode", "Relax Effect Modes", {"B Rank", "Playlist (Sea)"}),
    'Playlist (Sea): A Rank':        TECLoc_Data(454, "Sea Playlist Mode", "Relax Effect Modes", {"A Rank", "Playlist (Sea)"}),
    'Playlist (Sea): S Rank':        TECLoc_Data(455, "Sea Playlist Mode", "Relax Effect Modes", {"S Rank", "Playlist (Sea)"}),
    'Playlist (Sea): SS Rank':       TECLoc_Data(456, "Sea Playlist Mode", "Relax Effect Modes", {"SS Rank", "Playlist (Sea)"}),
    'Playlist (Wind): E Rank':       TECLoc_Data(460, "Wind Playlist Mode", "Relax Effect Modes", {"E Rank", "Playlist (Wind)"}),
    'Playlist (Wind): D Rank':       TECLoc_Data(461, "Wind Playlist Mode", "Relax Effect Modes", {"D Rank", "Playlist (Wind)"}),
    'Playlist (Wind): C Rank':       TECLoc_Data(462, "Wind Playlist Mode", "Relax Effect Modes", {"C Rank", "Playlist (Wind)"}),
    'Playlist (Wind): B Rank':       TECLoc_Data(463, "Wind Playlist Mode", "Relax Effect Modes", {"B Rank", "Playlist (Wind)"}),
    'Playlist (Wind): A Rank':       TECLoc_Data(464, "Wind Playlist Mode", "Relax Effect Modes", {"A Rank", "Playlist (Wind)"}),
    'Playlist (Wind): S Rank':       TECLoc_Data(465, "Wind Playlist Mode", "Relax Effect Modes", {"S Rank", "Playlist (Wind)"}),
    'Playlist (Wind): SS Rank':      TECLoc_Data(466, "Wind Playlist Mode", "Relax Effect Modes", {"SS Rank", "Playlist (Wind)"}),
    'Playlist (World): E Rank':      TECLoc_Data(470, "World Playlist Mode", "Relax Effect Modes", {"E Rank", "Playlist (World)"}),
    'Playlist (World): D Rank':      TECLoc_Data(471, "World Playlist Mode", "Relax Effect Modes", {"D Rank", "Playlist (World)"}),
    'Playlist (World): C Rank':      TECLoc_Data(472, "World Playlist Mode", "Relax Effect Modes", {"C Rank", "Playlist (World)"}),
    'Playlist (World): B Rank':      TECLoc_Data(473, "World Playlist Mode", "Relax Effect Modes", {"B Rank", "Playlist (World)"}),
    'Playlist (World): A Rank':      TECLoc_Data(474, "World Playlist Mode", "Relax Effect Modes", {"A Rank", "Playlist (World)"}),
    'Playlist (World): S Rank':      TECLoc_Data(475, "World Playlist Mode", "Relax Effect Modes", {"S Rank", "Playlist (World)"}),
    'Playlist (World): SS Rank':     TECLoc_Data(476, "World Playlist Mode", "Relax Effect Modes", {"SS Rank", "Playlist (World)"}),
    'All Clear: E Rank':             TECLoc_Data(480, "All Clear Mode", "Focus Effect Modes", {"E Rank", "All Clear"}),
    'All Clear: D Rank':             TECLoc_Data(481, "All Clear Mode", "Focus Effect Modes", {"D Rank", "All Clear"}),
    'All Clear: C Rank':             TECLoc_Data(482, "All Clear Mode", "Focus Effect Modes", {"C Rank", "All Clear"}),
    'All Clear: B Rank':             TECLoc_Data(483, "All Clear Mode", "Focus Effect Modes", {"B Rank", "All Clear"}),
    'All Clear: A Rank':             TECLoc_Data(484, "All Clear Mode", "Focus Effect Modes", {"A Rank", "All Clear"}),
    'All Clear: S Rank':             TECLoc_Data(485, "All Clear Mode", "Focus Effect Modes", {"S Rank", "All Clear"}),
    'All Clear: SS Rank':            TECLoc_Data(486, "All Clear Mode", "Focus Effect Modes", {"SS Rank", "All Clear"}),
    'Combo: E Rank':                 TECLoc_Data(490, "Combo Mode", "Focus Effect Modes", {"E Rank", "Combo"}),
    'Combo: D Rank':                 TECLoc_Data(491, "Combo Mode", "Focus Effect Modes", {"D Rank", "Combo"}),
    'Combo: C Rank':                 TECLoc_Data(492, "Combo Mode", "Focus Effect Modes", {"C Rank", "Combo"}),
    'Combo: B Rank':                 TECLoc_Data(493, "Combo Mode", "Focus Effect Modes", {"B Rank", "Combo"}),
    'Combo: A Rank':                 TECLoc_Data(494, "Combo Mode", "Focus Effect Modes", {"A Rank", "Combo"}),
    'Combo: S Rank':                 TECLoc_Data(495, "Combo Mode", "Focus Effect Modes", {"S Rank", "Combo"}),
    'Combo: SS Rank':                TECLoc_Data(496, "Combo Mode", "Focus Effect Modes", {"SS Rank", "Combo"}),
    'Target: E Rank':                TECLoc_Data(500, "Target Mode", "Focus Effect Modes", {"E Rank", "Target"}),
    'Target: D Rank':                TECLoc_Data(501, "Target Mode", "Focus Effect Modes", {"D Rank", "Target"}),
    'Target: C Rank':                TECLoc_Data(502, "Target Mode", "Focus Effect Modes", {"C Rank", "Target"}),
    'Target: B Rank':                TECLoc_Data(503, "Target Mode", "Focus Effect Modes", {"B Rank", "Target"}),
    'Target: A Rank':                TECLoc_Data(504, "Target Mode", "Focus Effect Modes", {"A Rank", "Target"}),
    'Target: S Rank':                TECLoc_Data(505, "Target Mode", "Focus Effect Modes", {"S Rank", "Target"}),
    'Target: SS Rank':               TECLoc_Data(506, "Target Mode", "Focus Effect Modes", {"SS Rank", "Target"}),
    'Countdown: E Rank':             TECLoc_Data(510, "Countdown Mode", "Adventorous Effect Modes", {"E Rank", "Countdown"}),
    'Countdown: D Rank':             TECLoc_Data(511, "Countdown Mode", "Adventorous Effect Modes", {"D Rank", "Countdown"}),
    'Countdown: C Rank':             TECLoc_Data(512, "Countdown Mode", "Adventorous Effect Modes", {"C Rank", "Countdown"}),
    'Countdown: B Rank':             TECLoc_Data(513, "Countdown Mode", "Adventorous Effect Modes", {"B Rank", "Countdown"}),
    'Countdown: A Rank':             TECLoc_Data(514, "Countdown Mode", "Adventorous Effect Modes", {"A Rank", "Countdown"}),
    'Countdown: S Rank':             TECLoc_Data(515, "Countdown Mode", "Adventorous Effect Modes", {"S Rank", "Countdown"}),
    'Countdown: SS Rank':            TECLoc_Data(516, "Countdown Mode", "Adventorous Effect Modes", {"SS Rank", "Countdown"}),
    'Purity: E Rank':                TECLoc_Data(520, "Purity Mode", "Adventorous Effect Modes", {"E Rank", "Purity"}),
    'Purity: D Rank':                TECLoc_Data(521, "Purity Mode", "Adventorous Effect Modes", {"D Rank", "Purity"}),
    'Purity: C Rank':                TECLoc_Data(522, "Purity Mode", "Adventorous Effect Modes", {"C Rank", "Purity"}),
    'Purity: B Rank':                TECLoc_Data(523, "Purity Mode", "Adventorous Effect Modes", {"B Rank", "Purity"}),
    'Purity: A Rank':                TECLoc_Data(524, "Purity Mode", "Adventorous Effect Modes", {"A Rank", "Purity"}),
    'Purity: S Rank':                TECLoc_Data(525, "Purity Mode", "Adventorous Effect Modes", {"S Rank", "Purity"}),
    'Purity: SS Rank':               TECLoc_Data(526, "Purity Mode", "Adventorous Effect Modes", {"SS Rank", "Purity"}),
    'Mystery: E Rank':               TECLoc_Data(530, "Mystery Mode", "Adventorous Effect Modes", {"E Rank", "Mystery"}),
    'Mystery: D Rank':               TECLoc_Data(531, "Mystery Mode", "Adventorous Effect Modes", {"D Rank", "Mystery"}),
    'Mystery: C Rank':               TECLoc_Data(532, "Mystery Mode", "Adventorous Effect Modes", {"C Rank", "Mystery"}),
    'Mystery: B Rank':               TECLoc_Data(533, "Mystery Mode", "Adventorous Effect Modes", {"B Rank", "Mystery"}),
    'Mystery: A Rank':               TECLoc_Data(534, "Mystery Mode", "Adventorous Effect Modes", {"A Rank", "Mystery"}),
    'Mystery: S Rank':               TECLoc_Data(535, "Mystery Mode", "Adventorous Effect Modes", {"S Rank", "Mystery"}),
    'Mystery: SS Rank':              TECLoc_Data(536, "Mystery Mode", "Adventorous Effect Modes", {"SS Rank", "Mystery"}),
}

zen_area_one = {name: data.location_id for name, data in base_locations.items() if data.in_area == "Area 1"}
zen_area_two = {name: data.location_id for name, data in base_locations.items() if data.in_area == "Area 2"}
zen_area_three = {name: data.location_id for name, data in base_locations.items() if data.in_area == "Area 3"}
zen_area_four = {name: data.location_id for name, data in base_locations.items() if data.in_area == "Area 4"}
zen_area_five = {name: data.location_id for name, data in base_locations.items() if data.in_area == "Area 5"}
zen_area_six = {name: data.location_id for name, data in base_locations.items() if data.in_area == "Area 6"}

effect_clasic = {name: data.location_id for name, data in effect_mode_locations.items() if data.in_area == "Classic Effect Modes"}
effect_relax = {name: data.location_id for name, data in effect_mode_locations.items() if data.in_area == "Relax Effect Modes"}
effect_focus = {name: data.location_id for name, data in effect_mode_locations.items() if data.in_area == "Focus Effect Modes"}
effect_adventure = {name: data.location_id for name, data in effect_mode_locations.items() if data.in_area == "Adventorous Effect Modes"}

# The minimum ranksanity was set to be C ranks, so the basis contains from E to C ranks
zen_areas_ranksanity_basis = {name: data for name, data in zen_ranksanity_locations.items() if "E Rank" in data.identifier or "D Rank" in data.identifier or "C Rank" in data.identifier}
zen_areas_ranksanity_B = {name: data for name, data in zen_ranksanity_locations.items() if "B Rank" in data.identifier}
zen_areas_ranksanity_A = {name: data for name, data in zen_ranksanity_locations.items() if "A Rank" in data.identifier}
zen_areas_ranksanity_S = {name: data for name, data in zen_ranksanity_locations.items() if "S Rank" in data.identifier}
zen_areas_ranksanity_SS = {name: data for name, data in zen_ranksanity_locations.items() if "SS Rank" in data.identifier}
