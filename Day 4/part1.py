with open("input.txt", "r") as f:

    totalSum = 0

    for gameLine in f.read().split("\n"):
        
        card = gameLine.split(":")
        cardNumber = card[0].replace("Card ", "")
        cardNumbers = card[1]

        numbers = cardNumbers.split("|")
        cardNumbers = numbers[0]
        winningNumbers = numbers[1]

        cardNumbers = cardNumbers.split(" ")
        winningNumbers = winningNumbers.split(" ")

        cardValue = 0

        for number in cardNumbers:

            for wNumber in winningNumbers:

                if (len(wNumber) == 0 or len(number) == 0): continue

                if (int(number) != int(wNumber)): continue

                if (cardValue != 0): cardValue *= 2
                else: cardValue += 1

        totalSum += cardValue
        
print(totalSum)