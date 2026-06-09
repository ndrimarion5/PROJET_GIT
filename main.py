#print("Hello, World!")
class MyClass: # cette classe a un constructeur qui prend un argument "name" et une méthode "greet" qui retourne une salutation personnalisée.
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"
# Exemple d'utilisation de la classe MyClass
if __name__ == "__main__": #
    my_object = MyClass("Alice")
    print(my_object.greet())  # Output: Hello, Alice!