import time
import os


def write(string: str, delay: float = 0.06):
    """Print text to the console as if it was being typed.

    Keyword arguments:
    string -- str: Message to be written to the console.
    delay -- float: Delay between each character.
    """
    for i in str(string):
        print(i, end="", flush=True)
        time.sleep(delay)
    print()
