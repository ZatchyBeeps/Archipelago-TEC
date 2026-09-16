from BaseClasses import Item, ItemClassification

class TECItem(Item):
    game = "Tetris Effect: Connected"

                                    # ID    Progression (0 = none, 1 = useful, 2 = progressive, 3 = trap)
itemlist = {
    'The Deep Unlock':              (100,   2),
    'Pharaoh\'s Code Unlock':       (101,   2),
    'Karma Wheel Unlock':           (102,   2),
    'Jellyfish Chorus Unlock':      (103,   2),
    'Da Vinci Unlock':              (104,   2),
    'Prayer Circles Unlock':        (105,   2),
    'Ritual Passion Unlock':        (106,   2),
    'Deserted Unlock':              (107,   2),
    'Dolphin Surf Unlock':          (108,   2),
    'Downtown Jazz Unlock':         (109,   2),
    'Spirit Canyon Unlock':         (110,   2),
    'Jewel Veil Unlock':            (111,   2),
    'Forest Dawn Unlock':           (112,   2),
    'Kaleidoscope Unlock':          (113,   2),
    'Turtle Dreams Unlock':         (114,   2),
    'Celebration Unlock':           (115,   2),
    'Sunset Breeze Unlock':         (116,   2),
    'Aurora Peak Unlock':           (117,   2),
    'Zen Blossoms Unlock':          (118,   2),
    'Ying & Yang Unlock':           (119,   2),
    'Hula Soul Unlock':             (120,   2),
    'Starfall Unlock':              (121,   2),
    'Balloon High Unlock':          (122,   2),
    'Mermaid Cove Unlock':          (123,   2),
    'Orbit Unlock':                 (124,   2),
    'Stratosphere Unlock':          (125,   2),
    'Metamorphosis Unlock':         (126,   2),


    'Area 1 Unlock':                (130,   2),
    'Area 2 Unlock':                (131,   2),
    'Area 3 Unlock':                (132,   2),
    'Area 4 Unlock':                (133,   2),
    'Area 5 Unlock':                (134,   2),
    'Area 6 Unlock':                (135,   2),
    # Since area 7 is just Metamorphosis, it shall be unlocked via it's individual stage unlock


    'Effect: Marathon Unlock':              (140,   2),
    'Effect: Zone Marathon Unlock':         (141,   2),
    'Effect: Ultra Unlock':                 (142,   2),
    'Effect: Sprint Unlock':                (143,   2),
    'Effect: Master Unlock':                (144,   2),
    'Effect: Classic Score Attack Unlock':  (145,   2),
    'Effect: Chill Marathon Unlock':        (146,   2),
    'Effect: Quick Play Unlock':            (147,   2),
    'Effect: Playlist (Sea) Unlock':        (148,   2),
    'Effect: Playlist (Wind) Unlock':       (149,   2),
    'Effect: Playlist (World) Unlock':      (150,   2),
    'Effect: All Clear Unlock':             (151,   2),
    'Effect: Combo Unlock':                 (152,   2),
    'Effect: Target Unlock':                (153,   2),
    'Effect: Countdown Unlock':             (154,   2),
    'Effect: Purity Unlock':                (155,   2),
    'Effect: Mystery Unlock':               (156,   2),

    'Effect: Classic Modes Unlcok':         (157,   2),
    'Effect: Relax Modes Unlcok':           (158,   2),
    'Effect: Focus Modes Unlcok':           (159,   2),
    'Effect: Adventurous Modes Unlcok':     (160,   2),


    # 161-175 reserved for Connected mode, whenever that happens

    'Zone Unlock':                          (180,   2),

    'T Mino Piece Unlock':                  (181,   2),
    'Z Mino Piece Unlock':                  (182,   2),
    'S Mino Piece Unlock':                  (183,   2),
    'O Mino Piece Unlock':                  (184,   2),
    'L Mino Piece Unlock':                  (185,   2),
    'J Mino Piece Unlock':                  (186,   2),
    'I Mino Piece Unlock':                  (187,   2),


    'Lines Trap':                           (200,   3),
    'Giant Mino Trap':                      (201,   3),
    'Broken Trap':                          (202,   3),
    'Zone Trap':                            (203,   3), # Untested method, may remove
    'Ghost Piece Trap':                     (204,   3),
    'Swap Trap':                            (205,   3),
    'Next Trap':                            (206,   3),
    #'IRS Trap':                            (207,   3), # Messes up with quick players but idk if it's worth implementing lol
    'Speed Trap':                           (207,   3),



    # Don't implement these until I figure out a way to prevent scores from getting saved, so it doesn't taint the player's records on their save file
    'Bonus points':                         (210,   0), 
    'Zone charge bonus':                    (211,   1),
    
    'Cosmetic effect':                      (212,   0),
    'Glowup':                               (213,   0),
    'Fake line clear':                      (214,   0),
    'Zone sounds':                          (215,   0),
    'Vibes':                                (216,   0), # These ones actually just do nothing
    'Feelings':                             (217,   0),

}