# import packages
import random
import pathlib
import csv
import pandas

# set random seed
random.seed(2023)

class aPolitician:
    def __init__(person, nationality, gender, name, age):
        person.name = name
        person.age = age
        person.gender = gender
        person.birthWeek = random.randint(1,52)
        person.nationality = nationality
        person.partyLoyalty = 0
        person.honesty = 0
        person.likeability = 0

    def __str__(person):
        return f"{person.name} ({person.age})"
    
    def introduce(person):
        print("Hello my name is " + person.name)

class anIdeology:
    def __init__(ideology,ideologyName,plannedEconomyVsCapitalism,closedVsOpenMarket,
    statVsFreeReligion,nationalVsGlobal,conservVsProgress,collectiveVsIndividual,rgbcolor):
        ideology.name = ideologyName
        ideology.plannedEconomyVsCapitalism = plannedEconomyVsCapitalism 
        ideology.closedVsOpenMarket = closedVsOpenMarket
        ideology.stateReligionVsFreeReligion = statVsFreeReligion
        ideology.nationalistVsGlobalist = nationalVsGlobal
        ideology.conservativeVsProgressive = conservVsProgress
        ideology.collectivistVsIndividualist = collectiveVsIndividual
        ideology.rgbcolor = rgbcolor

        try:
            ideology = checkBoundsOfValues(ideology)
        except:
            print('Some error with checking bounds')
        
    def __str__(ideology):
        return f"{ideology.name}" 
    
def checkBoundsOfValues(values):
    attributeNames = ["plannedEconomyVsCapitalism","closedVsOpenMarket","stateReligionVsFreeReligion",
    "nationalistVsGlobalist","conservativeVsProgressive", "collectivistVsIndividualist"]

    for att in attributeNames:   
        if getattr(values,att)<-10:
            setattr(values,att,-10)

        if  getattr(values,att)>10:
            setattr(values,att,10)
    
    return values

def generateName(nationality,gender):
    thisPath = pathlib.Path(__file__).parent.resolve()
    thisPath = str(thisPath.as_posix())
    thisFirstNameFile = thisPath + '/common/nameLists/' + nationality + '_firstNames.csv'
    thisLastNameFile = thisPath + '/common/nameLists/' + nationality + '_surnames.csv'

    # slow pandas, but easily reads the csv files without much work
    FirstNames = pandas.read_csv(thisFirstNameFile)
    LastNames = pandas.read_csv(thisLastNameFile)

    L = len(FirstNames)
    R = random.randint(0,L-1)
    if gender=='male':
        firstName = FirstNames.values[R,0]
    elif gender=='female':
        firstName = FirstNames.values[R,1]
    L = len(LastNames)
    R = random.randint(0,L-1)
    lastName = LastNames.Surnames[R]

    name = firstName + ' ' + lastName
    return name
    

class aPoliticalParty:
    def __init__(party,partyName):
        party.name = partyName

def generatePartyName(ideology,allIdeologies):
    if ideology == 'Socialism':
        anIdeology

def defineIdeologies():

    # Load the ideologies.csv
    thisPath = pathlib.Path(__file__).parent.resolve()
    thisPath = str(thisPath.as_posix())
    thisFile = thisPath + '/common/ideologies.csv'

    # slow pandas, but easily reads the csv files without much work
    Data = pandas.read_csv(thisFile)

    ideologies = []
    L = len(Data.values)
    for iN in range(L):
        name = Data.values[iN,0]
        plannedEconomyVsCapitalism = Data.values[iN,1]
        closedVsOpenMarket = Data.values[iN,2]
        stateReligionVsFreeReligion = Data.values[iN,3]
        nationalistVsGlobalist = Data.values[iN,4]
        conservativeVsProgressive = Data.values[iN,5]
        collectivistVsIndividualist = Data.values[iN,6]
        rgbcolor = [Data.values[iN,7], Data.values[iN,8], Data.values[iN,9]] 
        
        # Combine them into a single object
        try:    
            ideologies.append(anIdeology(name,plannedEconomyVsCapitalism,closedVsOpenMarket,
            stateReligionVsFreeReligion,nationalistVsGlobalist,conservativeVsProgressive,
            collectivistVsIndividualist,rgbcolor))
        except:
            print('Not all values are define for ideology number ' + str(iN))
    return ideologies

# tests
person = aPolitician("American","male","John Wick", 36)
person.introduce()
print(person.birthWeek)

# test random name
name = generateName("British",'male')
person = aPolitician("British",'male',name,random.randint(20,75))
name = generateName("British",'female')
person = aPolitician("British",'female',name,random.randint(20,75))
person.introduce()

# define all ideologies
ideologies = defineIdeologies()
print(ideologies[0])
print(ideologies[1])

# initialise some ideology
someIdeology = anIdeology('Dummy',-11,-11,-11,-11,-11,-11,[255, 255, 255])
print(someIdeology)
