import json

def validateInput(i,j):
    result = {
        'output': 0,
        'validation_status' : "ERROR", 
        'validation_message': "Invalid input parameters"
        }
    if (j > i) : 
        result["validation_message"] = "Number of columns can not be greater than rows"
        return result
    elif j > (i*(i+1)/2) :
        result["validation_status"] = "WARNING"
        result["validation_message"] = "the given glass will not be part of the stack triangle and will always be zero"
    else :
        result["validation_status"] = "SUCCESSFUL"
        result["validation_message"] = "Valid input parameters"
    return result