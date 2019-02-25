from Utils.validator import *


def liquid_in_the_given_glass(volume, rows, glass_number):
    result = validateInput(rows,glass_number)
    if (result.get("validation_status") != "ERROR"):
        filled_glasses = pour_liquid_over_stack_of_glasses(rows+1, volume)
        result["output"] = filled_glasses[glass_number+the_last_row(rows)]
    return result

def the_last_row(rows):
    return int((rows*(rows+1)/2))

def pour_liquid_over_stack_of_glasses(rows, volume):
    glasses = [0]*int(rows *(rows + 1) / 2)
    index = 0
    glasses[index] = volume
    # print("\n Length",len(glasses))
    for row in range(1,rows):
        # Fill glasses in a given row
        print("\nrow: ",row)
        for glass in range(1,row+1):
            volume = glasses[index]
            if (volume >= 250.0) :
                glasses[index] = 250.0
                volume = (volume - 250)
            else :
                glasses[index] = volume
                volume = 0.0
            print("glass: ",index, "glass_volume: " ,glasses[index])
            glasses[index + row] += (volume / 2)
            glasses[index + row + 1] += (volume / 2)
            index+=1
    return glasses