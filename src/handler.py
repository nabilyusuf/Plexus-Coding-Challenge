from Utils.processor import *

def setupRun(volume, row, glass):
        print("volume : ", volume, "row : ",row, " : ", "glass : ",glass)
        result = liquid_in_the_given_glass(volume, row, glass)
        print("result : ", result)
        return result