import random
itemsInTree = []

STRAW = '🍓'
BEE = '🐝'
ORG = '🟠'
GAP = '🍇'
APP = '🍎'
MEL = '🍉'
PI = [STRAW,BEE,ORG,GAP,APP,MEL]
itemsInTree = [
    BEE , ORG , APP , MEL , BEE , STRAW , GAP , MEL 
]

itemsInTree = []

ConstLength = 12

for i in range(ConstLength):
    if i == ConstLength and not itemsInTree.find(BEE):
        itemsInTree.append(BEE);
    else:
        itemsInTree.append(PI[random.randint(0, 5)])

gameOn = True
# if curPlayer == 1 => Player 1 
#    curPlayer == 2 => Player 2
curPlayer = True
player1 = input("Enter player 1 name: ")
player2 = input("Enter player 2 name: ")
print("Welcome to the pepega game.")

while (gameOn) :
    print(itemsInTree)
    userInput = int(input("Please choose the number of items (1 or 2): "))
    if userInput == 1 or userInput == 2: 
        for _ in range(userInput):
            item = itemsInTree.pop()
            if(item == BEE):
                gameOn = False 
        #End of for loop    
        curPlayer = not  curPlayer   
    #End of if   
    else:
        print("Invalid input")

if curPlayer:
    print(player1 + " has won!")
else:
    print(player2 + " has won!")