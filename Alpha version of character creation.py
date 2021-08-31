import random

class bcolors:
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'

class Character:
    characterNames = ['Luke', 'Leia', 'Zbyszek', 'Dart Vader', 'Gabriel', 'Jayce', 'Leona', 'Jinx']


    def __init__(self, strength, agility, vitality, intelligence, charisma):
        self.name = random.choice(self.characterNames)
        self.strength = strength
        self.agility = agility
        self.vitality = vitality
        self.intelligence = intelligence
        self.charisma = charisma
        self.hitpoints = vitality * 10

    def ALLInformation(self):
        #prints all the informations about character
        print(f"{bcolors.OKCYAN}CHARACTER: " + str(self.name)
        + ", Strength: " + str(self.strength)
        + ", Agility: " + str(self.agility)
        + ", Vitality: " + str(self.vitality)
        + ", Intelligence: " + str(self.intelligence)
        + ", Charisma: " + str(self.charisma)
        + ", HP: " + str(self.hitpoints))
        print("---------------------------------------")

    def getName(self):
        #Returns name of the character
        return self.name

def collectInformation():
    #Collect data about character if user chooses to create character manually
    stats = {"STR": 0, "AGL": 0 , "VIT": 0, "INT": 0, "CHA": 0}
    for y in stats:
        while True:
            try:
                val = int(input('Please enter ' + y + ' points for your character(1-10): '))
                if 1<= val <=10:
                    stats[y] = val
                    break
            except (ValueError, TypeError):
                pass
    return createCharacter(stats)

def generateInformation():
    #Generate all information for the character if user chooses to create character randomly
    stats = {
        'STR': random.randint(1,10),
        'AGL': random.randint(1,10),
        'VIT': random.randint(1,10),
        'INT': random.randint(1,10),
        'CHA': random.randint(1,10)
        }
    return createCharacter(stats)


def createCharacter(info):
    #Creates character
    return Character(info['STR'], info['AGL'], info['VIT'], info['INT'], info['CHA'])

def main():
    charactersList = {}

    while True:
        #Menu
        print(f"{bcolors.OKCYAN} WELCOME TO MAIN MENU:{bcolors.ENDC}")
        print("ENTER 1 TO CREATE CHARACTER MANUALLY: ")
        print("ENTER 2 TO CREATE CHARACTER RANDOMLY: ")
        print("ENTER 3 TO PRINT ALL CREATED CHARACTERS: ")
        print("ENTER 4 TO PRINT CHARACTER'S INFORMATION BY THE NAME(enter 3 in main menu to see ther names)")
        print("ENTER 5 to EXIT")
        print("-------------------------------------------")

        choice = input('Choose an option: ')

        if choice =="1":
            #Create character and adding it to the dictionary
            character = collectInformation()
            charactersList[character.getName()] = character
            print(f"{bcolors.OKGREEN} Character has been created!{bcolors.ENDC}")
        elif choice =="2":
            #Creating random Character and also adding it to the dictionary
            character = generateInformation()
            charactersList[character.getName()] = character
            print(f"{bcolors.OKGREEN}Character has been created!{bcolors.ENDC}")
        elif choice =="3":
            #Print all the character's names
            print(f"{bcolors.OKGREEN}List of all characters:{bcolors.ENDC}")
            for obj in charactersList:
                print(obj)
        elif choice =="4":
            # If you Enter characters name it will display details about it
            name = input("Please enter the name of the character: ")
            if name in charactersList:
                print(charactersList[name].ALLInformation())
            else:
                print(f"{bcolors.WARNING}!THERE IS NO SUCH NAME IN THE DICTIONARY!{bcolors.ENDC}")
        elif choice =="5":
            #EXITS PROGRAM
            break
        else:
            print(f"{bcolors.WARNING}I do not understand. Please choose right number!{bcolors.ENDC}")
    print("BYE!")

main()

