print("\n")

currency = str(input("Currency: "))

print("\n")

menu = {}

class FoodClass:
    def __init__(self, foodName, foodPrice):
        self.foodName = foodName
        self.foodPrice = foodPrice

    def addToMenu(self):
        menu.update({self.foodName: self.foodPrice})

        return menu
    
    def returnName(self):
        return self.foodName

def priceInput():
    while True:
        inputAnswer = input("Food Price: ")
        
        if not inputAnswer == "*":
            try:
                inputResult = float(inputAnswer)
                break
            
            except:
                print("\nThe Price has to be a number or *.\n")
        else:
            inputResult = "*"
            break
        
    return inputResult

def foodsInput():
    print(f"\nMay I take your order?")

    chosenMenu = []

    while True:
        foodsInputAnswer = input("Food Name: ")
        
        if not foodsInputAnswer == "*":
            chosenMenu.append(foodsInputAnswer)

        else:
            foodsInputAnswer = None
            break
        
    return chosenMenu

while True:
    RunFoodClass = FoodClass(str(input("Food Name: ")), priceInput())
    
    if RunFoodClass.returnName() == "*":
        break
    
    RunAddToMenu = RunFoodClass.addToMenu()
    print("\n")

print(f"\n_______________\n\nMenu:")

for food, price in menu.items():
    print(f"{food} for {price} {currency}")

class OrderClass:
    def __init__(self, customerName, chosenFoods=[]):
        self.customerName = customerName
        self.chosenFoods = chosenFoods
    
    def bill(self):
        totalPrice = 0

        while True:
            try:
                for i in self.chosenFoods:
                    totalPrice += menu[i]

                break
            
            except:
                print(f"\n{self.chosenFoods} is not on the menu!\n")
                self.chosenFoods = foodsInput()

        return totalPrice

print("_______________\n")

order = OrderClass(str(input("Your Name: ")), foodsInput())

print(f"\n_______________\n\nYour final bill is {order.bill()} {currency}\nYour order is:")

for b in range(len(order.chosenFoods)):
    if b+1 < len(order.chosenFoods):
        print(f"{order.chosenFoods[b]}, ", end="")
    
    elif b+1 == len(order.chosenFoods):
        print(order.chosenFoods[b])

print("\n")