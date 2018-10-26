import time
import threading

class Timer():
    """A repeating timer class for triggering movement and animation."""
    
    def __init__(self, delay):
        """Initialize the timer, which also starts it. Delay is in seconds. The thread is a daemon thread so that
        it can terminate when the program closes (otherwise there's a non-fatal collision which keeps it running)."""
        self.delay = delay
        self.listeners = []
        self.continueF = True
        self.loopThread = threading.Thread(target = self.mainLoop, daemon = True)
        self.loopThread.start()

    def add(self, newListener):
        """Add an object to the list of what is notified when the timer triggers."""
        self.listeners.append(newListener)
    
    def mainLoop(self):
        """An infinite loop. Called threaded so it doesn't lock up the program. Waits the delay, then 
        notifies everything on the list."""
        while self.continueF:
            time.sleep(self.delay)
            for i in self.listeners:
                i.tickElapsed()
    
    def destroy(self):
        """Ends the infinite loop from the constructor before exiting 
        (otherwise Python keeps running in the background)."""
        self.continueF = False