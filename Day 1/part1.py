import string

total = 0

with open("input.txt", "r") as f:

    for line in f.read().split("\n"):

        numbers = []

        for letter in line:
            
            if not (letter in string.ascii_lowercase): 
                numbers.append(letter)
        
        total += int(f"{numbers[0]}{numbers[-1]}")

    f.close()

print(f"The total is: {total}")