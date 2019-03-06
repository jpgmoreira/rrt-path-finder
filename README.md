# RRT algorithm implementation using Python and Pygame

​	This program implements the *RRT path finding* algorithm, as described in https://en.wikipedia.org/wiki/Rapidly-exploring_random_tree .

​	Demo video: https://www.youtube.com/watch?v=cbYwxA9g_9k

- - -

 - Prerequisites:

    This program was written in Python 3.6.3 with Pygame 1.9.3, but other Python 3 and Pygame versions must work too.

    - Python: https://www.python.org

    - Pygame: https://www.pygame.org

      

  - Description:

      The starting position is represented as a green square, and the target position as a red square.

      You can grab and drag the start and target positions to move them using the mouse's left button.

      The left mouse button also allows obstacles drawing. Use the right mouse button to erase the obstacles.

​    

  - Keyboard:

    - When the algorithm is not running (state != "running"):

      - Enter: Starts the RRT path finding algorithm on the current map.
      - 'c' : Clears the map's obstacles.
      - 's' : Saves the current map of obstacles as 'map.png'.
      - 'l': Loads an existing 'map.png' file as new obstacles map.

    > If there is a "map.png" file in the same directory of "main.py", then pressing the 's' key replaces the existing "map.png" with the new image! 

    - When the algorithm is running or a path was found:
      - 'h' : Hide or show status information of the algorithm. If a key other than 'h' is pressed now, then the algorithm stops and the program returns to the "normal" state.

------

Each time the program state changes, the new state is shown on the console.
Possible states are:

   - "normal", "start_drag", "target_drag", "drawing", "erasing", "running" and "path_found".

