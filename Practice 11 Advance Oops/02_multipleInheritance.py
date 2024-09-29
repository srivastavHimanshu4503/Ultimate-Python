# Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from
# ‘Pets’. Add a method ‘bark’ to class ‘Dog’
class Animals:
    @staticmethod
    def home():
        print("Animals generally live in jungle.")

class Pets(Animals):
    @staticmethod
    def types():
        print("Pets variety: Cats, Dogs, Cow, Goat, Buffalo etc")
    
class Dogs(Pets):    
    def bark(self):
        print("Sounds dog make is Bark.")

sound_dog_make = Dogs()
sound_dog_make.bark()
