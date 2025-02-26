class EmptyHomework(Exception):
    def __str__(self):
        return "Your homework is empty! Why you little..!"

def HomeworkFunc(hw):
    if hw == "":
        raise EmptyHomework
    
    else:
        return "Malades"

print(HomeworkFunc(""))