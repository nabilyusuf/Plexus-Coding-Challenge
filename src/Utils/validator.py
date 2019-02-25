import json

def validateInput(rows,glass_number):
    result = {
        'output': 0,
        'validation_status' : "ERROR",
        'validation_message': "Invalid input"
        }
    if (glass_number > rows) :
        result["validation_message"] = "selected glass is not in the given stack of rows"
        return result
    else :
        result["validation_status"] = "SUCCESSFUL"
        result["validation_message"] = "Valid input"
    return result