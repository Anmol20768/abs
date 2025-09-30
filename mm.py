from abc import ABC,abstractmethod
class animal(ABC):
    
    @abstractmethod
    def move(self):
        pass

class human(animal):
    def move(self):
        pass

class snake(animal):
    def move(self):
        print('i can crawl')

class bird(animal):
    def move(self):
        print('i can fly')

class dog(animal):
    def move(self):
        print('i can brak and walk')

r= human()
r.move()

k = snake()
k.move()

b = bird()
b.move()

d = dog()
d.move()