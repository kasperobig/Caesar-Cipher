def getFrequency(text):
    freqTab = {}
    rightTker = len(text) - 1
    leftTker = 0

    # handle even edge case
    if rightTker % 2 == 0:
        mid = int(rightTker/2)
        if text[mid] in freqTab:
            freqTab[text[mid]] += self.INCREMENT
        else:
            freqTab[text[mid]] = self.INCREMENT
