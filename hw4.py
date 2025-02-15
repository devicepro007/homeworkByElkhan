import random as rn

alphabet = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

class TextClass:
    def __init__(self, text, encrypted_text="", key=""):
        self.text = text
        self.encrypted_text = encrypted_text
        self.key = key
    
class EncryptClass(TextClass):
    def __init__(self):
        super().__init__("1234567812345678")
    
    def keyGenerator(self):
        b = 0

        for a in range(5, 8):
            if len(self.text) % (a) == 0:
                b = a
                break

        for c in range(b):
            self.key = f"{self.key}{alphabet[rn.randint(0, 61)]}"

        return self.key

    def textEncryptor(self):
        self.key = self.keyGenerator()
        
        for c in range(len(self.text)):
            self.encrypted_text = f"{self.encrypted_text}{self.text[len(self.text)-c-1]}"
        
        return self.encrypted_text

    def resultFunction(self):
        self.encrypted_text = self.textEncryptor()
        
        return f"{self.text}\n{self.encrypted_text}\n{self.key}"

object = EncryptClass()

print(object.resultFunction())