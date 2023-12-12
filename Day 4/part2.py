numberCardsToPlay = []


class Card:

    def __init__(self, wcardNumber, inningNumbers, givenNumbers):
        self.winningNumbers = winningNumbers
        self.givenNumbers = givenNumbers
        self.cardNumber = cardNumber
    
    def solveCard(self):

        i = self.cardNumber

        for number in self.givenNumbers:
            for wNumber in self.winningNumbers:
                if (number == wNumber):
                    i += 1
                    numberCardsToPlay.append(i)

with open("input.txt", "r") as f:

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



        if (len(wNumber) == 0 or len(number) == 0): continue

        if (int(number) != int(wNumber)): continue

        totalSum += cardValue