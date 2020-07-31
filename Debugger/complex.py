import pdb
import json


def pathtodict(path):
    """Open file at path and return dictionary."""
    with open(path) as jsonfile:
        diction = json.load(jsonfile)
    return diction


def printer(inputdict):
    """Loop through dictionary and print values."""
    for x, y in inputdict.items():
        pdb.set_trace()
        print('{0}: {1}'.format(x, y))



def mainfunction():
    '''Main function'''
    pdb.set_trace()
    diction = pathtodict('./Debugger/myjson.json')
    printer(diction)




mainfunction()






# To be debugged
# import pdb
# import json


# def pathtodict(path):
#     """Open file at path and return dictionary."""
#     with open(path) as json_file:
#         json_dict = json.load(json_file)


# def printer(input_dict):
#     """Loop through dictionary and print values."""
#     for k, v in input_dict.items():
#         print('{0}: {1}'.format(k, v))




# diction = pathtodict('./Debugger/sample.json')
# printer(diction)

