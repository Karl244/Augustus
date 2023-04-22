# import packages
import random
import pathlib
import numpy as np
import pandas
import json

# set random seed
random.seed(2023)

####### Generating countries ###########
class country: 
    def __init__(country,data):
        country.name = data["name"]
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
    def __init__(party,partyName):
        party.name = partyName

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
