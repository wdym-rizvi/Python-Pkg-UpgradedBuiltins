from time import sleep
from rich.console import Console
from rich.text import Text
import sys
import os

console = Console()

def print_(text, color):
    for char in text:
        console.print(char, style=color, end="", highlight=False)
        sleep(0.01)
    sys.stdout.flush()
    print()
