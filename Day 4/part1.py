with open("input.txt", "r") as f:

    totalSum = 0

    for gameLine in f.readlines():
        
        cardID, numbers = gameLine.split(":")

        cardID = int(cardID.replace("Card ", ""))

        winningNumbers, ourNumbers = numbers.split("|")

        ourNumbers =  set(ourNumbers.split())
        winningNumbers = set(winningNumbers.split())

        matches = ourNumbers & winningNumbers

        if matches: totalSum += 2 ** (len(matches) - 1)
        
print(totalSum)