from Utils.validator import *


def liquid_in_the_given_glass(volume, rows, glass):
    result = validateInput(rows,glass)
    if (result.get("validation_status") != "ERROR"):
        if (result.get("validation_status") == "WARINIG"):
            return result
        filled_glasses = pour_liquid_over_stack_of_glasses(rows, volume)
        glass_position = calculate_total_glasses_bases_on_rows(rows) - 1
        # result["output"] = int(filled_glasses[glass_position])
        print(filled_glasses[glass_position])
    return result

def calculate_total_glasses_bases_on_rows(rows):
    return int((rows*(rows+1)/2))

def pour_liquid_over_stack_of_glasses(rows, volume):
    glasses = [0]*int(rows *(rows + 1) / 2)
    index = 0
    glasses[index] = volume; #ass
    print("\n Length",len(glasses))
    for row in range(1,rows): 
        # Fill glasses in a given row
        for glass in range(1,row+1): 
            volume = glasses[index]
            glass[index] = 250.0 if (volume >= 250.0) else volume
            volume = (volume - 250) if (volume >= 250.0) else 0.0        
            glasses[index + row] += (volume / 2)
            glasses[index + row + 1] += (volume / 2)
            index+=1
    return glasses