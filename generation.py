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
    print('Should rewrite this as a csv file and use pandas to run this.')

    # Load the ideologies.txt
    thisPath = pathlib.Path(__file__).parent.resolve()
    thisPath = str(thisPath.as_posix())
    thisFile = thisPath + '/common/ideologie.txt'
    with open(thisFile,'r') as f:
        lines = f.readlines()
        # Find line where number = 0, that starts the process of reading this file
        start = []
        for iN in range(len(lines)):
            if lines[iN][0:6]=='number':
                start.append(iN)

        ideologies = []     # create empty list

        for iN in range(len(start)):
            for jN in range(9):
                if lines[start[iN] +jN][0:4]=='name':
                    name = lines[start[iN] +jN][7:-1]
                if lines[start[iN] +jN][0:26]=='plannedEconomyVsCapitalism':
                    plannedEconomyVsCapitalism = int(lines[start[iN] +jN][29:-1])
                if lines[start[iN] +jN][0:18]=='closedVsOpenMarket':
                    closedVsOpenMarket = int(lines[start[iN] +jN][21:-1])
                if lines[start[iN] +jN][0:27]=='stateReligionVsFreeReligion':
                    stateReligionVsFreeReligion = int(lines[start[iN] +jN][30:-1])
                if lines[start[iN] +jN][0:22]=='nationalistVsGlobalist':
                    nationalistVsGlobalist = int(lines[start[iN] +jN][25:-1])
                if lines[start[iN] +jN][0:25]=='conservativeVsProgressive':
                    conservativeVsProgressive = int(lines[start[iN] +jN][28:-1])
                if lines[start[iN] +jN][0:27]=='collectivistVsIndividualist':
                    collectivistVsIndividualist = int(lines[start[iN] +jN][30:-1])
                if lines[start[iN] +jN][0:8]=='rgbcolor':
                    temp = lines[start[iN] +jN][11:-1]
                    rgbcolor = []
                    k0 = 0
                    for k in range(len(temp)):
                        if temp[k] == ' ':
                            value = int(temp[k0:k])
                            rgbcolor.append(value)
                            k0 = k+1
                        if k==(len(temp)-1):
                            value = int(temp[k0:k+1])
                            rgbcolor.append(value)

            
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
