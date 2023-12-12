# x-to-y
# dest source steps

seeds = []


seedToSoil = []

maps = []

with open("input.txt", "r") as f:

    lines = f.read().split("\n\n")

    for i in range(len(lines)):

        line = lines[i]

        if line.startswith("seeds"): seeds = list(line.replace("seeds: ", "").split())

        if "map:" in line:
            rawValues = line.split("\n")[1:]

            convertMap = []
            
            for valueSet in rawValues:

                numbers = valueSet.split(" ")

                dataMap = {
                    "start": int(numbers[1]),
                    "end": int(numbers[1]) + int(numbers[2]),
                    "startDest": int(numbers[0]),
                    "toAdd": int(numbers[2])
                }

                convertMap.append(dataMap)

            maps.append(convertMap)

# [ map[{entry}, {entry}], map[{entry}] ]

print(maps)

seedInfo = []
for seed in seeds:

    seed = int(seed)
    convertedValues = []

    for i in range(len(maps)):
        convertionDone = False
        
        for entry in maps[i]:

            if ((seed >= entry["start"] and seed <= entry["end"]) and convertionDone == False):

                start = entry["start"]
                end = entry["end"]

                print(f"PASSED {seed} {start} {end}")

                convertedValues.append(entry["startDest"] + seed - entry["start"])
                convertionDone = True
                break

        if not convertionDone:
            convertedValues.append(seed)

    convertedValues.append(seed)
    seedInfo.append(convertedValues)


print(seedInfo)