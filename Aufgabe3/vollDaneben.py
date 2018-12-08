numbers = []
meanValues = []
#liste aller gruppen
group = [[],[],[],[],[],[],[],[],[],[]]
#hilfsliste zum umsortieren
newGroup = [[],[],[],[],[],[],[],[],[],[]]


#sortiert die Teilnehmerzahlen der Größe nach und speichert die neue Liste (global) in numbers
def sort(example):
    with open(example) as f:
        myNumbers = f.readlines()
        myNumbers = [x.rstrip() for x in myNumbers]
        myNumbers.sort(key=int)
        for number in myNumbers:
            numbers.append(number)


#berechnet die ersten zehn zahlen, von denen aus der gruppierungsprozess anfängt
def setFirstMeanValue():
    x = ( int(numbers[-1]) - int(numbers[0]) )/10
    difference = round(x,0)
    firstValue = round((int(numbers[0]) + (x/2)), 0)
    meanValues.append(firstValue)
    c = 0
    while int(meanValues[c]) <= (int(numbers[-1]) - difference):
        meanValues.append(int(meanValues[c]) + difference)
        c += 1


#die teilnehmerzahlen werden einer der gruppen zugewiesen
#group[0][x] ist das x-te element der 0. gruppe, welche zum 0. meanValue gehört
def assignNumbersToMeanValuesFirstTime():
    n = 0   #zum zählen der elemente in numbers
    c = 0   #zum zählen der elemente in meanValues
    g = 0   #zum zaehlen der gruppierungsprozess

    for number in numbers:
        while g <= 10 and c < 9:
            while abs(int(numbers[n]) - int(meanValues[c])) <= abs(int(numbers[n]) - int(meanValues[c+1])):
                group[g].append(int(numbers[n]))
                n += 1
            c += 1
            g += 1


#rechnet die neuen Mittel der einzelnen Gruppen aus
def calculateMeanValues():
    sum = 0
    n = 0
    g = 0
    while g < 9 and n < (len(group[g])-1):
        for number in group[g]:
            sum += round(int(group[g][n]),0)
            n += 1
        meanValues[g] = sum/len(group[g])


def assignNumbersToMeanValues():
    c = 0   #zum zählen der elemente in meanValues
    g = 0   #zum zaehlen der gruppierungsprozess

    for each in group:
        while g < 9 and c < 9:
            n = 0
            while int(group[g][-1]) != -1 and n < len(group[g]) and abs(int(group[g][n]) - int(meanValues[c])) <= abs(int(group[g][n]) - int(meanValues[c+1])):
                newGroup[g].append(int(group[g][n]))
                group[g][n] = -1
                n += 1
            while int(group[g][-1]) != -1 and n < len(group[g])-1:
                newGroup[g+1].append(int(group[g][n]))
                group[g][n] = -1
                n += 1
            c += 1
            g += 1


#Gruppen group und newGroup werden getauscht
def switchGroups():
    g = 0   #counts groups
    while g < len(newGroup):
        el = 0  #counts elements within groups
        while el < len(newGroup[g]):
            group[g][el] = int(newGroup[g][el])
            el += 1
        g += 1
    for every in newGroup:
        newGroup[z] = []
        z += 1


def repeat(maxReps):
    calculateMeanValues()
    assignNumbersToMeanValues()
    if maxReps > 0:
        cont = True
        g = 0
        for each in group:
            e = 0
            for item in group[g]:
                if group[g][e] != newGroup[g][e]:
                    cont = False
                e += 1
            g += 1
        if cont == False:
            print('Die dem Algorithsmus zu Fole besten Mittelwerte wurden erfolgreich berechnet!')
            print('Die Werte, die Al Capone Junior wählen solte sind: ')
            e = 0
            for each in meanValues:
                meanValues[e] = round(int(meanValues[e]))
                e += 1
            print(meanValues)
            test()
        else:
            switchGroups()
            maxReps -= 1
            repeat(maxReps)
    else:
        print('Die maximale Anzahl an rekursiven Wiederholungen wurde überschritten')
        print('Die beste Annäherung an die idealen Werte ist: ', meanValues)

def everything(example):
    sort(example)
    setFirstMeanValue()
    assignNumbersToMeanValuesFirstTime()
    repeat(10)

def test():
    money = len(numbers)*25
    payout = 0
    add = 0
    g = 0
    for each in group:
        e = 0
        for item in group[g]:
            add = abs(int(meanValues[g])-int(group[g][e]))
            e += 1
            payout = payout + add
        g += 1
    money = money - payout
    print(money)

if __name__ == '__main__':
    example = input('Mit welchem Beispiel möchen Sie arbeiten? (1/2/3) ')
    if int(example) == 1 or int(example) == 2 or int(example) == 3:
        if int(example) == 1:
            everything('beispiel1.txt')
        if int(example) == 2:
            everything('beispiel2.txt')
        if int(example) == 3:
            everything('beispiel3.txt')
    else:
        print('Die Eingabe war leider ungültig, bitte starten Sie das Programm erneut.')
