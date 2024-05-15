class Character:
    def __init__(self, name, rise_to_power, political_alignment, popularity=10, fear=10, US_relations=0, USSR_relations=0):
        self.name = name
        self.rise_to_power = rise_to_power
        self.political_alignment = political_alignment
        self.popularity = popularity
        self.fear = fear
        self.US_relations = US_relations
        self.USSR_relations = USSR_relations

    def handle_scenario(self):
        print("You are now going for a walk outside the palace and you see a group of people protesting against you")
        print("What do you do?")
        print("1. Talk to them")
        print("2. Shoot their Leader")
        print("3. Run back to the palace and send the army to arrest them")
        print("4. Shoot them all")
        print("5. Ignore them")
        choice = input("Enter the number corresponding to your choice: ")

        if choice == "1":
            if self.popularity < 0 and self.fear < 0:
                print("As you approached them, a protester shot you and you died. Game over.")
                return True
            elif self.popularity >= 0 and self.fear <= 20:
                print("You talked to them and they were happy with your words and they left")
                self.popularity += 10
                self.fear += 0
            elif self.fear > 20:
                print("Your mere presence scared them and they left")
        elif choice == "2":
            print("You walked up to the leader, pulled out your Pistol and shot him in the head, the Protestors are horrified and they start running away")
            self.popularity -= 10
            self.fear += 10
        elif choice == "3":
            print("You ran back to the palace and sent the army to disperse them, the army killed 5 of them and the rest fled")
            self.popularity -= 7
            self.fear += 5
        elif choice == "4":
            print("You pulled out your Pistol and started firing blindly like a maniac, until your second in command stopped you and took you back to the palace")
            self.popularity -= 20
            self.fear += 20
            self.US_relations -= 10
            self.USSR_relations -= 5
        elif choice == "5":
            print("You ignored them and they left after a while")
            self.popularity -= 5
            self.fear += 0
        else:
            print("Invalid choice. Please enter a valid option.")

        return False

    def talk_to_protesters(self):
        if self.popularity < 0 and self.fear < 0:
            print("As you approached them, a protester shot you and you died. Game over.")
            return True
        elif self.popularity >= 0 and self.fear <= 20:
            print("You talked to them and they were happy with your words and they left")
            self.popularity += 10
            self.fear += 0
        elif self.fear > 20:
            print("Your mere presence scared them and they left")
        return False

    def shoot_protest_leader(self):
        print("You walked up to the leader, pulled out your Pistol and shot him in the head, the Protestors are horrified and they start running away")
        self.popularity -= 10
        self.fear += 10

    def send_army(self):
        print("You ran back to the palace and sent the army to disperse them, the army killed 5 of them and the rest fled")
        self.popularity -= 7
        self.fear += 5

    def shoot_all(self):
        print("You pulled out your Pistol and started firing blindly like a maniac, untill your second in command stopped you and took you back to the palace")
        self.popularity -= 20
        self.fear += 20
        self.US_relations -= 10
        self.USSR_relations -= 5

    def ignore_protesters(self):
        print("You ignored them and they left after a while")
        self.popularity -= 5
        self.fear += 0
        return False

    def meet_delegation(self):
        print("You are now back in the palace and a delegation from the US and the USSR are here to meet you")
        print("What do you do?")
        print("1. Meet them (Get +5 for US and USSR relations)")
        print("2. Send your second in command to meet them (Get +2 for US and USSR relations)")
        print("3. Ignore the USSR delegation (-20 USSR relations, +20 US relations)")
        print("4. Ignore the US delegation (+20 USSR relations, -20 US relations)")
        choice = input("Enter the number corresponding to your choice: ")

        if choice == "1":
            print("You decided to meet the delegations.")
            self.US_relations += 5
            self.USSR_relations += 5
        elif choice == "2":
            print("You sent your second in command to meet the delegations.")
            self.US_relations += 2
            self.USSR_relations += 2
        elif choice == "3":
            print("You chose to ignore the USSR delegation.")
            self.US_relations += 20
            self.USSR_relations -= 20
        elif choice == "4":
            print("You chose to ignore the US delegation.")
            self.US_relations -= 20
            self.USSR_relations += 20
        else:
            print("Invalid choice. Please enter a valid option.")

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
    print("Welcome to the Dictator Text Game! You are now in charge after the Royal Family has been overthrown")
    character = create_character()
    display_character(character)

    while True:
        if character.handle_scenario():
            return  # End the game if it's already over

        if character.meet_delegation():
            return  # End the game if it's already over

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

if __name__ == "__main__":
    main()