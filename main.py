# Load all packages
import numpy as np
import generation

# Define functions
def defineIdeologies():
    ideologies = generation.anIdeology("socialism")
    return ideologies

ideologies = defineIdeologies()
p = generation.aPolitician
#print(p)
#print(ideologies)