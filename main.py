import subprocess
from sys import exit as niceExit


def readApiKey():
    try:
        keyFile = open("myApiKey", "read")
    except:
        niceExit("ERROR: failed to read file named \"myApiKey\"")

        apiKey = keyFile.read().strip()

        if len(apiKey) == 39:
            return apiKey
        else:
            niceExit(
                "ERROR: myApiKey file should contain 39 ch long Google API key")


def curlGoogleSearch(term):
    try:
        return subprocess.check_output(["curl", term])
    except OSError as error:
        print("ERROR: curl is probably not installed")
    except subprocess.CalledProcessError as error:
        print("ERROR: something went wrong with the request")
