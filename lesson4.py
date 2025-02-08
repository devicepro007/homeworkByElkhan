class FamilyTree:
    def __init__(self, firstName, weightKg, heightCm, eyeColor, hairColor):
        self.firstName = firstName
        self.weightKg = weightKg
        self.heightCm = heightCm
        self.eyeColor = eyeColor
        self.hairColor = hairColor
    
    def returnCharacteristics(self):
        return f"First Name - \"{self.firstName}\"\nWeight - {self.weightKg}kg\nHeight - {self.heightCm}cm\nEye Color - {self.eyeColor}\nHair Color - {self.hairColor}"

def inputWeight(person):
    weightInputAnswer = input(f"Your {person}Weight: ")
    
    while True:
        try:
            weightInputResult = float(weightInputAnswer)
            break

        except:
            print("\nThe Weight has to be a number\n")
    
    return weightInputResult

def inputHeight(person):
    heightInputAnswer = input(f"Your {person}Height: ")
    
    while True:
        try:
            heightInputResult = float(heightInputAnswer)
            break

        except:
            print("\nThe Height has to be a number\n")
    
    return heightInputResult

grandFather = FamilyTree(str(input("Your Grandfather's First Name: ")), inputWeight("Grandfather's "), inputHeight("Grandfather's "), str(input("Your Grandfather's Eye Color: ")), str(input("Your Grandfather's Hair Color: ")))

print("\n")

father = FamilyTree(str(input("Your Father's First Name: ")), inputWeight("Father's "), inputHeight("Father's "), str(input("Your Father's Eye Color: ")), str(input("Your Father's Hair Color: ")))

print("\n")

you = FamilyTree(str(input("Your First Name: ")), inputWeight(""), inputHeight(""), str(input("Your Eye Color: ")), str(input("Your Hair Color: ")))

print("\n")

print(f"{grandFather.returnCharacteristics()}\n\n{father.returnCharacteristics()}\n\n{you.returnCharacteristics()}")