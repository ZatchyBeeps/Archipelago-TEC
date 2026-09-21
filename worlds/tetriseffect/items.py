from typing import NamedTuple, Dict
from BaseClasses import Item, ItemClassification

class TECItem(Item):
    game = "Tetris Effect: Connected"



class TItemInfo(NamedTuple):
    item_id: int
    priority: ItemClassification

                                    # ID    Progression (0 = none, 1 = useful, 2 = progressive, 3 = trap)
itemlist = {
    'The Deep Unlock':              TItemInfo(100,   ItemClassification.progression),
    'Pharaoh\'s Code Unlock':       TItemInfo(101,   ItemClassification.progression),
    'Karma Wheel Unlock':           TItemInfo(102,   ItemClassification.progression),
    'Jellyfish Chorus Unlock':      TItemInfo(103,   ItemClassification.progression),
    'Da Vinci Unlock':              TItemInfo(104,   ItemClassification.progression),
    'Prayer Circles Unlock':        TItemInfo(105,   ItemClassification.progression),
    'Ritual Passion Unlock':        TItemInfo(106,   ItemClassification.progression),
    'Deserted Unlock':              TItemInfo(107,   ItemClassification.progression),
    'Dolphin Surf Unlock':          TItemInfo(108,   ItemClassification.progression),
    'Downtown Jazz Unlock':         TItemInfo(109,   ItemClassification.progression),
    'Spirit Canyon Unlock':         TItemInfo(110,   ItemClassification.progression),
    'Jewel Veil Unlock':            TItemInfo(111,   ItemClassification.progression),
    'Forest Dawn Unlock':           TItemInfo(112,   ItemClassification.progression),
    'Kaleidoscope Unlock':          TItemInfo(113,   ItemClassification.progression),
    'Turtle Dreams Unlock':         TItemInfo(114,   ItemClassification.progression),
    'Celebration Unlock':           TItemInfo(115,   ItemClassification.progression),
    'Sunset Breeze Unlock':         TItemInfo(116,   ItemClassification.progression),
    'Aurora Peak Unlock':           TItemInfo(117,   ItemClassification.progression),
    'Zen Blossoms Unlock':          TItemInfo(118,   ItemClassification.progression),
    'Ying & Yang Unlock':           TItemInfo(119,   ItemClassification.progression),
    'Hula Soul Unlock':             TItemInfo(120,   ItemClassification.progression),
    'Starfall Unlock':              TItemInfo(121,   ItemClassification.progression),
    'Balloon High Unlock':          TItemInfo(122,   ItemClassification.progression),
    'Mermaid Cove Unlock':          TItemInfo(123,   ItemClassification.progression),
    'Orbit Unlock':                 TItemInfo(124,   ItemClassification.progression),
    'Stratosphere Unlock':          TItemInfo(125,   ItemClassification.progression),
    'Metamorphosis Unlock':         TItemInfo(126,   ItemClassification.progression),


    'Effect: Marathon Mode Unlock':              TItemInfo(127,   ItemClassification.progression),
    'Effect: Zone Marathon Mode Unlock':         TItemInfo(128,   ItemClassification.progression),
    'Effect: Ultra Mode Unlock':                 TItemInfo(129,   ItemClassification.progression),
    'Effect: Sprint Mode Unlock':                TItemInfo(130,   ItemClassification.progression),
    'Effect: Master Mode Unlock':                TItemInfo(131,   ItemClassification.progression),
    'Effect: Classic Score Attack Mode Unlock':  TItemInfo(132,   ItemClassification.progression),
    'Effect: Chill Marathon Mode Unlock':        TItemInfo(133,   ItemClassification.progression),
    'Effect: Quick Play Mode Unlock':            TItemInfo(134,   ItemClassification.progression),
    'Effect: Playlist (Sea) Mode Unlock':        TItemInfo(135,   ItemClassification.progression),
    'Effect: Playlist (Wind) Mode Unlock':       TItemInfo(136,   ItemClassification.progression),
    'Effect: Playlist (World) Mode Unlock':      TItemInfo(137,   ItemClassification.progression),
    'Effect: All Clear Mode Unlock':             TItemInfo(138,   ItemClassification.progression),
    'Effect: Combo Mode Unlock':                 TItemInfo(139,   ItemClassification.progression),
    'Effect: Target Mode Unlock':                TItemInfo(140,   ItemClassification.progression),
    'Effect: Countdown Mode Unlock':             TItemInfo(141,   ItemClassification.progression),
    'Effect: Purity Mode Unlock':                TItemInfo(142,   ItemClassification.progression),
    'Effect: Mystery Mode Unlock':               TItemInfo(143,   ItemClassification.progression),


    'Area 1 Unlock':                TItemInfo(150,   ItemClassification.progression),
    'Area 2 Unlock':                TItemInfo(151,   ItemClassification.progression),
    'Area 3 Unlock':                TItemInfo(152,   ItemClassification.progression),
    'Area 4 Unlock':                TItemInfo(153,   ItemClassification.progression),
    'Area 5 Unlock':                TItemInfo(154,   ItemClassification.progression),
    'Area 6 Unlock':                TItemInfo(155,   ItemClassification.progression),
    # Since area 7 is just Metamorphosis, it shall be unlocked via it's individual stage unlock

    'Effect: Classic Modes Unlock':         TItemInfo(156,   ItemClassification.progression),
    'Effect: Relax Modes Unlock':           TItemInfo(157,   ItemClassification.progression),
    'Effect: Focus Modes Unlock':           TItemInfo(158,   ItemClassification.progression),
    'Effect: Adventurous Modes Unlock':     TItemInfo(159,   ItemClassification.progression),


    # 161-175 reserved for Connected mode, whenever that happens

    'Zone Unlock':                          TItemInfo(180,   ItemClassification.progression),

    'T Mino Piece Unlock':                  TItemInfo(181,   ItemClassification.progression),
    'Z Mino Piece Unlock':                  TItemInfo(182,   ItemClassification.progression),
    'S Mino Piece Unlock':                  TItemInfo(183,   ItemClassification.progression),
    'O Mino Piece Unlock':                  TItemInfo(184,   ItemClassification.progression),
    'L Mino Piece Unlock':                  TItemInfo(185,   ItemClassification.progression),
    'J Mino Piece Unlock':                  TItemInfo(186,   ItemClassification.progression),
    'I Mino Piece Unlock':                  TItemInfo(187,   ItemClassification.progression),


    'Lines Trap':                           TItemInfo(200,   ItemClassification.trap),
    'Giant Mino Trap':                      TItemInfo(201,   ItemClassification.trap),
    'Broken Mino Trap':                     TItemInfo(202,   ItemClassification.trap),
    'Zone Trap':                            TItemInfo(203,   ItemClassification.trap), # Untested method, may remove
    'Ghost Piece Trap':                     TItemInfo(204,   ItemClassification.trap),
    'Hold Trap':                            TItemInfo(205,   ItemClassification.trap),
    'Queue Trap':                           TItemInfo(206,   ItemClassification.trap),
    #'IRS Trap':                            TItemInfo(207,   ItemClassification.trap), # Messes up with quick players but idk if it's worth implementing lol
    'Speed Trap':                           TItemInfo(207,   ItemClassification.trap),



    # Don't implement these until I figure out a way to prevent scores from getting saved, so it doesn't taint the player's records on their save file
    'Bonus points':                         TItemInfo(210,   ItemClassification.useful), 
    'Zone charge bonus':                    TItemInfo(211,   ItemClassification.useful),
    
    'Cosmetic effect':                      TItemInfo(212,   ItemClassification.filler),
    'Glowup':                               TItemInfo(213,   ItemClassification.filler),
    'Fake line clear':                      TItemInfo(214,   ItemClassification.filler),
    'Zone sounds':                          TItemInfo(215,   ItemClassification.filler),
    'Vibes':                                TItemInfo(216,   ItemClassification.filler), # These ones actually just do nothing
    'Feelings':                             TItemInfo(217,   ItemClassification.filler),

}


