import time as tm

print("By DPro7\n\nHi!\nThis is an accurate prediction of your life based on your current stats.\n\nHave fun!\n\n\n")

class Character:
    def __init__(self, name, gender, age, happy, balance, grades, isAlive):
        self.name = name
        self.gender = gender
        self.age = age
        self.happy = happy
        self.balance = balance
        self.grades = grades
        self.isAlive = isAlive
    
    def life(self):
        self.isWorking = bool
        self.isStudying = bool
        self.isResting = bool
        if self.gender == "Male":
            self.pronoun = ["He", "his"]
        elif self.gender == "Female":
            self.pronoun = ["She", "her"]
        else:
            print("ERROR on line 24")
        
        while True:
            if self.isAlive == False or self.happy <= 0 or self.age > 80:
                break
            
            if self.grades < 4 and self.balance >= 1000:
                self.isWorking = False
                self.isStudying = True
                self.isResting = False
            
            elif self.grades >= 4 and self.balance >= 1000:
                self.isWorking = False
                self.isStudying = False
                self.isResting = True
            
            elif self.grades >= 4 and self.balance < 1000:
                self.isWorking = True
                self.isStudying = False
                self.isResting = False
            
            elif self.grades < 4 and self.balance < 1000 and self.balance >= 750:
                self.isWorking = False
                self.isStudying = True
                self.isResting = False
            
            elif self.grades < 4 and self.balance < 750:
                self.isWorking = True
                self.isStudying = False
                self.isResting = False
            
            else:
                print("\nERROR in line 56\n")
            
            if self.gender == "Male":
                if self.isWorking == True:
                    self.balance += 50
                    self.happy -= 4
                    self.grades -= 0.125
                
                elif self.isStudying == True:
                    self.grades += 0.5
                    self.happy -= 4
                
                elif self.isResting == True:
                    self.happy += 2
                    self.balance -= 75
                    self.grades -= 0.25
                
                else:
                    print("\nERROR in line 74\n")
            
            if self.gender == "Female":
                if self.isWorking == True:
                    self.balance += 45
                    self.happy -= 3
                    self.grades -= 0.0625
                
                elif self.isStudying == True:
                    self.grades += 0.75
                    self.happy -= 2
                
                elif self.isResting == True:
                    self.happy += 2
                    self.balance -= 75
                    self.grades -= 0.25
                
                else:
                    print("\nERROR in line 92\n")
            
            if self.happy > 100:
                self.happy = 100
            
            tm.sleep(1)
            self.age += 1
            print(f"\n\nName: {self.name} || Gender: {self.gender}\nWorking: {self.isWorking}   ||   Balance: {self.balance}$\nStudying: {self.isStudying}   ||   Grades: {self.grades}\nResting: {self.isResting}   ||   Happiness: {self.happy}%\nAlive: {self.isAlive}   ||   Age: {self.age}\n\n")
        
        if self.balance >= 1200:
            self.isRich = f"with a lot of money on {self.pronoun[1]} balance"
        elif self.balance >= 800 and self.balance < 1200:
            self.isRich = f"with an average amount of money on {self.pronoun[1]} balance"
        elif self.balance < 800:
            self.isRich = f"poor"
        else:
            print("ERROR on line 108")
        
        if self.age >= 70:
            self.isOld = "an old"
            self.isLong = "long"
        elif self.age < 70:
            self.isOld = "a young"
            self.isLong = "short"
        else:
            print("ERROR on line 117")
        
        if self.grades >= 3.5:
            self.isGoodStudent = "well and had good marks"
        elif self.grades < 3.5:
            self.isGoodStudent = "poorly and had bad marks"
        else:
            print("ERROR on line 124")
        
        if self.happy >= 75:
            self.isHappy = "a very happy"
        elif self.happy >= 50 and self.happy < 75:
            self.isHappy = "a happy"
        elif self.happy >= 25 and self.happy < 50:
            self.isHappy = "an unhappy"
        elif self.happy < 25:
            self.isHappy = "a very unhappy"
        else:
            print("ERROR on line 135")
        
        print(f"\n\n{self.name} died {self.isRich} at {self.isOld} age. {self.pronoun[0]} studied {self.isGoodStudent}. {self.pronoun[0]} lived {self.isHappy} and {self.isLong} life.\n\n")

def inputAge():
    while True:
        age = int(input("(Average is 24) Student's Age: "))
        if age >= 31 or age <= 17:
            print("The Student has to be older than 17 and younger than 31.\n")
        elif age < 31 and age > 17:
            break
        else:
            print("ERROR on line 147")
    return age

def inputGrades():
    while True:
        grades = float(input("(Average is 4) Student's Grades: "))
        if grades > 5 or grades < 2:
            print("\nThe Student's grades have to be higher than 1 and lower than 6.\n")
        elif grades <= 5 and grades >= 2:
            break
        else:
            print("ERROR on line 158")
    return grades

def inputGender():
    while True:
        gender = str(input("Student's Gender: "))
        if gender.lower() == "male":
            gender = "Male"
            break
        elif gender.lower() == "female":
            gender = "Female"
            break
        else:
            print("There are only two genders - Male and Female.\n")
    return gender

def inputBalance():
    while True:
        money = int(input("(Average is 2750$) Student's Balance: "))
        if money > 5501 or money <= 0:
            print("\nBalance has to be higher than 0 and lower than 5501\n")
        elif money < 5501 and money > 0:
            break
        else:
            print("ERROR on line 182\n")
    return money

while True:
    try:
        student = Character(str(input("Student's Name: ")).capitalize(), inputGender(), inputAge(), 100, inputBalance(), inputGrades(), True)
        student.life()
        break
    except:
        print("\n\nSomething went wrong... Please, try again\n\n")