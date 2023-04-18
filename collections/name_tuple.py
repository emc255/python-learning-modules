from collections import namedtuple


class Dog:
    def __init__(self, name: str, breed: str, age: int):
        self.name = name
        self.breed = breed
        self.age = age


if __name__ == '__main__':
    Dog = namedtuple("Dog", ["name", "breed", "age"])
    sushi = Dog("sushi", "golden", 2)
    print(type(sushi))
    print(sushi)
    print(sushi.name)
    print(sushi[0])
    print(sushi[1])
