import time
import os


def write(string: str, delay: float = 0.03):
    """Print text to the console as if it was being typed.

    Keyword arguments:
    string -- str: Message to be written to the console.
    delay -- float: Delay between each character.
    """
    try:
        for i in str(string):
            print(i, end="", flush=True)
            time.sleep(delay)
        print()
        
        return True

    except Exception as e:
        return False
