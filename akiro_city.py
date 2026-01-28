# NOTE(v0.1): Prototype script. Messy by design. 
# Questions answered inline while experimenting.
# v0.1 have only random and time modules imported for simulating city events.

import random # For random events
import time # For simulating time passage

# City State
population = 100
money = 1000
food = 500
power = 300
happiness = 75  # out of 100
year = 1

def print_city_stats(): # Display current city stats
    print(f"\nYear: {year}")
    print(f"Population: {population}")
    print(f"Money: ${money}")
    print(f"Food: {food} units")
    print(f"Power: {power} units")
    print(f"Happiness: {happiness}/100\n")

def year_update(): # Update city state for the year
    global population, money, food, power, happiness, year
    # Population consumes food
    food_consumption = population * 2  # each person consumes 2 units of food
    if food >= food_consumption:
        food -= food_consumption
    else:
        food = 0
        happiness -= 10  # lack of food reduces happiness
    
    if food < food_consumption: # Food shortage event
        print("⚠ Food shortage! Happiness decreased.")

    if random.random() < 0.2:  # 20% chance of a festival
        print("Festival held! Happiness increased.")
        happiness += 5

    # Power consumption (simplified)
    power_consumption = population  # each person consumes 1 unit of power
    if power >= power_consumption:
        power -= power_consumption
    else:
        power = 0
        happiness -= 5  # lack of power reduces happiness

    # Happiness affects population growth
    if happiness > 70:
        growth_rate = 0.05  # 5% growth
    elif happiness > 40:
        growth_rate = 0.02  # 2% growth
    else:
        growth_rate = -0.01  # -1% decline

    population_growth = int(population * growth_rate)
    population += population_growth

    # Ensure happiness stays within bounds
    happiness = max(0, min(100, happiness))

    year += 1

def build_house(): # Build a house to increase population
    global money, population
    cost = 200
    if money >= cost:
        money -= cost
        population_increase = 10
        population += population_increase
        print(f"Built a house! Population increased by {population_increase}.")
    else:
        print("Not enough money to build a house.")

def build_farm(): # Build a farm to increase food supply
    global money, food
    cost = 300
    if money >= cost:
        money -= cost
        food_increase = 100
        food += food_increase
        print(f"Built a farm! Food increased by {food_increase}.")
    else:
        print("Not enough money to build a farm.")

def build_power_plant(): # Build a power plant to increase power supply
    global money, power
    cost = 400
    if money >= cost:
        money -= cost
        power_increase = 150
        power += power_increase
        print(f"Built a power plant! Power increased by {power_increase}.")
    else:
        print("Not enough money to build a power plant.")

def main(): # Main game loop
    global money
    print("Welcome to Akiro City!")
    while True:
        print_city_stats()
        print("Choose an action:")
        print("1. Build House ($200)")
        print("2. Build Farm ($300)")
        print("3. Build Power Plant ($400)")
        print("4. End Year")
        print("5. Quit Game")
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            build_house()
        elif choice == '2':
            build_farm()
        elif choice == '3':
            build_power_plant()
        elif choice == '4':
            year_update()
            # Simulate earning money each year
            income = population * 5  # each person generates $5 income
            money += income
            print(f"Year ended. Earned ${income} from the population.")
        elif choice == '5':
            print("Thanks for playing Akiro City!")
            break
        else:
            print("Invalid choice. Please try again.")
        time.sleep(1)  # Pause for a moment before next action
if __name__ == "__main__":
    main()

# End of akiro_city.py