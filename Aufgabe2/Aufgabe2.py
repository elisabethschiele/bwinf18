def start():
    twist = input("Moechten Sie twisten? (True/False)")
    if twist:
        twistStart()
    decode = input("Moechten Sie einen Twist decoden? (True/False)")
    if decode:
        decodeStart()
    if not decode and not twist:
        print ("Wenn Sie nichts von mir wollen, kann ich Ihnen auch nicht helfen...")



def woerterZerlegen( text ):
    import re
    import locale
    locale.setlocale(locale.LC_ALL, 'de_DE')
    return re.split("(\W)", text)        #Zerlege den Text in Woerter

#TWISTEN
def twistStart():
    var = input("Geben Sie hier bitte ihren Text ein, den sie twisten moechten: ")
    twisten (str(var))

def twisten( text ):
    twistedText = ""
    for word in woerterZerlegen( text ):
        if len(word) > 0:
            twistedText = twistedText + (wortTwisten( word ))
        else:
            twistedText = twistedText + word
    print str(twistedText);
    # gefundeneWoerter = [] #nur die laengsten sind richtig
    # twistedText = text
    # with open('woerter.txt') as f:
    #     woerter = f.readlines()
    #     woerter = [x.rstrip() for x in woerter]
    #     for wort in woerter:
    #         if text.find(wort) != -1:
    #             gefundeneWoerter.append(wort)
    #     gefundeneWoerter.sort(reverse = True, key=laengenGewichtung)
    #     for wort in gefundeneWoerter:
    #         if twistedText.find(wort) != -1:
    #             twistedWort = wortTwisten(wort)
    #             twistedText = twistedText.replace(str(wort), str(twistedWort))
    #     print twistedText


# def laengenGewichtung(w):
#     return len(w)

def wortTwisten( word ):
    from random import randint
    twistedWord = word[0]
    middlePart = list(word [1 : (len(word)-1)])
    wordlength = range(0, len(middlePart))
    for i in wordlength:
        j = randint(wordlength[0], wordlength[-1])
        middlePart[i], middlePart[j]  = middlePart[j], middlePart[i]
    twistedWord = twistedWord + "".join(middlePart)
    if len(word) != 1:
        lastChar = word[len(word)-1]
        twistedWord = twistedWord + lastChar
    return twistedWord




#DECODEN
def decodeStart():
    var = input("Geben Sie hier bitte den Text ein, den sie entwisten moechten: ")
    decodeText (str(var))

def decodeText( text ):
    decodedText = ""
    for word in woerterZerlegen( text ):
        if len(word) > 0:
            decodedText = decodedText + (enttwistenWord( word ))
        else:
            decodedText = decodedText + word
    print decodedText

def enttwistenWord( word ):
    possibilities = []
    alphabeth = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    with open('woerter.txt') as f:
        woerter = f.readlines()
        woerter = [x.rstrip() for x in woerter]
        for wort in woerter:
            fits = True
            if wort[0] == word[0] and len(wort) == len(word) and wort[len(wort)-1] == word[len(word)-1]:
                for character in alphabeth:
                    if not word[1: len(word)-1].count(character) == wort[1: len(wort)-1].count(character):      #Passt nur, wenn die gleiche Anzahl von Buchstaben
                        fits = False
                if fits:
                    possibilities.append(wort)
        if len(possibilities) == 1:
            return possibilities[0]
        if len(possibilities) == 0:
            return word
        if len(possibilities) > 1:
            allWordsDifferent = False
            firstWord = possibilities[0]
            for x in possibilities:
                if not firstWord == x:
                    allWordsDifferent = True
            if allWordsDifferent:
                return str(possibilities)
            else:
                return firstWord
