def getFrequency(text):
    freqTable = {}
    rightTracker = len(text) - 1
    leftTracker = 0

    # handle even edge case
    if rightTracker % 2 == 0:
        mid = int(rightTracker/2)
        if text[mid] in freqTable:
            freqTable[text[mid]] += self.INCREMENT
        else:
            freqTable[text[mid]] = self.INCREMENT

    for i in text:
        if i in freqTable:
            freqTable[i] += 1
        else:
            freqTable[i] = 1

    print('result Analysis: \n', freqTable)
    printOutMsg = '\nOption: \n1) Take replace rule \n2) Exit'
    print(printOutMsg)
    userAction = int(input())
    if userAction == 1:
        encDecryptMessage()
        return
    if userAction == 2:
        quit()
    else:
        print("invalid option selected, quiting program")
        return


def encDecryptMessage(text):
    key = {}
    newStr = ''
    print('Enter the replacement rule-> ')
    replacementRule = input()
    replacementRule = replacementRule.lower().split(',')

    for val in replacementRule:
        key[val[0]] = val[2]
    print(key)
    for ch in text:
        if ch in key:
            newStr += key.get(ch)
        else:
            newStr += ch
    print(newStr)
