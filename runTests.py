import generation
import json
import random
import time

################ test definitions #########################
def testApolitician():
    try:
        person = generation.aPolitician("American","male","John Wick", 36)
        person.introduce()
        print(person.birthWeek)
        passTest = True
    except:
        print("testApolitician failed")
        passTest = False
    return passTest

def testRandomName():
    try:
        name = generation.generateName("British",'male')
        person = generation.aPolitician("British",'male',name,random.randint(20,75))
        name = generation.generateName("British",'female')
        person = generation.aPolitician("British",'female',name,random.randint(20,75))
        person.introduce()
        passTest = True
    except:
        print("testRandomName failed")
        passTest = False
    return passTest

def testDefineAllIdeologies():
    try:
        ideologies = generation.defineIdeologies()
        print(ideologies[0])
        print(ideologies[1])
        passTest = True
    except:
        print("testDefineAllIdeologies failed")
        passTest = False
    return passTest

def testAnIdeology():
    try:
        # initialise some ideology
        someIdeology = generation.anIdeology('Dummy',-11,-11,-11,-11,-11,-11,[255, 255, 255])
        print(someIdeology)
        passTest = True
    except:
        print("testAnIdeology failed")
        passTest = False
    return passTest

def testLoadCountyData():
    try:
        # Test to see if we can load a county data
        fileName = "common/countries/testCountry/countyA.txt"
        with open(fileName,'r') as f:
            data = json.load(f)
        # now convert the information to a new object
        thisTestCounty = generation.county(data)
        print(thisTestCounty)
        passTest = True
    except:
        print("testLoadCountyData failed")
        passTest = False
    return passTest

def testGenerateRandomGenders():
    R = 1000
    try:
        gender = generation.generateRandomGender(R)
        passTest = True
    except:
        print("testGenerateRandomGenders failed")
        passTest = False
    return passTest


def testInitialiseAcountry():
    try:
        # Test if we can initialise a country
        fileName = "common/countries/testCountry.txt"
        with open(fileName,'r') as f:
            data = json.load(f)
        thisTestCountry = generation.country(data)
        print(thisTestCountry)
        passTest = True
    except:
        print("testInitialiseAcountry failed")
        passTest = False
    return passTest

# get the start time
startTime_s = time.time()

### Specify that we want to run all tests
passTest = []
passTest.append(testApolitician())
passTest.append(testRandomName())
passTest.append(testDefineAllIdeologies())
passTest.append(testAnIdeology())
passTest.append(testLoadCountyData())
passTest.append(testGenerateRandomGenders())
passTest.append(testInitialiseAcountry())

# get the end time
endTime_s = time.time()
elapsedTime_s = endTime_s - startTime_s
print('Execution time:', elapsedTime_s, 'seconds')

## Tell the user if our tests passed or failed
if sum(passTest) == len(passTest):
    print("All tests passed.")
else:
    print("Not all tests passed!")

