with open("input.txt", "r") as f:

    totalPower = 0

    for gameLine in f.read().split("\n"):
        
        gameInfo = gameLine.split(":")
        gameNumber = gameInfo[0].replace("Game ", "")
        gameCubes = gameInfo[1]

        throws = gameCubes.split(";")

        minCubesReq = {
            "red": 0,
            "green": 0,
            "blue" : 0
        }

        for throw in throws:

            for color in minCubesReq.keys():
                
                position = throw.find(color)
                
                if (position == -1): continue

                nrColorCubes = throw[position - 3 : position - 1]
                nrColorCubes = int(nrColorCubes)

                if (nrColorCubes <= minCubesReq[color]): continue
                minCubesReq[color] = nrColorCubes

        totalPower += minCubesReq["red"] * minCubesReq["green"] * minCubesReq["blue"]
        
print(totalPower)