class AnimalShelter():
    def __init__(self):
        self.dogs = []
        self.cats = []
        self.id = 0

    def enqueue(self, animal):
        animal.id = self.id
        self.id += 1
        if animal.animalType == 'cat':
            self.cats.insert(0, animal)
        elif animal.animalType == 'dog':
            self.dogs.insert(0, animal)

    def dequeue(self, animalType):
        if animalType == 'cat':
            if len(self.cats) == 0:
                return None
            return self.cats.pop()
        elif animalType == 'dog':
            if len(self.dogs) == 0:
                return None
            return self.dogs.pop()
        else:
            returnItem = None
            lowestId = None
            index = None
            for i, dog in enumerate(self.dogs):
                if lowestId is None:
                    returnItem = dog
                    lowestId = dog.id
                    index = i
                elif dog.id < lowestId:
                    returnItem = dog
                    lowestId = dog.id
                    index = i

            for i, cat in enumerate(self.cats):
                if lowestId is None:
                    returnItem = cat
                    lowestId = cat.id
                    index = i
                elif cat.id < lowestId:
                    returnItem = cat
                    lowestId = cat.id
                    index = i

            if returnItem is not None and returnItem.animalType == 'cat':
                del self.cats[index]
            elif returnItem is not None and returnItem.animalType == 'dog':
                del self.dogs[index]

            return returnItem

            
        

class Animal():
    def __init__(self, name, animalType):
        self.name = name
        self.animalType = animalType
        self.id = None

animalShelter = AnimalShelter()
dogOne = Animal("billy", "dog")
dogTwo = Animal("frank", "dog")
dogThree = Animal("zee", "dog")

catOne = Animal("socks", "cat")
catTwo = Animal("mittens", "cat")
catThree = Animal("boots", "cat")

animalShelter.enqueue(catOne)
animalShelter.enqueue(dogOne)
animalShelter.enqueue(catTwo)
animalShelter.enqueue(catThree)
animalShelter.enqueue(dogTwo)
animalShelter.enqueue(dogThree)

dog = animalShelter.dequeue("dog")

if dog is not None:
    print(dog.name)

cat = animalShelter.dequeue("cat")

if cat is not None:
    print(cat.name)

anyAnimal = animalShelter.dequeue(None)

if anyAnimal is not None:
    print(anyAnimal.name)

anyAnimal = animalShelter.dequeue(None)
anyAnimal = animalShelter.dequeue(None)
anyAnimal = animalShelter.dequeue(None)
anyAnimal = animalShelter.dequeue(None)
anyAnimal = animalShelter.dequeue(None)

if anyAnimal is None:
    print("There were no animals left!")