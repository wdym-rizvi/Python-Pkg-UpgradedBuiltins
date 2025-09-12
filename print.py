from time import sleep
from rich.console import Console
from rich.text import Text
import sys
import os

console = Console()

def typewrite(text, color="Blue", delay=0.05):
    for char in text:
        console.print(char, style=color, end="", highlight=False)
        sleep(delay)
    sys.stdout.flush()
    print()
