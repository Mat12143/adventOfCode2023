maxCubes = {
    "red" : 12,
    "green": 13,
    "blue" : 14
}

with open("input.txt", "r") as f:

    realGameSum = 0

    for gameLine in f.read().split("\n"):
        
        gameInfo = gameLine.split(":")
        gameNumber = gameInfo[0].replace("Game ", "")
        gameCubes = gameInfo[1]

        throws = gameCubes.split(";")

        isTheGameImpossible = False

        for throw in throws:

            for cube in maxCubes.keys():
                
                position = throw.find(cube)
                
                if (position == -1): continue

                nrCubes = throw[position - 3 : position - 1]

                if (int(nrCubes) <= maxCubes[cube]): continue
                isTheGameImpossible = True


        if not isTheGameImpossible:
            realGameSum += int(gameNumber)
        
print(realGameSum)