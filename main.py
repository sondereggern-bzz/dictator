import random

def display_statistics(character):
    print("Character Statistics:")
    print(f"Name: {character.name}")
    print(f"Political Alignment: {character.political_alignment}")
    print(f"Rise to Power: {character.rise_to_power}")
    print(f"Popularity: {character.popularity}")
    print(f"Fear: {character.fear}")
    print(f"US Relations: {character.US_relations}")
    print(f"USSR Relations: {character.USSR_relations}")
    print(f"Money: {character.money}")
    print()

def main_menu():
    print("Welcome to the Dictator Text Game!")
    print("1. View Statistics")
    print("2. Start Game")
    print("3. Exit")
    choice = input("Enter the number corresponding to your choice: ")
    return choice

class Character:
    def __init__(self, name, rise_to_power, political_alignment, popularity=10, fear=10, US_relations=0, USSR_relations=0, money=1000):
        self.name = name
        self.rise_to_power = rise_to_power
        self.political_alignment = political_alignment
        self.popularity = popularity
        self.fear = fear
        self.US_relations = US_relations
        self.USSR_relations = USSR_relations
        self.money = money

    def apply_rise_to_power_modifier(self):
        if self.rise_to_power == "CIA-backed coup":
            self.US_relations += 10
        # Add more modifiers as needed for different rise to power scenarios

    def apply_political_alignment_modifier(self):
        # Example modifier for political alignment
        if self.political_alignment == "Communist":
            self.US_relations -= 5
            self.USSR_relations += 10
        elif self.political_alignment == "Nationalist":
            self.US_relations += 5
            self.USSR_relations -= 5
        elif self.political_alignment == "Capitalist":
            self.US_relations += 10
            self.USSR_relations -= 5
            self.money += 500  # Bonus money for capitalist dictators
        elif self.political_alignment == "Anti-Communist":
            self.US_relations += 15
            self.USSR_relations -= 10
        elif self.political_alignment == "Democratic":
            self.US_relations += 10
            self.USSR_relations += -5

        # Add more modifiers as needed for different political alignments

    def handle_protester_scenario(self):
        print("You are now going for a walk outside the palace and you see a group of people protesting against you")
        print("What do you do?")
        print("1. Talk to them")
        print("2. Shoot their Leader")
        print("3. Ignore them")
        choice = input("Enter the number corresponding to your choice: ")

        if choice == "1":
            if self.popularity < 0 and self.fear < 0:
                print("As you approached them, a protester shot you and you died. Game over.")
                return True
            elif self.popularity >= 0 and self.fear <= 20:
                print("You talked to them and they were happy with your words and they left")
                self.popularity += 10
                self.fear += 0
                self.money -= 500  # Deduct money when talking to protesters
            elif self.fear > 20:
                print("Your mere presence scared them and they left")
        elif choice == "2":
            print("You walked up to the leader, pulled out your Pistol and shot him in the head, the Protestors are horrified and they start running away")
            self.popularity -= 10
            self.fear += 10
        elif choice == "3":
            print("You ignored them and they left after a while")
            self.popularity -= 5
            self.fear += 0
            self.money -= 20  # Deduct a smaller amount of money when ignoring protesters
        else:
            print("Invalid choice. Please enter a valid option.")

        return False

    def handle_delegation_scenario(self):
        print("You are now back in the palace and a delegation from the US and the USSR are here to meet you")
        print("What do you do?")
        print("1. Meet them (Get +5 for US and USSR relations plus 200 USD)")
        print("2. Send your second in command to meet them (Get +2 for US and USSR relations)")
        print("3. Ignore the USSR delegation (-20 USSR relations, +20 US relations, +150 USD")
        print("4. Ignore the US delegation (+20 USSR relations, -20 US relations, +50 USD)")
        choice = input("Enter the number corresponding to your choice: ")

        if choice == "1":
            print("You decided to meet the delegations.")
            self.US_relations += 5
            self.USSR_relations += 5
            self.money += 200
        elif choice == "2":
            print("You sent your second in command to meet the delegations.")
            self.US_relations += 2
            self.USSR_relations += 2
        elif choice == "3":
            print("You chose to ignore the USSR delegation.")
            self.US_relations += 20
            self.USSR_relations -= 20
            self.money += 150
        elif choice == "4":
            print("You chose to ignore the US delegation.")
            self.US_relations -= 20
            self.USSR_relations += 20
            self.money += 50
        else:
            print("Invalid choice. Please enter a valid option.")

    def earn_money(self, amount):
        self.money += amount

    def spend_money(self, amount):
        if self.money >= amount:
            self.money -= amount
        else:
            print("You don't have enough money to perform this action.")

def create_character():
    name = input("Enter your dictator's name: ")
    rise_to_power = choose_power_method()
    political_alignment = choose_political_alignment(rise_to_power)
    return Character(name, rise_to_power, political_alignment)

def choose_power_method():
    print("How did you come to power?")
    print("1. CIA-backed coup")
    print("2. Communist revolution")
    print("3. Democratic election")
    print("4. Military coup")
    choice = input("Enter the number corresponding to your choice: ")
    power_methods = {
        "1": "CIA-backed coup",
        "2": "Communist revolution",
        "3": "Democratic election",
        "4": "Military coup"
    }
    return power_methods.get(choice, "Unknown")

def choose_political_alignment(rise_to_power):
    if rise_to_power == "CIA-backed coup":
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
    print("What is your political alignment?")
    for key, value in political_alignments.items():
        print(f"{key}. {value}")
    choice = input("Enter the number corresponding to your choice: ")
    return political_alignments.get(choice, "Unknown")

def display_character(character):
    print("Character creation complete! Here are your details:")
    for key, value in character.__dict__.items():
        formatted_key = key.replace("_", " ").capitalize()
        print(f"{formatted_key}: {value}")


def main():
    character = create_character()
    while True:
        choice = main_menu()
        if choice == "1":
            display_statistics(character)
        elif choice == "2":
            scenario = random.choice(["protester", "delegation"])
            if scenario == "protester":
                if character.handle_protester_scenario():
                    return
            elif scenario == "delegation":
                if character.handle_delegation_scenario():
                    return

        # Check game-over conditions...
        if character.popularity < -75 and character.fear < 50:
            print("Your popularity is too low and fear is too low. You were overthrown. Game over.")
            return
        elif character.popularity < -150:
            print("Your popularity is too low. You were overthrown. Game over.")
            return
        elif character.fear > 50:
            print("Your fear is too high. You were overthrown. Game over.")
            return
        elif character.US_relations < -20 or character.USSR_relations < -20:
            print("Your relations with the US or USSR are too low. They have decided to invade. Game over.")
            return

        elif choice == "3":
            print("Exiting the game. Goodbye!")
            return


if __name__ == "__main__":
    main()