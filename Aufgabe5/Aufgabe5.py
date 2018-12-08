listResistors = [1000, 5600, 180, 6800, 8200, 820, 2700, 150, 100, 1800, 220, 1500, 330, 390, 680, 120, 3900, 3300, 4700, 560, 470, 1200, 270, 2200]

def start():
    wantedResistance = input("Bitte geben Sie den gewuenschten Widerstand ein: ")
    listResistors.sort()        #aufsteigend
    print ("k = 1:")
    print(createResistanceK1(wantedResistance))

    # print(createResistanceK2(wantedResistance))

# def getAbsolutValue(x):
#     if x < 0:
#         return -x
#     else:
#         return x

def createResistanceK1( wantedResistance ):
    minDif = abs(listResistors[0] - wantedResistance)
    bestResistor = 0
    for r in listResistors:
        if abs(r - wantedResistance) < minDif:
            minDif = abs(r - wantedResistance)
            bestResistor = r
    return minDif, bestResistor

def createResistanceK2( listResistors, wantedResistance):
    minDifSer = 9999999999
    minDifPar = 9999999999
    bestResistorCombinationSer = ""
    bestResistorCombinationPar = ""
    seriell = False
    # Serielle Schaltung
    for r in listResistors:
        DifSer = 0
        checkList = listResistors.remove(r)        #Jeder Widerstand hat mit sich selber die geringste Differenz
        ResHilf = createResistanceK1( checkList, getAbsolutValue(wantedResistance - r))[0] + r
        DifSer = getAbsolutValue(ResHilf - wantedResistance)
        if DifSer < minDifSer:
            minDiSerf = DifSer
            bestResistorCombinationSer = r, createResistanceK1( checkList, getAbsolutValue(wantedResistance - r))[1]
        checkList = listResistors
    # ParallelSchaltung
    for r in listResistors:
        DifPar = 0
        checklist = listResistors.remove(r)
        ResHilf = 1/(1/(createResistanceK1( checkList, getAbsolutValue(1/wantedResistance - 1/r))[0] + 1/r))
        DifPar = getAbsolutValue(ResHilf - wantedResistance)
        if DifPar < minDifPar:
            minDifPar = minDifPar
            bestResistorCombinationPar = r, createResistanceK1( checkList, getAbsolutValue(wantedResistance -r))[1]
        checkList = listResistors
    if minDifSer < minDifPar:
        seriell = True
        return minDifSer, bestResistorCombinationSer, seriell
    else:
        return minDifPar, bestResistorCombinationPar, seriell
