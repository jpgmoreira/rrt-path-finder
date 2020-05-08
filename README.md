# RRT algorithm implementation using Python and Pygame

This program implements the Rapidly-exploring Random Tree (RRT) algorithm, as described in https://en.wikipedia.org/wiki/Rapidly-exploring_random_tree

Demo video: https://www.youtube.com/watch?v=cbYwxA9g_9k

**May 2020 update**: This program was rewritten, and now its code is more organized and better structured.



## How to run

This program was written using [Python](https://www.python.org/) 3.6.8 and [Pygame](https://www.pygame.org/) 1.9.6, but newer versions of Python3 and Pygame must work too.

After installing Python and Pygame on your system, go to the root folder of this repository and execute the command `python3 src/main.py` or `python src/main.py`, depending on your Python3 executable name.



## Usage

The start position is represented as a green circle, and the goal position as a red circle.
Use the mouse to move the start and goal positions.
Use the left mouse button to draw obstacles, and the right button to erase them.

##### Keyboard:

When the algorithm is not running:

- <kbd>Return</kbd>: Start the RRT algorithm on the current map.
- <kbd>c</kbd>: Clear the map's obstacles.
- <kbd>s</kbd>: Save the current map as 'map.png'
- <kbd>l</kbd>: Load an existing 'map.png' file as the new obstacles map.

When the algorithm is running or a path was found:

- <kbd>h</kbd>: Show / hide information about the algorithm on the screen.

  If any key other than <kbd>h</kbd> is pressed now, then the algorithm stops and the program returns to the initial state.