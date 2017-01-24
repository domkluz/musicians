


class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end=" ")
        print()

class Bassist(Musician): # The Musician class is the parent of the Bassist class
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Twang", "Thrumb", "Bling\n"])

class Guitarist(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Boink", "Bow", "Boom\n"])

    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")

class Drummer(Musician):
    def __init__(self):
        super().__init__(["bang","ting","tang\n"])

    def count(self):  
        print("a 1","a 2","a 1,2,3,4","...\n")
    
    def combust(self):
        print("just combusted")

class Band(Musician):
    def __init__(self):
        print()
        
    def play(self):  
        print("Okay let's get this started, give us the drums first\n")   
    
    def fired(self):  
        print(" that didn't sound great Alex you are fired")


gary=Band()
gary.play()

darren= Drummer()
darren.count()
darren.solo(15)

alex=Bassist()
alex.solo(9)


pete=Guitarist()
pete.solo(6)

gary.fired()

