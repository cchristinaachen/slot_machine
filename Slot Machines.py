# The Pokies (Basic Slot Machine) (Sorry for the late sub, slipped right out of my head after school)

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
Makes the slot machine spin by randomly selecting 3 symbols
"""
def spin_money():
    return [random.choice(symbols) for _ in range(3)]

"""
Checks for special condition "Any"
"""
def check_special_conditions(outcome):
    if outcome[0] == "🎱" and outcome[1] == "🎱":
        return 5
    return 0

"""
Calculates the payout amount based on the spin outcome
"""
def calculate_payout(outcome, bet):
    outcome = tuple(outcome)

    if outcome in payouts:
        return payouts[outcome] * bet

    # checks for special conditions, if it is 0 then its none
    return check_special_conditions(outcome) * bet

"""
Main game
"""
def slot_machine():
    player_balance = 100  # Starting money for the user

    while player_balance > 0:
        print("Your balance:", player_balance)

        risk = int(input("Place the amount you would like to gamble (0 to quit): "))

        if risk == 0:
            print("Goodbye")
            break

        if risk > player_balance:
            print("Insufficient balance")
            continue

        # Decreases the players balance by how much they bet
        player_balance -= risk
    
        # Spins the machine
        outcome = spin_money()

        # Generate 5 rows with 3 random symbols each
        spin = [[random.choice(symbols) for _ in range(3)] for _ in range(5)]
        spin[-1] = outcome

        # Prints the spin result
        print("Spinning the money")
        for row in spin:
            print(" | ".join(row))

        winning_money = calculate_payout(outcome, risk)

        if winning_money > 0:
            print("You won:", winning_money)
        else:
            print("No win")

        player_balance += winning_money  # add the winning money into the players balance


# Beginning of the program
print("Welcome to the Slot Machine")

# Shows the players reamining balance
slot_machine()

