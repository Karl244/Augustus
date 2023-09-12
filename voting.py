import generation
import numpy as np
import json

def election(country):
    a=1
    ## Generate random voters for each county
    C = len(country.counties)
    for j in range(C):
        voters = generateVoters(country.counties[j])

def generateVoters(county,R=100):

    # 
    P = len(county["populations"] )

    # Loop over populations
    for j in range(P):
        b=1

    plannedEconomyVsCapitalism = -10+np.random.rand(20,R)
    closedVsOpenMarket = 0
    stateReligionVsFreeReligion = 0
    nationalistVsGlobalist = 0
    conservativeVsProgressive = 0
    collectivistVsIndividualist = 0

def generateRadomValuesForThisDistribution(x,y,R=10):
    dx = x[1]-x[0]
    # Compute CDF
    cdf0 = np.divide(np.cumsum(y),dx)

    # add extra point to cdf: not sure if this fixes my issue however!
    print('Not sure if this fixes anything')
    cdf = np.array(0)
    cdf = np.append(cdf,cdf0)
    x1 = np.linspace(min(x),max(x),len(cdf))

    # Make random numbers
    randomNumbers = np.random.rand(R)
    # Interpolate random numbers to get ideology values
    randomValues = np.interp(randomNumbers,cdf,x1)
    return randomValues

def generateFineProbDensity(x,y):
    N = 2000
    xNew = np.linspace(min(x),max(x),N)
    yNew = np.interp(xNew,x,y)

    # Normalize: make sure that sum y*dx = 1
    dx = xNew[1]-xNew[0]
    sumY = sum(yNew)
    yNew = yNew/(sumY*dx)

    return xNew, yNew
    


# Make tests here
def testGenerateRandomNumbersVSanalyticSolution():
    # Make x and y
    x = np.linspace(-10,10,21)
    # initialise y
    y = np.zeros(21)
    y[10:21] = 1
    y = y/sum(y)
    randomValues = generateRadomValuesForThisDistribution(x,y,1000)

    # Check if the random values have the same mean as the distribution
    # First determine int (x*f(x))*dx
    xNew,yNew = generateFineProbDensity(x,y)
    dx = xNew[1]-xNew[0]
    xfx = np.multiply(xNew,yNew)
    meanY = np.sum(xfx*dx)
    meanRV = np.mean(randomValues)
    Delta = np.abs(meanY-meanRV)

    # about 1%
    maxError = 1e-2

    if Delta<maxError:
        passTest = True
    else:
        print("testGenerateRandomNumbersVSanalyticSolution failed")
        passTest = False
    return passTest




##### Test
testGenerateRandomNumbersVSanalyticSolution()

# Generate country
fileName = "common/countries/testCountry.txt"
with open(fileName,'r') as f:
    data = json.load(f)
    thisTestCountry = generation.country(data)

# Let them vote
election(thisTestCountry)