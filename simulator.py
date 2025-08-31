import random
import matplotlib.pyplot as plt
# performance optimizations added to handle large simulations(bug fix simulation)
def roll_dice():
    
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

def calculate_percentages(counts, num_rolls=10000):
    
    percentages = {}
    for key, value in counts.items():
        percentages[key] = (value / num_rolls) * 100
    return percentages

def display_results_chart(percentages):
    
    sums = list(percentages.keys())
    percents = list(percentages.values())

    plt.figure(figsize=(10, 6))
    plt.bar(sums, percents, color='skyblue')
    plt.xlabel("Sum of Two Dice")
    plt.ylabel("Percentage (%)")
    plt.title("Dice Roll Simulation Results (10,000 Rolls)")
    plt.xticks(sums)
    plt.grid(axis='y', linestyle='--')

    print("\nDisplaying results chart...")
    plt.show()

if __name__ == "__main__":
    simulation_results = run_simulation()
    percentage_results = calculate_percentages(simulation_results)
    
    print("--- Simulation Results (Counts) ---")
    print(simulation_results)
    
    print("\n--- Percentage Results ---")
    for roll_sum, percentage in percentage_results.items():
        #format to 2 decimal places
        print(f"Sum {roll_sum}: {percentage:.2f}%")
        
    
    display_results_chart(percentage_results)