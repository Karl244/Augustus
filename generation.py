# import packages
import random
import pathlib
import numpy as np
import pandas
import json

# set random seed
random.seed(2023)

# character id
characterId = 0

####### Generating countries ###########
class country: 
    def __init__(country,data):
        country.name = data["name"]
        country.mainNationality = data["mainNationality"]
        country.counties = []

        # Load county data
        L = len(data["counties"])
        fileNameFirstPart = "common/countries/" + data["folderName"] + '/'
        for j in range(L):
            fileName = fileNameFirstPart + data["counties"][j] + '.txt'
            with open(fileName,'r') as f:
                countyData = json.load(f)
            # append the counties
            country.counties.append(countyData)       
        # Load law data
        a=1

        
        # Load existing parties
        country.parties = []    # initialise parties
        country.people = []             # initialise people
        P = len(data["parties"][0]['partyAbrevNames'])
        for j in range(P):
            key = data["parties"][0]['partyAbrevNames'][j]
            party, partyLeader, members = loadPoliticalPartyFromData(data["parties"][j+1][key],country.mainNationality)
            country.parties.append(party)
            country.people.append(partyLeader)
            country.people.append(members)

    def __str__(country):
        return f"{country.name}" 

class county:
    def __init__(county,data):
        county.name = data["countyName"]
        county.population = []  # Initialise population object

        # initialise other scaler values
        county.totalPopulation = 0
        county.totalAssets = 0
        county.totalIncomePerYear = 0
        L = len(data["populations"])
        # load in the data
        for j in range(L):
            county.population.append(population(data["populations"][j]))
            # set scalar values
            county.totalPopulation = county.totalPopulation + county.population[j].inhabitants
            county.totalAssets = county.totalAssets + county.population[j].totalAssets
            county.totalIncomePerYear = county.totalIncomePerYear + county.population[j].totalIncomePerYear
        
        # Average income and assets
        county.averageIncomePerYear = county.totalIncomePerYear/county.totalPopulation
        county.averageAssets = county.totalAssets/county.totalPopulation

    def __str__(county):
        return f"{county.name}" 
    
class population:
    def __init__(population,populationData):
        population.type = populationData["type"]
        population.inhabitants = populationData["inhabitants"]
        population.assetsPerPerson = populationData["assetsPerPerson"]
        population.workIncomePerPersonPerYear = populationData["workIncomePerPersonPerYear"]
        population.totalAssets = population.inhabitants*population.assetsPerPerson
        population.totalIncomePerYear = population.inhabitants*population.workIncomePerPersonPerYear

        # Set ideologies
        L = len(populationData["ideologies"])
        population.ideologies = []
        for j in range(L):
            temp = populationIdeology(populationData["ideologies"][j])
            population.ideologies.append(temp)
    
    def __str__(population):
        return f"{population.type}" 

class populationIdeology:
    def __init__(populationIdeology,thisIdeologyData):
        populationIdeology.name = "".join(list(thisIdeologyData))
        temp = np.array(thisIdeologyData[populationIdeology.name])

        # Check that the ideology values get normalized, just incase
        S = sum(temp)
        if S==1:
            populationIdeology.values = temp
        elif S==0:
            print('This ' + populationIdeology.name + ' ideology has no distribution. Setting it to neutral')
            populationIdeology.values = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        else:
            population.values = temp/S



########### Generating people
class aPolitician:
    def __init__(person, nationality, gender, name, age,plannedEconomyVsCapitalism=0,closedVsOpenMarket=0,stateReligionVsFreeReligion=0,
        nationalistVsGlobalist=0,conservativeVsProgressive=0,collectivistVsIndividualist=0 ):
        global characterId
        person.name = name
        person.age = age
        person.gender = gender
        person.birthWeek = random.randint(1,52)
        person.nationality = nationality
        person.characterId = characterId
        person.partyLoyalty = round(random.uniform(3,10),1)
        person.plannedEconomyVsCapitalism = plannedEconomyVsCapitalism
        person.closedVsOpenMarket = closedVsOpenMarket
        person.stateReligionVsFreeReligion = stateReligionVsFreeReligion
        person.nationalistVsGlobalist = nationalistVsGlobalist
        person.conservativeVsProgressive = conservativeVsProgressive
        person.collectivistVsIndividualist = collectivistVsIndividualist

        characterId = characterId + 1

    def __str__(person):
        return f"{person.name} ({person.age})"
    
    def introduce(person):
        print("Hello my name is " + person.name)

