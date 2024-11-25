# Starcraft Dance mat controller

Uses Antimicro and pynput

The controller is intended for a Dance Mat of 10 buttons:
8 buttons around the centre (the centre may be a button or
not, it doesn't matter, it's not used) plus start and select.

The Starcraft controller works by switching between 5 modes.

## Scroll Mode
Initial mode, or Scroll Mode, accesses all the others.
* Top Left goes to Mouse Mode
* Top Right goes to Command Mode
* Bottom Left goes to Control Mode 1
* Bottom Right goes to Control Mode 2
* Up, Left, Down, Right press the corresponding arrow keys.
    The arrow keys are to move the screen easily.
* In Scroll Mode, Select and Start are unused.

In the four other modes, Start always goes back to Scroll Mode.
So you always know which mode you're in if you press Start once.

## Mouse Mode
* Up, Down Left, Right move the mouse up, down, left, right.
* Top Left is left click.
    Note you can hold down left click while moving the mouse
    to draw a box.
* Top right is right click
* Bottom Left hits the bottom left button on the command card,
    useful for easily casting most abilities.
* Bottom Right is 'a', useful for easily issuing attack move.
* Select is Esc, to get out of undesired targeting

## Command Mode
* Top Left, Up, Top Right, Left, Right, Bottom Left, Down, Bottom Right
    all hit the corresponding button on the command card. Imagine the
    command card is overlayed on the Dance Mat.
* Select hits the middle button of the command card.

## Control Mode 1
* Up and Down are Control (Left Control)
* Top Left, Top Right, Left, Right, Bottom Left, Bottom Right
    are 1 through 6. Used to access control groups.
* Select is Shift, for adding to control groups.

## Control Mode 2
* Top Left, Up, Top Right are F2, F3, F4 for Camera Locations.
* Select is Shift, for adding to control groups and setting Camera Locations.
* Left, Right, Bottom Left, Bottom Right are 7, 8, 9, 0.
    Used to access control groups.
* Down is Control. (Left Control).
