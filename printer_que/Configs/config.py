"""
API Key to ensure full functionality when running the Octoprint API in the future
"""
try:
    API_KEY = open('API_KEY.txt').read()

except FileNotFoundError:
    """
    Using a file object in this case as a resourse warnig is raised otherwise
    """
    try:
        fileObject = open(r'Configs/API_KEY.txt')
    except FileNotFoundError:
        fileObject = open(r'../Configs/API_KEY.txt')

    API_KEY = fileObject.read()
    fileObject.close()

SCREEN_RESOLUTION = (800, 480)
STARTUP_POS = (0, 0)
