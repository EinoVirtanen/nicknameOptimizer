from subprocess import check_output
from sys import exit as niceExit
from sys import argv
from random import choice
from string import ascii_lowercase


def readApiKey():
    try:
        apiKeyFile = open("myApiKey", "read")
    except:
        niceExit("ERROR: failed to read file named 'myApiKey'")

    apiKey = apiKeyFile.read().strip()

    if len(apiKey) is not 39:
        niceExit(
            "ERROR: myApiKey file should contain 39 ch long Google API key")

    return apiKey


def readCxKey():
    try:
        cxKeyFile = open("myCxKey", "read")
    except:
        niceExit("ERROR: failed to read file named 'myCxKey'")

    cxKey = cxKeyFile.read().strip()

    if len(cxKey) is not 33:
        niceExit(
            "ERROR: myCxKey file should contain 33 ch long Google CSE cx value")

    return cxKey


def curlGoogleSearch(apiKey, cxKey, nick):
    url = "https://www.googleapis.com/customsearch/v1" + \
        "?key=" + apiKey + \
        "&cx=" + cxKey + \
        "&q=" + nick + \
        "&fields=searchInformation(totalResults)"

    try:
        return check_output(["curl", "-s", url]).split("\n")[2].split('"')[3]
    except OSError as error:
        print "ERROR: curl is probably not installed"
    except subprocess.CalledProcessError as error:
        print "ERROR: something went wrong with the request"


def nickGenerator(baseNick, addedLength, numNicks):
    nickVariations = []

    while numNicks > 0:
        nickVariation = baseNick

        for i in range(addedLength):
            nickVariation = nickVariation + choice(ascii_lowercase)

        nickVariations.append(nickVariation)
        numNicks = numNicks - 1

    return nickVariations


def main():
    apiKey = readApiKey()
    cxKey = readCxKey()

    if len(argv) is not 4:
        niceExit("USAGE: main.py <base nick> <added length> <number of nicks>\n" +
                 "       for example 'main.py johncena 3 2' might return:\n" +
                 "       johncenakfi, johncenapdu")

    possibleNicks = nickGenerator(argv[1], int(argv[2]), int(argv[3]))
    nickResults = []

    print "Querying nicks..\n"

    for nick in possibleNicks:
        nickResults.append(int(curlGoogleSearch(apiKey, cxKey, nick)))

    results = dict(zip(possibleNicks, nickResults))

    for result in sorted(results, key=results.get, reverse=True):
        print result + ": " + str(results[result])

    print "\n[nick]: [number of results]"


main()
