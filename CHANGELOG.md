# Changelog

## [0.0.0]
 - set up initial project directories, structure
 - created main event loop
 - created main menu
 - created dummy pong game

## [0.0.1]
 - improved the appearance of the Main Menu and setup a 'Title' class for game title appearance attributes
   - game title information is defined in main_menu.py and main.py.
   - names for the game title, and game dictionary should match to avoid conflicts
 - created Arcade Settings game for users to change the system volume and quit the console
   - pygame audio mixer is shared across the project, changes will be applied to music for all games
 - created a color blender for animated backgrounds that change color
 - created a music player component to manage system Music
 - created a sound mixer component to manage system Sounds
 - added fonts and images to resources for demonstrations
 - cursor set to invisible over window
 - implemented correct key mapping for joystick and button controls
 - created a rectangle sprite class
 - created a line sprite class
 - created an image sprite class
 - created a carousel class that will loop through the content
 - added a redraw function to the Label class to change font, color, and text