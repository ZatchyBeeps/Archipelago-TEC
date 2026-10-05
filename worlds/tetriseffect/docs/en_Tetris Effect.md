# Tetris Effect: Connected

## What is randomized in this game?
All levels on the story mode are items that you need to find in order to unlock them with the option of receiving more items based on the ranks you obtain. You can also add the Effect modes into the mix, which will also send completion and ranking checks. An effect mode is considered cleared after getting a C rank on them. Your zone and tetriminos can also become unlockable items in the multiworld which increases the difficulty of clearing levels and getting high ranks. Your goal is to beat the final stage of the story mode, Metamorphosis.

You cam customize the behaviour of the randomizer to your liking on your YAML file, with options like maximum obtainable ranks, switching between individual stage unlocks or grouped by area; and excluding Effect modes if you find one of them annoying or too hard.


## How to set-up
For information on how to generate and install the mod, head over to [the setup guide](setup_en.md)


# Things to note
## Online features and scores
The mod can be capable of slightly boosting your score in the form of filler items, therefore, offline mode is forcibly on to prevent non realistic entries for the player to the leaderboards and it will prevent saving said scores to preserve your autentic hi-scores for as long as the mod is active. It is nothing big anyways, it will at most give you 1000 points of score, not put you at 999 million or something stupid.

## What is planned for the mod?
This mod is still in development and is missing features. This will be a checklist for what needs to be added for being called a stable release, somewhat ordered on priority:
- Resolve the issue of playlists being a single one
- Turn the text log into a rich text box to support colors
- Implement minosanity
- Add more planned traps
- Implement filler items actually doing something
- Make Effect modes give rank checks asynchronously
- Make the text log fade out when inactive
- Implement Connected mode

## How to report a bug
If you want to report a bug please explain what happened with your log file attached either on the Tetris Effect: Connected thread in the Future Game Design channel on the Archipelago server or on a new issue here on GitHub.
Your log file should be located on `<Game Location>\Tetris Effect Connected\TetrisEffect\Binaries\Win64\ue4ss\UE4SS.log`. Have in mind that the log file gets cleared every time you open the game.

## Does my savefile get modified?
Your savefile is not modified in the slightest.

## How do I return to the normal game?
There are 3 options to do this. See the [Returning back to the normal game](https://github.com/ZatchyBeeps/Archipelago-TEC/blob/main/worlds/tetriseffect/docs/setup_en.md#Returning-back-to-the-normal-game) section on the setup docs.


# Know issues
This is a list of issues I already know of
## When selecting a story stage, it sometimes breaks and stops working
This is because the mod will make you try to select an available stage as otherwise the game will automatically select your last played stage, which can allow you to play an unobtained level.
You can fix this by either going back and selecting a difficulty again, or ignoring it and clicking anywhere which will play your furthest obtained level on the story.
## Crashes occur when death linked
This seems to be a memory issue with lua-apclientpp. Trying to update the dll to the latest version which seems to have memory fixes causes the mod to crash upon load, so this is not fixable for now.
## Lines given by traps or death link don't have holes
While they do are detremental on quantity, they are not permanent. Simply use the zone and they will not only go away when finished but they will also be added to the zone's total ammount of lines cleared.
I am still looking on how to add their holes.