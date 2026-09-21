from dataclasses import dataclass

from Options import OptionGroup, Toggle, Range, Choice, PerGameCommonOptions, OptionSet, DefaultOnToggle, OptionCounter

class UnlockMethod(Choice):
    """Sets how do you want to unlock your stages. Applies to Effect mode if enabled
    
    - **Individual:** One item for each individual stage/mode is added to the multiworld
    - **Grouped:** One item for each area/mode group is added to the multiworld"""
    display_name = "Unlock Method"
    rich_text_doc = True
    option_individual = 0
    option_grouped = 1
    default = 0

class IncludeEffectMode(DefaultOnToggle):
    """Determines if the Effect game modes are included and shuffled in the multiworld"""
    display_name = "Include Effect Modes"

class ExcludedEffectModes(OptionSet):
    """Allows you to set which modes in the Effect mode will contain checks.
    By default, Master mode and Classic Score Attack are in this list. It is discouraged to do master mode unless you know what you're doing
    
    The available options are: Marathon, Zone Marathon, Ultra, Sprint, Master, Classic Score Attack, Chill Marathon, Quick Play, Sea Playlist, Wind Playlist, World Playlist,
    All Clear, Combo, Target, Countdown, Purify and Mystery.
    You may also do the following to exclude an entire group of modes: Classic, Relax, Focus and Adventorous"""
    display_name = "Excluded Effect Modes"
    valid_keys = {"Marathon", "Zone Marathon", "Ultra", "Sprint", "Master", "Classic Score Attack", "Chill Marathon", "Quick Play", "Sea Playlist", "Wind Playlist", "World Playlist", "All Clear", "Combo", "Target", "Countdown", "Purify", "Mystery", "Classic", "Relax", "Focus", "Adventorous"}
    default = {"Master", "Classic Score Attack"}

class EnableRanksanity(DefaultOnToggle):
    """Adds locations based on your rank, from E rank to SS rank (max rank can be configured below to accomodate less experienced players).
    Applies to Effect modes if it's enabled"""
    display_name = "Ranksanity"

class RanksanityMaxRank(Choice):
    """Sets up to what ranks will be counted as locations. 
    Make sure this is a rank you can consistently obtain in general or you could stale the whole multiworld"""
    display_name = "Max Rank"
    option_c_rank = 0
    option_b_rank = 1
    option_a_rank = 2
    option_s_rank = 3
    option_ss_rank = 4
    default = 3

class MinoSanity(Toggle):
    """Your mino pieces are items in the multiworld and must be obtained. This can make things like ranksanity considerably harder. 
    As of now there's no logic applied to this. Use at your own caution"""
    display_name = "Minosanity"

class StartWithZone(DefaultOnToggle):
    """The zone is an item in the multiworld that has to be obtained. Makes ranksanity harder.
    Affects the logic of zone trick locations set on the Trick Locations option"""
    display_name = "Start with Zone"

class EnableDeathLink(Choice):
    """Enable death link for this game. If you die, everyone else with it enabled also dies. Of course, the other way around also applies
    
    - **Enabled:** Normal behaviour. If you get deathlinked, you instantly top out
    - **Painful:** When deathlinked, you receive 10 lines to your board instantly
    - **Reduced:** You receive 6 lines upon deathlink, applied on the next mino drop"""
    display_name = "Death Link"
    rich_text_doc = True
    option_enabled = 0
    option_painful = 1
    option_reduced = 2
    option_disabled = 3
    default = 3


class TrapPercentage(Range):
    """Sets a percentage of how many of the filler items in your world will be traps. Setting this to 0 will disable traps"""
    display_name = "Trap Fill Percentage"
    range_start = 0
    range_end = 100
    default = 50

class TrickLocations(OptionCounter):
    """Sets an amount of locations by achieving feats as you play, allowing you to keep sending checks while waiting for a stage unlock.
    These locations are attempted to be logically evenly distributed through the first spheres of the multiworld 
    Setting values to 0 disables them"""
    display_name = "Trick Locations"
    default = {"Perform 10 T-spins": 5, "Perform 10 back-to-backs": 5, "Perform 15 Tetris line clears": 5, "Perform a 10 line combo": 5, "Earn an all clear": 3, "Perform 4 consecutive back-to-backs": 3, "Earn a T-spin triple": 0, "Earn an octotris": 20, "Earn a dodecatris": 15, "Earn a decahexatris": 7, "Earn a perfectris": 1, "Earn a ultimatris": 0, "Earn a kirbtris": 0}


class TSpinsAmmount(Range):
    """How many locations there will be by doing 10 t-spins"""
    display_name = "Do 10 T-Spins"
    range_start = 0
    range_end = 50
    default = 5

