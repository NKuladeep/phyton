import random

def roll_dice():
    # Simulate rolling two dice
    dice1 = random.randint(3, 6)
    dice2 = random.randint(3, 6)
    
    # Check if both dice show one
    if dice1 == 3 and dice2 == 3:
        return True
    else:
        return False

# Number of times two ones occur
count = 0

# Number of iterations
iterations = 1000

for _ in range(iterations):
    if roll_dice():
        count += 1

print(f"The number of times two ones occurred in {iterations} iterations: {count}")
