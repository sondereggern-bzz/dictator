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
    character["rise to power"] = power_methods.get(choice, "Unknown")

    # Wenn CIA-backed coup gewählt wird, kommunistische Ausrichtung ausschließen
    if character["rise_to_power"] == "CIA-backed coup":
        print("You cannot be communist if you came to power through a CIA-backed coup.")
        political_alignments = {
            "2": "Nationalist",
            "3": "Capitalist",
            "4": "Loyalist",
            "5": "Democratic"
        }
    else:
        political_alignments = {
            "1": "Communist",
            "2": "Nationalist",
            "3": "Capitalist",
            "4": "Loyalist",
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
        print(f"{key}: {value}")


def main():
    print("Welcome to the Dictator Text Game! You are now in charge after the Royal Family has been overthrown")
    character = create_character()
    display_character(character)


if __name__ == "__main__":
    main()
