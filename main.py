from random import random


def create_character():
    character = {}

    # Name des Charakters eingeben
    character["name"] = input("Enter your dictator's name: ")
    # Auswahl, wie man zur Macht kam
    print("How did you come to power?")
    print("1. CIA-backed coup")
    print("2. Communist revolution")
    print("3. Democratic election")
    print("4. Military coup")
    power_methods = {
        "1": "CIA-backed coup",
        "2": "Communist revolution",
        "3": "Democratic election",
        "4": "Military coup"
    }
    choice = input("Enter the number corresponding to your choice: ")
    character["rise_to_power"] = power_methods.get(choice, "Unknown")

    # Wenn CIA-backed coup gewählt wird, kommunistische Ausrichtung ausschließen
    if character["rise_to_power"] == "CIA-backed coup":
        print("You cannot be communist if you came to power through a CIA-backed coup.")
        political_alignments = {
            "2": "Nationalist",
            "3": "Capitalist",
            "4": "Anti-Communist",
            "5": "Democratic"
        }
    else:
        political_alignments = {
            "1": "Communist",
            "2": "Nationalist",
            "3": "Capitalist",
            "4": "Anti-Communist",
            "5": "Democratic"
        }

    # Auswahl der politischen Ausrichtung
    print("What is your political alignment?")
    for key, value in political_alignments.items():
        print(f"{key}. {value}")
    choice = input("Enter the number corresponding to your choice: ")
    character["political_alignment"] = political_alignments.get(choice, "Unknown")

    return character


def display_character(character):
    print("Character creation complete! Here are your details:")
    for key, value in character.items():
        formatted_key = key.replace("_", " ").capitalize()
        print(f"{formatted_key}: {value}")


def main():
    print("Welcome to the Dictator Text Game! You are now in charge after the Royal Family has been overthrown")
    character = create_character()
    display_character(character)

    populariy = 0
    fear = 10
    US_relations = 0
    USSR_relations = 0

    if character["rise_to_power"] == "CIA-backed coup":
        US_relations += 20
    elif character["rise_to_power"] == "Communist revolution":
        USSR_relations += 20
        US_relations -= 10

    print("You can now start the game \n you are now going for a walk outside the palace and you see a group of people protesting against you \n what do you do? \n 1. Talk to them \n 2. Shoot thier Leader \n 3. Run back to the palace and send the army to arrest them \n 4. Shoot them all \n 5. Ignore them")
    choice = input("Enter the number corresponding to your choice: ")
    if choice == "1":
        if populariy < 0 and fear < 0:
            print("As you approched them, a protster shot you and you died")
        elif populariy >= 0 and fear <= 0:
            print("You talked to them and they were happy with your words and they left")
            populariy += 10
            fear += 0
        elif fear > 20:
            print("your mere presence scared them and they left")

    elif choice == "2":
        print("You walked up to the leader, pulled out your Pistol and shot him in the head, the Protestors are horrified and they start running away")
        populariy -= 10
        fear += 10
    elif choice == "3":
        print("You ran back to the palace and sent the army to disperse them, the army killed 5 of them and the rest fled")
        populariy -= 7
        fear += 5
    elif choice == "4":
        print("You pulled out your Pistol and started firing blindly like a maniac, untill your second in command stopped you and took you back to the palace")
        populariy -= 20
        fear += 20
    elif choice == "5":
        print("You ignored them and they left after a while")
        populariy -= 5
        fear += 0

    print(f"Your popularity is {populariy} and your feared-level is {fear}")
    print("You are now back in the palace and a delegation from the US and the USSR are here to meet you \n what do you do? \n 1. Meet them \n 2. Ignore them \n 3. Send your second in command to meet them \n 4. ignore the USSR \n 5.Ignore the US")






if __name__ == "__main__":
    main()
