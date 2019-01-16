test_list = [14, 3, 15, 2, 3, 15, 6, 10]


def findMax(list):
    '''take in a list and find the minimum value'''
    minValue = list[0] #minValue = 2

    for number in list:
        print("Value in list: " + str(number))
        if minValue < number:
            minValue = number
            print("New maximum found: " + str(minValue))
    return minValue


print(5/2)