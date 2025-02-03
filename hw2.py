class Character:
    def __init__(self, name, age, health, balance, grades, isWorking, isStudying, isAlive):
        self.name = name
        self.age = age
        self.health = health
        self.balance = balance
        self.grades = grades
        
        self.isWorking = isWorking
        self.isStudying = isStudying
        self.isAlive = isAlive

student = Character(str(input("Student's Name: ")), int(input("Student's Age: ")), 100, int(input("Student's Balance: ")), int(input("Student's Grades: ")))