def start():
    var = input("Please enter a list of all Users (['firstUser', 'secondUser', '...']): ")
    findSuperstar (var)

class User:
    name = "something"
    possibleSuperstar = True
    follower = 0


def findSuperstar( allUsers ):
    users = []
    for x in allUsers:
        newUser = User()
        newUser.name = x
        users.append(newUser)
    nichtGefunden = True
    for i in users:
            for j in users:
                if j.possibleSuperstar and i != j:
                    if folgtxy(i.name, j.name):
                        i.possibleSuperstar = False
                        j.follower += 1
                        if (j.follower == len(allUsers) - 1):           #sich selber kann man ja nicht folgen, deswegen -1
                            nichtGefunden = False
                            print("Der Superstar dieser Gruppe ist: " + j.name)
                            break
                    else:
                        j.possibleSuperstar = False
    if nichtGefunden:
        print("Es gibt keinen Superstar in dieser Gruppe :(")


def folgtxy( user1, user2 ):
    var = input("Folgt " + user1 + " " + user2 + "? (Please enter True/False): ")
    return var

def startExample1():
    
