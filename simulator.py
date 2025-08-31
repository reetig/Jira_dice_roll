
# simulator.py

import random

def roll_dice():
    """Simulates rolling two 6-sided dice."""
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1 + die2

print("Dice Roll Simulator script created.")

def run_simulation(num_rolls=10000):
    
    # A dictionary to store the counts of each sum (2 through 12)
    counts = {i: 0 for i in range(2, 13)}

    for _ in range(num_rolls):
        roll_sum = roll_dice()
        counts[roll_sum] += 1

    return counts

# This is the main part of the script that runs when you execute the file
if __name__ == "__main__":
    results = run_simulation()
    print("--- Simulation Results ---")
    print(results)