
  - RRT algorithm implementation using Python with Pygame. -

  This program implements the RRT path finding algorithm, as
   described in "https://en.wikipedia.org/wiki/Rapidly-exploring_random_tree".

  - - -

  - Description:
  
  The starting position is represented as a green square, and
   the goal position as a red square.

  You can grab and drag the initial and goal positions to move them
   on the screen.

  The left mouse button allows obstacles drawing,
   and the right mouse button erases the obstacles.

   
  - Keyboard:
  
   When the algorithm is not running (state != 'running'):
   - Enter: Starts the RRT path finding algorithm on the current map.
   - 'c' : Clears the map's obstacles.
   - 's' : Saves the current map obstacles as 'map.png'.
    If there is an existing 'map.png' in the same directory of 'RRT path finder.py',
     then it replaces the old 'map.png' with the new image.
   - 'l': Loads an existing 'map.png' file as new obstacles map.
   
   When the algorithm is running or a path was found:
   - 'h' : Hide or show status information of the algorithm.
   If a key other than 'h' is pressed now, then the algorithm stops
    and the program returns to the 'normal' state.
    
  - - -

  Each time the program states change, the new state is shown on the console.
  Possible states are:

   - 'normal', 'start_drag', 'goal_drag', 'drawing',
     'erasing','running' and 'path_found'.

