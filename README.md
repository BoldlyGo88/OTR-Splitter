# OTR-Splitter
Python script that splits .otr files for compatability on the Nintendo Switch

## Space warning
.otr files can get bigger once split and I currently don't know a way to fix it/why its happening/or im overlooking something on my end, so until then this warning will have to do

## Prerequisites

  - Plenty of free space on your Switch (OoT Reloaded files will be about 25GB after completing this)
  - [Retro](https://github.com/HarbourMasters64/retro)
  - [OoT-Reloaded Source Files](https://github.com/GhostlyDark/OoT-Reloaded-SoH/tree/master/OoT%20Reloaded%20(SoH)) (or any other .OTR source exceeding 4GB)
  - [Python](https://www.python.org/)

### Creating the .otr's for the Switch

1. Navigate to the OoT-Reloaded Source directory (OoT-Reloaded-SoH-master\OoT Reloaded (SoH)) (or whatever you have)
2. Download or copy the python script into the source directory and launch it
3. Enter a value between 1000 and 1500
   - When I was testing with OoT Reloaded I used 1350, I suggest using 1350, anything higher risks Scene_5/6 being bigger than 4GB
   - If you decide you want to use a higher number make a copy of the scenes folder and manifest.json and do those at 1350 separately
       - You can also remove the "mq" folder within scenes if your copy of Ship of Harkinian does not contain Master Quest, I can't say how much space this will save
4. Wait for everything to finish and get the newly created directories ready
5. Open [Retro](https://github.com/HarbourMasters64/retro) and Press "Create OTR"
6. Press "Replace Textures" and then press "Yes", select any of the new directories from step 4
7. When loaded press "Stage Textures" and wait for it to complete
8. Finally press Finalize OTR and Generate OTR
9. Repeat steps 6-9 until you have every .otr file generated
10. Transfer to your Ship of Harkinian mods folder

## License

This project is licensed under the [MIT License](LICENSE.md)

As a developer you get control over:
- Commercial use
- Modification
- Distribution
- Private use 

Find out more information about the [MIT License](LICENSE.md)

## Acknowledgments

  - The creator of [OoT-Reloaded-SoH](https://github.com/GhostlyDark/OoT-Reloaded-SoH/tree/master)
  - The developers of [Ship of Harkinian](https://github.com/HarbourMasters/Shipwright)
  - The developers of [Retro](https://github.com/HarbourMasters64/retro)
