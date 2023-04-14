# import packages
import random
import pathlib

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

class aPoliticalParty:
    def __init__(party,partyName):
        party.name = partyName

def generatePartyName(ideology,allIdeologies):
    if ideology == 'Socialism':
        anIdeology



def defineIdeologies():
    # Load the ideologies.txt
    thisPath = pathlib.Path(__file__).parent.resolve()
    thisPath = str(thisPath.as_posix())
    thisFile = thisPath + '/common/ideologie.txt'
    with open(thisFile,'r') as f:
        lines = f.readlines()
        a=1
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
person = aPolitician("John Wick", 36)
person.introduce()
print(person.birthWeek)

# define all ideologies
ideologies = defineIdeologies()
print(ideologies[0])
print(ideologies[1])

# initialise some ideology
someIdeology = anIdeology('Dummy',-11,-11,-11,-11,-11,-11,[255, 255, 255])
print(someIdeology)
