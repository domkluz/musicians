class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)],end=" ") # general syntax here print(self.sounds[0], end=""" there just happens to be a formula for the [] )
        print()
        
david = Musician(["Twang", "Thrumb", "Bling"])
david.solo(6)
