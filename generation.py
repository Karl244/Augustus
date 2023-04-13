# import packages
import random

# set random seed
random.seed(2023)

class aPolitician:
    def __init__(person, name, age):
        person.name = name
        person.age = age
        person.birthWeek = random.randint(0,52)
        person.partyLoyalty = 0
        person.honesty = 0
        person.likeability = 0

    def __str__(person):
        return f"{person.name} ({person.age})"
    
    def introduce(person):
        print("Hello my name is " + person.name)

class anIdeology:
    def __init__(ideology,ideologyName):
        ideology.name = ideologyName

    def __str__(ideology):
        return f"{ideology.name}" 

class aPoliticalParty:
    def __init__(party,partyName):
        party.name = partyName

# tests
person = aPolitician("John Wick", 36)
person.introduce()
print(person.birthWeek)

