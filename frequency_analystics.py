def getFrequency(text):
    freqTab = {}
    rightchecker = len(text) - 1
    leftchecker = 0

    # handle case
    if rightchecker % 2 == 0:
        mid = int(rightchecker/2)
        if text[mid] in freqTab:
            freqTab[text[mid]] += self.INCREMENT
        else:
            freqTab[text[mid]] = self.INCREMENT

    for i in text:
        if i in freqTab:
            freqTab[i] += 1
        else:
            freqTab[i] = 1

    print('result is: \n', freqTab)
    printOutMsg = '\nOption: \n1) Take replace rule \n2) Exit'
    print(printOutMsg)
    userAction = int(input())
    if actUser == 1:
        encdecrMessage()
        return
    if actUser == 2:
        quit()
    else:
        print("invalid option selected, quiting program")
        return


def encdecrMessage(text):
    key = {}
    newStr = ''
    print('Enter new rule-> ')
    newRule = input()
    newRule = newRule.lower().split(',')

    for val in newRule:
        key[val[0]] = val[2]
    print(key)
    for ab in text:
        if ab in key:
            newStr += key.get(ab)
        else:
            newStr += ab
    print(newStr)
