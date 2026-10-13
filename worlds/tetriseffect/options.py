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
    """Set to true if you want the Effect game modes included and shuffled in the multiworld"""
    display_name = "Include Effect Modes"

class ExcludedEffectModes(OptionSet):
    """Allows you to set which modes in the Effect mode will contain location 
    checks in them. By default, Master mode and Classic Score Attack are in 
    this list. It is discouraged to do master mode unless you know what you're doing
    
    The available options are: Marathon, Zone Marathon, Ultra, Sprint, Master, 
    Classic Score Attack, Chill Marathon, Quick Play, Sea Playlist, Wind Playlist, 
    World Playlist, All Clear, Combo, Target, Countdown, Purify and Mystery.
    You may also do the following to exclude an entire group of modes: Classic,
    Relax, Focus and Adventorous"""
    display_name = "Excluded Effect Modes"
    valid_keys = {"Marathon", "Zone Marathon", "Ultra", "Sprint", "Master", "Classic Score Attack", "Chill Marathon", "Quick Play", "Sea Playlist", "Wind Playlist", "World Playlist", "All Clear", "Combo", "Target", "Countdown", "Purify", "Mystery", "Classic", "Relax", "Focus", "Adventorous"}
    default = {"Master", "Classic Score Attack"}

class GoalLevelRequiremnt(Range):
    """Sets how many stages and modes (if Effect is enabled) do you have to 
    clear in order to access Metamorphosis.
    There are 26 stages in Story mode and 17 Effect modes without exclusions, 
    making 43 total possible clears.
    
    If Effect is disabled and the value is set above 26, this option will be 
    set to said number, requiring you to play all of Story mode.
    Otherwise excluded Effect modes are also considered."""
    display_name="Level Clears for Goal Stage"
    range_start = 1
    range_end = 43
    default = 30

class EnableRanksanity(DefaultOnToggle):
    """Adds locations based on your rank, from E rank to SS rank (max rank can 
    be configured below to accomodate less experienced players).
    Applies to Effect modes if it's enabled"""
    display_name = "Ranksanity"

class RanksanityMaxRank(Choice):
    """Sets up to what ranks will be counted as locations.

    Make sure this is a rank you can consistently obtain or you could stale the 
    whole multiworld"""
    display_name = "Max Rank"
    option_c_rank = 0
    option_b_rank = 1
    option_a_rank = 2
    option_s_rank = 3
    option_ss_rank = 4
    default = 0

class MinoSanity(Toggle):
    """Unimplemented. Does nothing as of this version of the world.
    Your mino pieces are items in the multiworld and must be obtained. This can make things like ranksanity considerably harder. 
    As of now there's no logic applied to this. Use at your own caution"""
    display_name = "Minosanity"

class StartWithZone(DefaultOnToggle):
    """When false, the zone becomes an item in the multiworld 
    that has to be obtained for you to use the zone mechanic.
    Affects the logic of zone trick locations, set on the Trick 
    Locations section, and area ranks if ranksanity is enabled."""
    display_name = "Start with Zone"