class BackToBackAmmouont(Range):
    """How many locations there will be for doing 10 back-to-backs. Back-to-backs are counted by doing 2 or more consecutive t-spins, mini t-spin or Tetris"""
    display_name = "Do 10 back-to-backs"
    range_start = 0
    range_end = 50
    default = 5

class TetrisAmmount(Range):
    """How many locations there will be by doing 15 Tetris line clears (4 lines)"""
    display_name = "Do 15 Tetris line clears"
    range_start = 0
    range_end = 50
    default = 10

class ComboAmmount(Range):
    """How many locations there will be by doing a 10 combo (clear any amount of lines 10 consecutive times)"""
    display_name = "Achieve 10 line combos"
    range_start = 0
    range_end = 50
    default = 5

class AllClearAmmount(Range):
    """How many locations there will be by achieving an All Clear (the game board is emptied by the player)"""
    display_name = "Achieve an all clear "
    range_start = 0
    range_end = 50
    default = 3

class ConsBackToBackAmmount(Range):
    """How many locations there will be by achieving a back-to-back 3 combo (do 4 t-spins, mini t-spin or Tetris in a row, the combo starts from the second consecutive clear (hence it being called a 3 combo))"""
    display_name = "Do 4 consecutive back-to-backs"
    range_start = 0
    range_end = 50
    default = 3

class TSpinTripleAmmount(Range):
    """How many locations there will be by doing a T-Spin triple. T-Spin triples are advanced so make sure you at least know how to set them up"""
    display_name = "Do a T-Spin triple"
    range_start = 0
    range_end = 50
    default = 0

class OctotrisAmmount(Range):
    """How many locations there will be by finishing a zone with 8 or more lines cleared"""
    display_name = "Do an octotris"
    range_start = 0
    range_end = 50
    default = 20

class DodecatrisAmmount(Range):
    """How many locations there will be by finishing a zone with 12 or more lines cleared"""
    display_name = "Do a dodecatris"
    range_start = 0
    range_end = 50
    default = 15

class DecahexatrisAmmount(Range):
    """How many locations there will be by finishing a zone with 16 or more lines cleared"""
    display_name = "Do a decahexatris"
    range_start = 0
    range_end = 50
    default = 5

class PerfectrisAmmount(Range):
    """How many locations there will be by finishing a zone with 18 or more lines cleared"""
    display_name = "Do a perfectris"
    range_start = 0
    range_end = 50
    default = 1

class UltimatrisAmmount(Range):
    """How many locations there will be by finishing a zone with 20 or more lines cleared. This can prove to be really difficult so be mindful when increasing this value"""
    display_name = "Do an ultimatris"
    range_start = 0
    range_end = 50
    default = 0

class KirbtrisAmmount(Range):
    """How many locations there will be by finishing a zone with 21 or more lines cleared. If you don't know how to use IRS (the Initial Rotation System) it is strongly encouraged to keep this at 0"""
    display_name = "Do a kirbtris"
    range_start = 0
    range_end = 50
    default = 0


tec_option_groups = [
    OptionGroup("Trick Locations", [
        TSpinsAmmount,
        BackToBackAmmouont,
        TetrisAmmount,
        ComboAmmount,
        AllClearAmmount,
        ConsBackToBackAmmount,
        TSpinTripleAmmount,
        OctotrisAmmount,
        DodecatrisAmmount,
        DecahexatrisAmmount,
        PerfectrisAmmount,
        UltimatrisAmmount,
        KirbtrisAmmount
    ])
]




@dataclass
class HiTheseAreGameOptions(PerGameCommonOptions):
    unlock_method: UnlockMethod
    is_include_effect: IncludeEffectMode
    excluded_modes: ExcludedEffectModes
    is_ranksanity: EnableRanksanity
    ranksanity_limit: RanksanityMaxRank
    is_minosanity: MinoSanity
    is_start_zone: StartWithZone
    death_link: EnableDeathLink
    #trick_locations: TrickLocations
    traps_perc: TrapPercentage
    tspins_n: TSpinsAmmount
    backtobacks_n: BackToBackAmmouont
    tetrises_n: TetrisAmmount
    combos_n: ComboAmmount
    all_clears_n: AllClearAmmount
    combo_backtoback_n: ConsBackToBackAmmount
    tspin_triples_n: TSpinTripleAmmount
    octotris_n: OctotrisAmmount
    dodecatris_n: DodecatrisAmmount
    decahexatris_n: DecahexatrisAmmount
    perfectris_n: PerfectrisAmmount
    ultimatris_n: UltimatrisAmmount
    kirbtris_n: KirbtrisAmmount
