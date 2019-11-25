class Dog:
    """ A model of a dog """
    def __init__(self, name, age):
        """ Inialize name and age attributes """
        self.name = name
        self.age = age

    def sit(self):
        """ Stimulate a dog sitting command """
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """ Stimulate a dog rolling over command """
        print(f"{self.name} rolled over!")



class puppy(Dog):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_desc(self):
        return f"{self.name} is {self.age} years old!"

    def sit(self):
        return f"{self.name} didn't sit"

    def roll_over(self):
        return "No"

my_dog = puppy('Paw', '1')
print(my_dog.get_desc())
print(my_dog.sit())
print(my_dog.roll_over())