class EnableDeathLink(Choice):
    """Enable death link for this game. If you die, everyone else with it 
    enabled also dies. Of course, the other way around also applies
    
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
    """Sets a percentage of how many of the filler items in your world will 
    be traps. Setting this to 0 will disable traps"""
    display_name = "Trap Fill Percentage"
    range_start = 0
    range_end = 100
    default = 30


class TSpinsAmmount(Range):
    """How many locations there will be by doing 4 t-spins of any kind
    
    (Note: Trick locations are logically spread to 4 per stage)"""
    display_name = "Do 4 T-Spins"
    range_start = 0
    range_end = 50
    default = 5

class BackToBackAmmouont(Range):
    """How many locations there will be for doing 3 back-to-backs. Back-to-backs 
    are counted by doing 2 or more consecutive t-spins, mini t-spin or Tetris
    
    (Note: Trick locations are logically spread to 4 per stage)"""
    display_name = "Do 3 back-to-backs"
    range_start = 0
    range_end = 50
    default = 5

class TetrisAmmount(Range):
    """How many locations there will be by doing 6 Tetris line clears (4 lines)
    
    (Note: Trick locations are logically spread to 4 per stage)"""
    display_name = "Do 6 Tetris line clears"
    range_start = 0
    range_end = 50
    default = 15

class ComboAmmount(Range):
    """How many locations there will be by doing a 4 combo (clear at least 1 line 
    4 consecutive times)
    
    (Note: Trick locations are logically spread to 4 per stage)"""
    display_name = "Achieve a 4 combo"
    range_start = 0
    range_end = 50
    default = 5

class AllClearAmmount(Range):
    """How many locations there will be by achieving an All Clear (the game 
    board is emptied by the player)
    
    (Note: Trick locations are logically spread to 4 per stage)"""
    display_name = "Achieve an all clear "
    range_start = 0
    range_end = 20
    default = 0

class ConsBackToBackAmmount(Range):
    """How many locations there will be by achieving a back-to-back 3 combo 
    (do 4 t-spins, mini t-spin or Tetris in a row, the combo starts from 
    the second consecutive clear (hence it being called a 3 combo))
    
    (Note: Trick locations are logically spread to 4 per stage)"""
    display_name = "Do 4 consecutive back-to-backs"
    range_start = 0
    range_end = 50
    default = 2

class TSpinTripleAmmount(Range):
    """How many locations there will be by doing a T-Spin triple. T-Spin 
    triples are advanced so make sure you at least know how to set them up
    
    (Note: Trick locations are logically spread to 4 per stage)"""
    display_name = "Do a T-Spin triple"
    range_start = 0
    range_end = 20
    default = 0

class ZoneTricksBehaviour(Choice):
    """Specifies how zone-related locations will be checked when you complete a zone
    
    - **Singular:** When exiting the zone, only the location related to the amount of
    lines cleared will be sent (ex. a 12 line zone will only send 'Made 1 dodecatris').
    - **Include Previous:** When exiting the zone, the location related to the amount
    of lines cleared and all the previous ones will be sent (ex. a 12 line zone will
    send both 'Made 1 dodecatris' and 'Made 1 octotris')"""
    display_name = "Zone-Related Location Check Behaviour"
    rich_text_doc = True
    option_singular = 0
    option_include_previous = 1
    default = 1

class OctotrisAmmount(Range):
    """How many locations there will be by finishing a zone with 8 or 
    more lines cleared"""
    display_name = "Do an octotris"
    range_start = 0
    range_end = 50
    default = 10

class DodecatrisAmmount(Range):
    """How many locations there will be by finishing a zone with 12 or 
    more lines cleared"""
    display_name = "Do a dodecatris"
    range_start = 0
    range_end = 25
    default = 5

class DecahexatrisAmmount(Range):
    """How many locations there will be by finishing a zone with 16 or 
    more lines cleared"""
    display_name = "Do a decahexatris"
    range_start = 0
    range_end = 25
    default = 1

class PerfectrisAmmount(Range):
    """How many locations there will be by finishing a zone with 18 or 
    more lines cleared"""
    display_name = "Do a perfectris"
    range_start = 0
    range_end = 20
    default = 0

class UltimatrisAmmount(Range):
    """How many locations there will be by finishing a zone with 20 or 
    more lines cleared. This can prove to be really difficult so be 
    mindful when increasing this value"""
    display_name = "Do an ultimatris"
    range_start = 0
    range_end = 15
    default = 0

class KirbtrisAmmount(Range):
    """How many locations there will be by finishing a zone with 21 or 
    more lines cleared. If you don't know how to use IRS (the Initial 
    Rotation System) it is strongly encouraged to keep this at 0"""
    display_name = "Do a kirbtris"
    range_start = 0
    range_end = 10
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
        ZoneTricksBehaviour,
        OctotrisAmmount,
        DodecatrisAmmount,
        DecahexatrisAmmount,
        PerfectrisAmmount,
        UltimatrisAmmount,
        KirbtrisAmmount
    ])
]




@dataclass
class TECGameOptions(PerGameCommonOptions):
    unlock_method: UnlockMethod
    include_effect: IncludeEffectMode
    excluded_modes: ExcludedEffectModes
    stage_clears_required_to_goal: GoalLevelRequiremnt
    enable_ranksanity: EnableRanksanity
    ranksanity_limit: RanksanityMaxRank
    #is_minosanity: MinoSanity
    start_with_zone: StartWithZone
    death_link: EnableDeathLink
    trap_fill_percentage: TrapPercentage
    tspin_locations_num: TSpinsAmmount
    backtoback_locations_num: BackToBackAmmouont
    tetrisclear_locations_num: TetrisAmmount
    combo_locations_num: ComboAmmount
    all_clear_locations_num: AllClearAmmount
    #combo_backtoback_n: ConsBackToBackAmmount
    tspin_triple_locations_num: TSpinTripleAmmount
    zone_locations_behaviour: ZoneTricksBehaviour
    octotris_locations_num: OctotrisAmmount
    dodecatris_locations_num: DodecatrisAmmount
    decahexatris_locations_num: DecahexatrisAmmount
    perfectris_locations_num: PerfectrisAmmount
    ultimatris_locations_num: UltimatrisAmmount
    kirbtris_locations_num: KirbtrisAmmount