def generateRandomPoliticians(nationality,R=1,plannedEconomyVsCapitalism=0,closedVsOpenMarket=0,stateReligionVsFreeReligion=0,
        nationalistVsGlobalist=0,conservativeVsProgressive=0,collectivistVsIndividualist=0):      
    gender = generateRandomGender(R)
    age = generateRandomAge(R)

    randomPoliticans = []
    for j in range(R):
        name = generateName(nationality,gender[j])

         # adjust their ideology a bit
        thisPlannedEconomyVsCapitalism = plannedEconomyVsCapitalism + round(random.gauss(0,1),1)
        thisClosedVsOpenMarket = closedVsOpenMarket + round(random.gauss(0,1),1)
        thisStateReligionVsFreeReligion = stateReligionVsFreeReligion + round(random.gauss(0,1),1)
        thisNationalistVsGlobalist = nationalistVsGlobalist + round(random.gauss(0,1),1)
        thisConservativeVsProgressive = conservativeVsProgressive + round(random.gauss(0,1),1)
        thisCollectivistVsIndividualist = collectivistVsIndividualist + round(random.gauss(0,1),1)

        randomPoliticans.append(aPolitician(nationality,gender[j],name, age[j], thisPlannedEconomyVsCapitalism,
                                thisClosedVsOpenMarket,thisStateReligionVsFreeReligion,thisNationalistVsGlobalist,
                                thisConservativeVsProgressive,thisCollectivistVsIndividualist))
    return randomPoliticans

def generateRandomGender(R=1):
    RandomNumber = []
    gender = []
    for j in range(R):
        RandomNumber.append(random.randint(0,1))
        if RandomNumber[j]==1:
            gender.append('male')
        else:
            gender.append('female')
    return gender
    
def generateRandomAge(R=1):
    age = []
    for j in range(R):
        age.append(random.randint(25,67))
    return age

###### Generating ideologies
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
            ideology = checkBoundsOfIdeologyValues(ideology)
        except:
            print('Some error with checking bounds')
        
    def __str__(ideology):
        return f"{ideology.name}" 


###### TO DO: generating a political party
class aPoliticalParty:
    def __init__(party,partyName,membersName,plannedEconomyVsCapitalism,closedVsOpenMarket,stateReligionVsFreeReligion,
                 nationalistVsGlobalist,conservativeVsProgressive,collectivistVsIndividualist,leaderId,membersId):
        party.name = partyName
        party.membersName = membersName
        party.plannedEconomyVsCapitalism = plannedEconomyVsCapitalism
        party.closedVsOpenMarket = closedVsOpenMarket
        party.stateReligionVsFreeReligion = stateReligionVsFreeReligion
        party.nationalistVsGlobalist = nationalistVsGlobalist
        party.conservativeVsProgressive = conservativeVsProgressive
        party.collectivistVsIndividualist = collectivistVsIndividualist
        party.leaderId = leaderId
        party.membersId = membersId
        


def loadPoliticalPartyFromData(data,mainNationality):
    partyName = data[0]['partyName']
    partyMembersName = data[0]['partyMembersName']
    plannedEconomyVsCapitalism = data[0]['plannedEconomyVsCapitalism']
    closedVsOpenMarket = data[0]['closedVsOpenMarket']
    stateReligionVsFreeReligion = data[0]['stateReligionVsFreeReligion']
    nationalistVsGlobalist = data[0]['nationalistVsGlobalist']
    conservativeVsProgressive = data[0]['conservativeVsProgressive']
    collectivistVsIndividualist = data[0]['collectivistVsIndividualist']
    L = len(data[0]['rgbcolor'])
    rgbcolor = []
    for j in range(L):
        rgbcolor.append(data[0]['rgbcolor'][j])
    # Check party leader
    if data[0]['partyLeader']==False:
        leader = generateRandomPoliticians(mainNationality,R=1)
    else:
        print("Need to actually make some code to load this person.")

    # generate N random members
    N = 25
    members = generateRandomPoliticians(mainNationality,N,plannedEconomyVsCapitalism,closedVsOpenMarket,stateReligionVsFreeReligion,
        nationalistVsGlobalist,conservativeVsProgressive,collectivistVsIndividualist)
    memberCharacterId = []
    for j in range(len(members)):
        memberCharacterId.append(members[j].characterId)

    # Create party
    party = aPoliticalParty(partyName,partyMembersName,plannedEconomyVsCapitalism,closedVsOpenMarket,stateReligionVsFreeReligion,
                 nationalistVsGlobalist,conservativeVsProgressive,collectivistVsIndividualist,leader[0].characterId,memberCharacterId)
    
    return party, leader, members

    



def generatePartyName(ideology,allIdeologies):
    if ideology == 'Socialism':
        anIdeology

############## Functions #######
def checkBoundsOfIdeologyValues(values):
    attributeNames = ["plannedEconomyVsCapitalism","closedVsOpenMarket","stateReligionVsFreeReligion",
    "nationalistVsGlobalist","conservativeVsProgressive", "collectivistVsIndividualist"]

    for att in attributeNames:   
        if getattr(values,att)<-10:
            setattr(values,att,-10)

        if  getattr(values,att)>10:
            setattr(values,att,10)
    
    return values

######### Name generation ##############
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


######## CURRENTLY WORKING ON: Making political parties work
fileName = "common/countries/testCountry.txt"
with open(fileName,'r') as f:
    data = json.load(f)
    thisTestCountry = country(data)

    a=1