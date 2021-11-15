from stack_and_queue import Queue

class AnimalShelter:
    def __init__(self):
        self.cat = Queue()
        self.dog = Queue()

    def enqueue_animal(self,animal):
        if animal.lower().startswith("cat") :
            self.cat.enqueue(animal)
        elif animal.lower().startswith("dog") :
            self.dog.enqueue(animal)
        else:
           raise Exception('Enter only cats and dogs')

    def dequeue_animal(self,pref):
        if pref.lower().startswith("cat"):
            return self.cat.dequeue()
        elif pref.lower().startswith("dog"):
            return self.dog.dequeue()
        else :
            return "null"
