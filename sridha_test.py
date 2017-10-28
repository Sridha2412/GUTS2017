import os
import sys
import random
import time
import multiprocessing
import pygame as pg

SCREEN_SIZE = (500, 400)

class App(object):
    """
    This is the main class for our application.
    It manages our event and game loops.
    """
    def __init__(self):
        """
        Get a reference to the screen (created in main); define necessary
        attributes; and set our starting color to black.
        """
        self.screen = pg.display.get_surface() # Get reference to the display.
        self.clock = pg.time.Clock() # Create a clock to restrict framerate.
        self.fps = 60 # Define your max framerate.
        self.done = False # A flag to tell our game when to quit.
        self.keys = pg.key.get_pressed() # All the keys currently held.
        self.color = pg.Color("black") # The screen will start as black.

    def event_loop(self, quit, value, change):
        """
        Our event loop; called once every frame.  Only things relevant to
        processing specific events should be here.  It should not
        contain any drawing/rendering code.
        """
        if change.value == 1:
            self.screen.fill(value)

        for event in pg.event.get():  # Check each event in the event queue.

            if event.type == pg.QUIT or self.keys[pg.K_ESCAPE]:
                # If the user presses escape or closes the window we're done.
                quit.value = 0
                self.done = True  #quits the game
            elif event.type == pg.MOUSEBUTTONDOWN:
                # If the user clicks the screen, change the color.
                self.color = [random.randint(0, 255) for _ in range(3)]
                change.value = 1


                self.screen.fill(self.color) # Fill the screen with the new color.

                # for idx, i in enumerate(self.color):
                #     value[idx] = self.color[idx]

                self.done = True
            elif event.type in (pg.KEYUP, pg.KEYDOWN):
                # Update keys when a key is pressed or released.
                self.keys = pg.key.get_pressed()

    def main_loop(self, value, quit, change):
        """
        Our game loop. It calls the event loop; updates the display;
        restricts the framerate; and loops.
        """

        while not self.done:
            self.event_loop(quit, value, change) # Run the event loop every frame.

            # print(color, self.color)
            # print(self.done)
            # print(color, self.color)
            # self.screen.fill(value) # Fill the screen with the new
            for idx, i in enumerate(self.color):
                value[idx] = self.color[idx]
                            # #print(value[0], value[1], value[2], value[3])
            # print(self.color, str(value))
            pg.display.update() # Make updates to screen every frame.
            self.clock.tick(self.fps) # Restrict framerate of program.

def win1(caption, value, quit, change, lock):
    """
    Prepare our environment, create a display, and start the program.
    """
    # os.environ['SDL_VIDEO_CENTERED'] = '1' # Center the window (optional).
    pg.init() # Initialize Pygame.
    pg.display.set_caption(caption) # Set the caption for the window.
    pg.display.set_mode(SCREEN_SIZE) # Prepare the screen.
    print("win1", value[0], value[1], value[2], value[3], quit.value, change.value)
    while quit.value == 1:
        print("1", value[0], value[1], value[2], value[3], quit.value, change.value)
        lock.acquire()
        lock.release()
        change.value = 0
        # print("1", value[0], value[1], value[2], value[3])
        App().main_loop(value, quit, change)
        # print("2", value[0], value[1], value[2], value[3])
        change.value = 0
        # color = value
        # print("Main", str(value))
        lock.acquire()
        lock.release()

    print "win1"
    pg.quit()
    sys.exit()


def win2(caption, value, quit, change, lock):
    """
    Prepare our environment, create a display, and start the program.
    """
    # os.environ['SDL_VIDEO_CENTERED'] = '1' # Center the window (optional).
    pg.init() # Initialize Pygame.
    pg.display.set_caption(caption) # Set the caption for the window.
    pg.display.set_mode(SCREEN_SIZE) # Prepare the screen.
    print("win2", value[0], value[1], value[2], value[3], quit.value, change.value)
    while quit.value == 1:
        print("2", value[0], value[1], value[2], value[3], quit.value, change.value)

        lock.acquire()
        lock.release()
        # print("3", value[0], value[1], value[2], value[3])
        App().main_loop(value, quit, change)
        # print("4", value[0], value[1], value[2], value[3])
        change.value = 0
        lock.acquire()
        lock.release()
        # color = value
        # print("Main", str(value))

    print "win2"
    pg.quit()
    sys.exit()


if __name__ == "__main__":
    value = multiprocessing.Array('i', 4)
    quit = multiprocessing.Value('i', 1)
    change = multiprocessing.Value('i', 0)

    lock = multiprocessing.Lock()
    p1 = multiprocessing.Process(target = win1, args = ("Window1", value, quit, change, lock))

    p2 = multiprocessing.Process(target = win2, args = ("Window2", value, quit, change, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print "Done"
