class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return "Woof!"
    
class Cat:
    def __init__(self, breed, color):
        self.breed = breed
        self.color = color

    def meow(self):
        return "Meow!"
    

MyDog =Dog("Jeery", 5)
print(MyDog.name)
print(MyDog.age)

class APIConfig:
    def __init__(self,model,name,version):
        self.model = model
        self.name = name
        self.version = version


dev_config = APIConfig("gpt-3.5-turbo", "ChatGPT", "2024-06")
print(dev_config.version)