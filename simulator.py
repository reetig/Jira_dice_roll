
# simulator.py

import random

def roll_dice():
    """Simulates rolling two 6-sided dice."""
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1 + die2

print("Dice Roll Simulator script created.")