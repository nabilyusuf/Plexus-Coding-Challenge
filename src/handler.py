from Utils.processor import *

def setupRun(volume, row, glass):
        print("volume : ", volume, "row : ",row, " : ", "glass : ",glass)
        return liquid_in_the_given_glass(volume, row, glass)


print(setupRun(500, 1, 1))