import os

# Change the working directory to the subfolder or main folder
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # This changes to the script's directory

STATE_CITY_DIR = 'ListOfStatesAndCities.txt'
STATE_CODE_DIR = 'StateCodes.txt'


def cleaningstateandcity(dir):
    with open(dir, 'r') as f:
        data = f.read()

    citylines = []
    statelines = []
    stateandcity = {}

    lines = data.split("\n")

    for line in lines:
        if line == "":
            continue
        if line.startswith(" "):
            stripped_line = line.strip()
            citylines.append(stripped_line)
            keyword = list(stateandcity.keys())[-1]
            stateandcity[keyword].append(stripped_line)
        else:
            statelines.append(line)
            stateandcity.update({line: []})

    return stateandcity

def cleaningstatecodes(dir):
    with open(dir, 'r') as f:
        data = f.read()

    lines = data.split("\n")
    stateandcode = {}

    for line in lines:
        if line == "":
            continue
        else:
            words = line.split()
            statename = ''
            for word in words:
                if word.isdigit() == False and len(word) > 2 or word == 'of':
                    statename += word + ' '
            stripped_statename = statename.strip(' \u00A0')
            stateandcode.update({stripped_statename: words[-1]})
    
    return stateandcode


statesandcity = cleaningstateandcity(STATE_CITY_DIR)
statesandcodes = cleaningstatecodes(STATE_CODE_DIR)
cityandstatecodes = {}


def StatecodeAndCity():
    for state, code in statesandcodes.items():
        try:
            cityandstatecodes.update({code: statesandcity[state]})
        except KeyError:
            pass
    return cityandstatecodes
    