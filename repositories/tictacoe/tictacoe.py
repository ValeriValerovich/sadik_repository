map = [
    ".", ".", ".",
    ".", ".", ".",
    ".", ".", "."
]

def DisplayPositions():
    print(map[0] + map[1] + map[2])
    print(map[3] + map[4] + map[5])
    print(map[6] + map[7] + map[8])

def SelectNextPositionFromInput():
    playerPositionInput = int(input("Please type what position: "))

    if playerPositionInput == 1:
        map[0] = "X"

    if playerPositionInput == 2:
        map[1] = "X" 

    if playerPositionInput == 3:
        map[2] = "X" 

    if playerPositionInput == 4:
        map[3] = "X" 

    if playerPositionInput == 5:
        map[4] = "X" 

    if playerPositionInput == 6:
        map[5] = "X" 

    if playerPositionInput == 7:
        map[6] = "X" 

    if playerPositionInput == 8:
        map[7] = "X" 

    if playerPositionInput == 9:
        map[8] = "X" 

SelectNextPositionFromInput()
DisplayPositions()

SelectNextPositionFromInput()
DisplayPositions()

SelectNextPositionFromInput()
DisplayPositions()