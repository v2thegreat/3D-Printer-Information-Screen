from random import choice
from PyQt5 import QtWidgets

def getRandomRange(a,b):
    return range(choice(range(a,b)))

__nums = [chr(ord('0')+x) for x in range(10)]
getVals = lambda n:[''.join([choice(__nums) for x in getRandomRange(0, 9)]) for x in range(len(n))]


def genNumPushButtons(Dialog):
    possibleNumberPushButtons = [QtWidgets.QPushButton(Dialog) for x in range(100)]
    for pushButton in possibleNumberPushButtons:
        pushButton.setText(choice(__nums))

    return possibleNumberPushButtons

# Generated from (https://stackoverflow.com/questions/18834636/random-word-generator-python)
def genPossibleLabels(n):
    possibleStudentIDLabels = [
    "Enter your Student ID: ",
    "Enter Student or Personnel ID: ",
    ]
    try:
        with open('allWords.dat') as allWordsFileObject:
            listOfWords = allWordsFileObject.readlines()
            listOfWords = [words[:-1] for words in listOfWords]
    except FileNotFoundError:
        with open(r'test_BackendStatics_TestingPrams\allWords.dat') as allWordsFileObject:
            listOfWords = allWordsFileObject.readlines()
            listOfWords = [words[:-1] for words in listOfWords]

    OtherPossibleLabels = [' '.join([choice(listOfWords) for x in getRandomRange(0, 10)]) for x in range(n)]
    for labelPos in range(len(OtherPossibleLabels)):
        OtherPossibleLabels[labelPos]+= ': '
    possibleStudentIDLabels = possibleStudentIDLabels + OtherPossibleLabels
    return possibleStudentIDLabels

possibleStudentIDLabels = genPossibleLabels(100)

possibleStudentID = getVals(possibleStudentIDLabels)

for x in range(len(possibleStudentIDLabels)):
    possibleStudentIDLabels[x] += possibleStudentID[x]
