# Installing the mod

## Requirements
- Tetris Effect: Connected with previously completed story mode on any of the 3 difficulties. The mod will not unlock stages that you haven't reached yet.
- The UE4SS mod framework for Unreal Engine games. The mod requires the experimental version to work correctly [that can be found here](https://github.com/UE4SS-RE/RE-UE4SS/releases/tag/experimental-latest). Follow it's installation guide [here](https://docs.ue4ss.com/dev/installation-guide.html).
- The client mod. Find it in the [releases page](https://github.com/ZatchyBeeps/Archipelago-TEC/releases)
- If you're gonna generate a world or would like to use the archipelago options creator GUI, install the [archipelago launcher](https://github.com/ArchipelagoMW/Archipelago/releases) and download and install the apworld (find it in the [releases](https://github.com/ZatchyBeeps/Archipelago-TEC/releases) page as well).

## Installing
Once you have installed UE4SS successfully, **meaning that a command prompt opens every time you open the game**: 
- Extract the folder with the mod files from the zip file and copy it.
- Open the game folder (the same folder that is opened when you hit "Browse local files" on Steam, this could be `YourSteamLibrary\steamapps\common\Tetris Effect Connected\`)
- Paste the folder here.
If everything was done correctly you should see a prompt to replace the file "mods.txt", click yes. The mod is now be installed.

## Configuring your YAML file and generating a world
As with every other archipelago world, you will need a YAML file that dictate your game options and your player name. You can use the YAML file provided on the latest release and edit it on notepad to set your own options, or you can use the options creator from the archipelago launcher.

Once you have your YAML file, the host of the multiworld will require said YAML file and the apworld file. Provide them with these so that they can generate the multiworld.

### Generating
If you are the one to generate the multiworld or are planning to do a single player game, follow the instructions on [how to generate a multiworld](https://archipelago.gg/tutorial/Archipelago/setup_en#generating-a-multiplayer-game), specifically the "On your local installation" as custom worlds are only local; and then click the Host button on the archipelago launcher and selecting the generated multiworld zip file or [host the multiworld on the website](https://archipelago.gg/uploads) by uploading said multiworld file for others to connect to it. Check the [hosting an archipelago server](https://archipelago.gg/tutorial/Archipelago/setup_en#hosting-an-archipelago-server) section, specifically the "From a locally generated game" and "Hosting on a local machine" subsections, for more information.

## Connecting
This is as straightforward as launching the game, getting to the main menu and inputting the connection details, then pressing connect! Enjoy your randomized game!

# Returning back to the normal game
You have 3 options to remove the mod from the game
## Disabling UE4SS via a command argument
On your game launcher, open the game's properties and look for a launch options section. Then add `--disable-ue4ss` into it.
This will launch the game unmodded without uninstalling UE4SS or the client mod, allowing you to play the mod again by removing the launch options whenever you want.
## Disabling the mod
Go to `<Game Location>\Tetris Effect Connected\TetrisEffect\Binaries\Win64\ue4ss\Mods` and open `mods.txt`. Then change `TetrisEffectArchipelago` and `BPModLoaderMod` to 0. Have in mind that this does not disable UE4SS itself.
## Uninstall UE4SS
Go to `<Game Location>\Tetris Effect Connected\TetrisEffect\Binaries\Win64\` and delete `dwmapi.dll`. You may also delete the ue4ss folder in the same location if wanted. If you wanna play the mod again, you'll need to install everything again.