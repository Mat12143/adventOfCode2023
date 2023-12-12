from queue import Queue

queue = Queue()
matchesPerCard = {}
total = 0

with open("input.txt", "r") as f:

    for gameLine in f.readlines():
        
        cardID, numbers = gameLine.split(":")

        cardID = int(cardID.replace("Card ", ""))

        winningNumbers, ourNumbers = numbers.split("|")

        ourNumbers =  set(ourNumbers.split())
        winningNumbers = set(winningNumbers.split())

        matches = ourNumbers & winningNumbers

        matchesPerCard[cardID] = len(matches)

        queue.put(cardID)


while not queue.empty():
    total += 1

    k = queue.get()

    for i in range(k + 1, k + matchesPerCard[k] + 1):
        queue.put(i)

print(total)