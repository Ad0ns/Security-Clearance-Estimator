import random

def clearance_check():
    name = input("Enter your name to assess your security clearance level: ")
    known_agents = {"bond", "neo", "danon", "indigo"}

    if name.lower() not in known_agents:
        level = random.randint(100, 900)

        if level <= 100:
            print(f"{name.capitalize()}, your clearance level is {level}. You're not authorized beyond the lobby.")
        elif level <= 400:
            print(f"{name.capitalize()}, with a level of {level}, you can access general files. Not bad.")
        elif level <= 700:
            print(f"Clearance {level} granted, {name.capitalize()}. You're trusted with confidential operations.")
        else:
            print(f"{name.capitalize()}, your level is {level}. You have Omega-level access. Don't abuse it.")
    else:
        print(f"{name.capitalize()} detected. Classified access granted — welcome back, operative.")

clearance_check()