item_table = {name: data.item_id for name, data in itemlist.items()}
zen_levels = ['The Deep Unlock', 'Pharaoh\'s Code Unlock', 'Karma Wheel Unlock', 'Jellyfish Chorus Unlock', 'Da Vinci Unlock', 'Prayer Circles Unlock', 'Ritual Passion Unlock', 'Deserted Unlock', 'Dolphin Surf Unlock',
              'Downtown Jazz Unlock', 'Spirit Canyon Unlock', 'Jewel Veil Unlock', 'Forest Dawn Unlock', 'Kaleidoscope Unlock', 'Turtle Dreams Unlock', 'Celebration Unlock', 'Sunset Breeze Unlock', 'Aurora Peak Unlock',
              'Zen Blossoms Unlock', 'Ying & Yang Unlock', 'Hula Soul Unlock', 'Starfall Unlock', 'Balloon High Unlock', 'Mermaid Cove Unlock', 'Orbit Unlock', 'Stratosphere Unlock', 'Metamorphosis Unlock']
effect_classic_levels = ['Effect: Marathon Mode Unlock', 'Effect: Zone Marathon Mode Unlock', 'Effect: Ultra Mode Unlock', 'Effect: Sprint Mode Unlock', 'Effect: Master Mode Unlock', 'Effect: Classic Score Attack Mode Unlock']
effect_relax_levels = ['Effect: Chill Marathon Mode Unlock', 'Effect: Quick Play Mode Unlock', 'Effect: Playlist (Sea) Mode Unlock', 'Effect: Playlist (Wind) Mode Unlock', 'Effect: Playlist (World) Mode Unlock']
effect_focus_levels = ['Effect: All Clear Mode Unlock', 'Effect: Combo Mode Unlock', 'Effect: Target Mode Unlock']
effect_adventure_levels = ['Effect: Countdown Mode Unlock', 'Effect: Purity Mode Unlock', 'Effect: Mystery Mode Unlock']
zen_areas = ['Area 1 Unlock', 'Area 2 Unlock', 'Area 3 Unlock', 'Area 4 Unlock', 'Area 5 Unlock', 'Area 6 Unlock']
effect_groups = ['Effect: Classic Modes Unlock', 'Effect: Relax Modes Unlock', 'Effect: Focus Modes Unlock', 'Effect: Adventurous Modes Unlock']
tetrimino_items = ['T Mino Piece Unlock', 'Z Mino Piece Unlock', 'S Mino Piece Unlock', 'O Mino Piece Unlock', 'L Mino Piece Unlock', 'J Mino Piece Unlock', 'J Mino Piece Unlock']
traps = ['Lines Trap', 'Giant Mino Trap', 'Broken Mino Trap', 'Zone Trap', 'Ghost Piece Trap', 'Hold Trap', 'Queue Trap', 'Speed Trap']
garbage = ['Bonus points', 'Zone charge bonus', 'Cosmetic effect', 'Glowup', 'Fake line clear', 'Zone sounds', 'Vibes', 'Feelings']