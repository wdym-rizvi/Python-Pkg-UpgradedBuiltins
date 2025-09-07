from time import sleep
from rich.console import Console
from rich.text import Text
import sys
import os

console = Console()

def input_str(prompt, color, delay):
    for char in prompt:
        console.print(char, style=color, end="", highlight=False)
        sleep(delay)
    sys.stdout.flush()
    str_ = input()
    return str_

def input_int(prompt, color):
    for char in prompt:
        console.print(char, style=color, end="", highlight=False)
        sleep(0.01)
    sys.stdout.flush()
    int_ = int(input())
    return int_