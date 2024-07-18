class Animals: 
	def __init__(self): 
		self.lion = 'carnivore'
		self.dog = 'omnivore'
		self.giraffe = 'herbivore'
	def printit(self): 
		print("Dictionary from the object fields belonging to the class Animals:") 
animal = Animals() 
animal.printit() 
print(animal.__dict__) 
