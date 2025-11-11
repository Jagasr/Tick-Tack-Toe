import random

def luarange(b, START=1):
    return range(START, b+1)

def grid(dict):
    print("/------|--------|------\\")
    print("|   " + dict[1] + "  |    " + dict[2] + "   |   " + dict[3] + "  |")
    print("|------|--------|------|")
    print("|   " + dict[4] + "  |    " + dict[5] + "   |   " + dict[6] + "  |")
    print("|------|--------|------|")
    print("|   " + dict[7] + "  |    " + dict[8] + "   |   " + dict[9] + "  |")
    print("\\------|--------|------/")

gram = [None, '1', '2', '3', '4', '5', '6', '7', '8', '9']

winner_gramx = [[1,2,3], [4,5,6], [7,8,9], [7,5,3], [1,5,9], [1,4,7], [2,5,8], [3,6,9]]
winner_gramo = [[1,2,3], [4,5,6], [7,8,9], [7,5,3], [1,5,9], [1,4,7], [2,5,8], [3,6,9]]

# Even if the player doesn't chose X, it is coded as if the player is X anyway in variable names.

x = 'X' # 10
o = '0' # 10

print("Would you like to be Xs or 0s? Type 'X' and enter for X, type any other key for 0s")
print("Type: ", end='')
tempx = input().lower()
if not 'x' in tempx:
    x = '0'
    o = 'X'
print("We have set you to " + x + "s. Enjoy!")

lualist = luarange(9) # To prevent the program from doing the same operation millions of times.
lualist2 = luarange(8)

for moves in luarange(5):
    grid(gram)

    print("Type: ", end='')
    value = input()

    try:
        int(value)
        str(value)
    except:
        print("There was an error with your input and so we need to close. Sorry.")
        quit()

    if int(value) > 9 or int(value) < 1:
        print("There was an error with your input and so we need to close. Sorry.")
        quit()
    
    for i in lualist:
        if str(i) in value and not (gram[i] == 'X' or gram[i] == '0'):
            numb = gram[i] # Independant
            gram[i] = x

            for i2 in winner_gramx: # Add to the winner database
                valueindex = 0 # IMPORTANT: The embedded lists start at zero instead of one.
                for i3 in i2:
                    if i3 == int(numb): # numb equals X as a index number
                        i2[valueindex] = 10

                    valueindex = valueindex + 1
            while True: # This is the computer playing the game now
                num = random.randint(1,9)
                if not (gram[num] == 'X' or gram[num] == '0'):
                    gram[num] = o
                    for i2 in winner_gramo: # Add to the winner database
                        valueindex = 0 # IMPORTANT: The embedded lists start at zero instead of one.
                        for i3 in i2:
                            if i3 == num: # num equals X as a index number
                                i2[valueindex] = 10
                            valueindex = valueindex + 1
                    break
                if (gram[1] == 'X' or gram[1] == '0') and (gram[2] == 'X' or gram[2] == '0') and (gram[3] == 'X' or gram[3] == '0') and (gram[4] == 'X' or gram[4] == '0') and (gram[5] == 'X' or gram[5] == '0') and (gram[6] == 'X' or gram[6] == '0') and (gram[7] == 'X' or gram[7] == '0') and (gram[8] == 'X' or gram[8] == '0') and (gram[9] == 'X' or gram[9] == '0'):
                    break

    for i in winner_gramx:
        if i == [10, 10, 10]:
            print("You Win!")

            print("\nThis was how the game turned out:")
            grid(gram)
            quit()
    for i in winner_gramo:
        if i == [10, 10, 10]:
            print("You lose! The computer Wins.")

            print("\nThis was how the game turned out:")
            grid(gram)
            quit()

print("You Win! There was a draw.")
