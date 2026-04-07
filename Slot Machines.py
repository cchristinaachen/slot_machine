# The Pokies (Basic Slot Machine)


import random

# Slot symbols
symbols = ["🎱", "🪙", "🎰", "🎳", "💸", "🗝", "💎"]

# Symbol combinations
payouts = {
("🎱", "🎱", "🎱"): 10,
("🎱", "🎱", "Any"): 5,
("🪙", "🪙", "🪙"): 8,
("🎰", "🎰", "🎰"): 6,
("🎳", "🎳", "🎳"): 4,
("💸", "💸", "💸"): 12,
("🗝", "🗝", "🗝"): 15,
("💎", "💎", "💎"): 20
}

"""
Function
"""
def spin_money():
    return[random.choice(symbols) for _ in range(3)]

def calculate_payout(outcome):
    if outcome in payouts:
        return payouts[outcome]
    return 0

"""
Shows the players reamining balance
"""
def slot_machine():
    player_balance = 100
    while player_balance > 0:
        print("Your balance:", player_balance)
        risk = int(input("Place the amount you would like to gamble (0 to quit): "))
        if risk == 0:
              print("Goodbye")
              break
        if risk > player_balance:
            print("Insufficient balance. Please place a valid amount")
            continue

        # Decreases the players balance by how much they bet
        player_balance -= risk
        
        # Spins the machine
        spins = spin_money()
        # Generate 5 rows with 3 random symbols each
        spin = [[random.choice(symbols) for _ in range(3)] for _ in range(5)]

        # Print the spin result
        print("Spinning the money")
        for row in spin:
            print(" | ".join(row))

# Beginning of the program
print("Welcome to the Slot Machine")

# Shows the players reamining balance
slot_machine()
