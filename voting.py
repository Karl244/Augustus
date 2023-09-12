import generation
import numpy as np
import json
import matplotlib.pyplot as plt

class voters:
    def __init__(voters,countyName='',nPops=1,R=100):
        voters.county = countyName
        voters.populations = defineEmptyPopulation()

        for j in range(nPops):
            voters.populations()
    
    def defineEmptyPopulation():
        voters.populations.plannedEconomyVsCapitalism = np.zeros(21)
        voters.populations.plannedEconomyVsCapitalism = np.zeros(21)


def election(country):
    a=1
    ## Generate random voters for each county
    C = len(country.counties)
    for j in range(C):
        voters = generateVoters(country.counties[j])

def generateVoters(county,R=100):

    # discrete steps
    x = np.linspace(-10,10,21)

    # 
    P = len(county["populations"] )

    # Loop over populations
    for j in range(P):
        # make a temporary short hand
        thisPop = county["populations"][j]

        # Generate their discrete values
        plannedEconomyVsCapitalism = generateRadomValuesForThisDistribution(x,thisPop["ideologies"][0]['plannedEconomyVsCapitalism'],R)
        closedVsOpenMarket = generateRadomValuesForThisDistribution(x,thisPop["ideologies"][1]['closedVsOpenMarket'],R)
        stateReligionVsFreeReligion = generateRadomValuesForThisDistribution(x,thisPop["ideologies"][2]['stateReligionVsFreeReligion'],R)
        nationalistVsGlobalist = generateRadomValuesForThisDistribution(x,thisPop["ideologies"][3]['nationalistVsGlobalist'],R)
        conservativeVsProgressive = generateRadomValuesForThisDistribution(x,thisPop["ideologies"][4]['conservativeVsProgressive'],R)
        collectivistVsIndividualist  = generateRadomValuesForThisDistribution(x,thisPop["ideologies"][5]['collectivistVsIndividualist'],R)

        # For the population make voters with discrete ideologies
        voters[j].plannedEconomyVsCapitalism = plannedEconomyVsCapitalism

        b=1

    plannedEconomyVsCapitalism = -10+np.random.rand(20,R)
    closedVsOpenMarket = 0
    stateReligionVsFreeReligion = 0
    nationalistVsGlobalist = 0
    conservativeVsProgressive = 0
    collectivistVsIndividualist = 0

def generateRadomValuesForThisDistribution(xIn,yIn,R=10):

    # Copy over values
    x = xIn.copy()
    y = yIn.copy()

    # incase R is somehow not an int:
    R = np.uint32(R)

    dx = x[1]-x[0]

    # remember: y[0] and y[-1] have only a half width: correct for this
    y[0] = y[0]/2
    y[-1] = y[-1]/2
    y = y/np.sum(y)

    # Compute CDF
    cdf0 = np.divide(np.cumsum(y),dx)

    # add extra point to cdf: not sure if this fixes my issue however!
    cdf = np.array(0)
    cdf = np.append(cdf,cdf0)
    x1 = np.linspace(min(x)-dx/2,max(x)+dx/2,len(cdf))

    # Make random numbers
    randomNumbers = np.random.rand(R)

    # Interpolate random numbers to get ideology values
    randomValues = np.interp(randomNumbers,cdf,x1)

    # Check out of bound values by adding or substracting deltaX/2
    randomValues[randomValues<-10] =  randomValues[randomValues<-10]+dx/2
    randomValues[randomValues>10] =  randomValues[randomValues>10]-dx/2

    return randomValues

def generateFineProbDensity(xIn,yIn):

    # Copy over values
    x = xIn.copy()
    y = yIn.copy()

    N = 1000
    dx = x[1]-x[0]
    xNew = np.linspace(min(x),max(x),N)
    yNew = np.interp(xNew,x,y)

    # Normalize: make sure that sum y*dx = 1
    dx = xNew[1]-xNew[0]
    sumY = sum(yNew)
    yNew = yNew/(sumY*dx)

    return xNew, yNew
    
def plotRandomValueDistribution(randomValues):
    # plot part
    fig = plt.figure()
    fig,ax = plt.subplots(1,1,figsize = (10,6))
    # make histogram
    n, bins, patches = ax.hist(randomValues,bins=np.linspace(-10,10,41),density=True,facecolor='C0',alpha=0.75)
    ax.set(xlim=(-10, 10))
    plt.grid(visible=True)
    plt.savefig('test.pdf',format = 'pdf')

def plotProbabilityDensity(x,y):
    fig = plt.figure()
    fig,ax = plt.subplots(1,1,figsize = (10,6))

    ax.plot(x,y)
    ax.set(xlim=(-10, 10))
    plt.grid(visible=True)
    plt.savefig('test.pdf',format = 'pdf')


# Make tests here
def testUniformGrid0():
    #
    R = np.uint32(10e3)

    # Make x and y
    x = np.linspace(-10,10,21)
    # initialise y
    y = np.ones(21)
    y = y/sum(y)
    randomValues = generateRadomValuesForThisDistribution(x,y,R)
    meanRV = np.mean(randomValues)

    Delta = np.abs(meanRV-0)       # The average should be 0

    # about 5%
    maxError = 5e-2

    if Delta<maxError:
        passTest = True
    else:
        print("testGenerateRandomNumbersVSanalyticSolution failed")
        passTest = False
    return passTest

def testUniformGrid1():
    # Make x and y
    x = np.linspace(-10,10,21)
    # initialise y
    y = np.ones(21)
    # set x=-10 and x=10 to y=0
    y[0] = 0
    y[-1] = 0

    y = y/sum(y)
    randomValues = generateRadomValuesForThisDistribution(x,y,10e3)
    meanRV = np.mean(randomValues)

    Delta = np.abs(meanRV-0)       # The average should be 0

    # about 5%
    maxError = 5e-2

    if Delta<maxError:
        passTest = True
    else:
        print("testGenerateRandomNumbersVSanalyticSolution failed")
        passTest = False
    return passTest

def testGenerateRandomNumbersVSanalyticSolution():
    # Make x and y
    x = np.linspace(-10,10,21)
    # initialise y
    y = np.zeros(21)
    y[10:21] = 1
    y = y/sum(y)
    randomValues = generateRadomValuesForThisDistribution(x,y,50e3)

    # Check if the random values have the same mean as the distribution
    # First determine int (x*f(x))*dx
    xNew,yNew = generateFineProbDensity(x,y)
    dx = xNew[1]-xNew[0]
    xfx = np.multiply(xNew,yNew)
    meanY = np.sum(xfx*dx)
    meanRV = np.mean(randomValues)
    Delta = np.abs(meanY-meanRV)

    plotRandomValueDistribution(randomValues)
    plotProbabilityDensity(xNew,yNew)
    # about 5%
    maxError = 5e-2

    if Delta<maxError:
        passTest = True
    else:
        print("testGenerateRandomNumbersVSanalyticSolution failed")
        passTest = False
    return passTest

def testVoters():
    try:
        emptyVoters = voters()
    except:
        print('I crash')

##### Test
testUniformGrid0()
testUniformGrid1()
testGenerateRandomNumbersVSanalyticSolution()

# Generate country
fileName = "common/countries/testCountry.txt"
with open(fileName,'r') as f:
    data = json.load(f)
    thisTestCountry = generation.country(data)

# Let them vote
election(thisTestCountry)