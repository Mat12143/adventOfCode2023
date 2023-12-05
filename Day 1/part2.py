import string

lettersToNumber = {
    "one" : 1,
    "two" : 2,
    "three" : 3,
    "four" : 4,
    "five" : 5,
    "six" : 6,
    "seven" : 7,
    "eight" : 8,
    "nine" : 9,
}

total = 0

with open("input.txt", "r") as f:

    for line in f.read().split("\n"):

        numbers = []

        for numberWord in lettersToNumber.keys():
            
            line = line.replace(numberWord, f"{numberWord}{lettersToNumber[numberWord]}{numberWord}")

        for letter in line:
            if not (letter in string.ascii_lowercase): 
                numbers.append(letter)
        
        total += int(f"{numbers[0]}{numbers[-1]}")

    f.close()

print(f"The Total is: {total}")