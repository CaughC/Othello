def put(person,y,x):
    change = []
    if x != 0:
        if board[y][x-1] != person:
            change.append([0,-1,y,x])
        if y != 0:
            if board[y-1][x-1] != person:
                change.append([-1,-1,y,x])
        if y != 7:
            if board[y+1][x-1] != person:
                change.append([1,-1,y,x])
    if y != 0 and board[y-1][x] != person:
        change.append([-1,0,y,x])
    if y != 7 and board[y+1][x] != person:
        change.append([1,0,y,x])
    if x != 7:
        if board[y][x+1] != person:
            change.append([0,1,y,x])
        if y != 0:
            if board[y-1][x+1] != person:
                change.append([-1,1,y,x])
        if y != 7:
            if board[y+1][x+1] != person:
                change.append([1,1,y,x])
    return change
    
def checkColor(person,opponent,directionY,directionX,y,x):
    attempt = 0
    subjectY,subjectX = y,x
    while True:
        subjectX = subjectX + directionX
        subjectY = subjectY + directionY
        if subjectX == -1 or subjectX == 8 or subjectY == -1 or subjectY == 8:
            attempt = 0
            break
        if opponent == board[subjectY][subjectX]:
            attempt = 1
        elif "_" == board[subjectY][subjectX]:
            attempt = 0
            break
        elif attempt == 0 and person == board[subjectY][subjectX]:
            break
        elif attempt == 1 and person == board[subjectY][subjectX]:
            break
    return attempt

def changeColor(person,opponent,directionY,directionX,y,x):
    subjectY = y + directionY
    subjectX = x + directionX
    board[y][x] = person
    while True:
        if board[subjectY][subjectX] == opponent:
            board[subjectY][subjectX] = person
        else:
            break
        subjectX += directionX
        subjectY += directionY

print("オセロを始めます。")
print("コンピュータを相手にする場合は1を、対人戦を行う場合は2を入力してください")
How2play = int(input())
print("先攻使う文字（1字)を入力してください")
player1 = input()
print("後攻攻使う文字（1字)を入力してください")
while True:
    player2 = input()
    if player1 == player2:
        print("先攻と違う文字を使用してください。再度入力してください")
    else:
        break

board = []
for i in range(8):
    board.append(['_','_','_','_','_','_','_','_'])
board[3][3],board[4][4] = player1,player1
board[3][4],board[4][3] = player2,player2

verticalCharacter = ['A','B','C','D','E','F','G','H']

skip = 0
while skip < 2:
    print(' 0 1 2 3 4 5 6 7')
    for i in range(8):
        print(verticalCharacter[i] + ' '.join(board[i]))
    while True:
        print("先攻どこに置くか入力(左上をA 0、右上をA 7、右下を7 7とする)(置く場所が無いならskip)")
        command = []
        command = input().split(' ')
        if command[0] =="skip":
            skip += 1
            break
        if verticalCharacter.count(command[0]) == 0 or not command[1].isnumeric():
            print("その値は無効です。再入力してください")
            continue
        if int(command[1]) < 0 or int(command[1]) > 7:
            print("その値は無効です。再入力してください")
            continue        
        place = [verticalCharacter.index(command[0]),int(command[1])]        
        if board[int(place[0])][int(place[1])] == player1 or board[int(place[0])][int(place[1])] == player2:
            print("その場所には置けません")
            continue
        check = put(player1, int(place[0]),int(place[1]))
        attemptCount = 0
        deadEndList = []
        for i in range(len(check)):
            attempt= checkColor(player1,player2,check[i][0],check[i][1],check[i][2],check[i][3])
            attemptCount += attempt
            if attempt == 0:
                deadEndList.append(i)
        if attemptCount == 0:
            print("その場所には置けません")
            continue
        else:
            deadEndList.sort(reverse=True)
            for i in deadEndList:
                del check[i]                            
            for i in range(len(check)):
                changeColor(player1,player2,check[i][0],check[i][1],check[i][2],check[i][3])
                skip = 0
        break
    print(' 0 1 2 3 4 5 6 7')
    for i in range(8):
        print(verticalCharacter[i] + ' '.join(board[i]))
    while True:
        print("後攻どこに置くか入力(左上をA 0、右上をA 7、右下を7 7とする)(置く場所が無いならskip)")
        command = []
        command = input().split(' ')
        if command[0] == "skip":
            skip += 1
            break
        if verticalCharacter.count(command[0]) == 0 or not command[1].isnumeric():
            print("その値は無効です。再入力してください")
            continue
        if int(command[1]) < 0 or int(command[1]) > 7:
            print("その値は無効です。再入力してください")
            continue        
        place = [verticalCharacter.index(command[0]),int(command[1])]
        if board[int(place[0])][int(place[1])] == player1 or board[int(place[0])][int(place[1])] == player2:
            print("その場所には置けません")
            continue
        check = put(player2, int(place[0]),int(place[1]))
        attemptCount = 0
        deadEndList = []
        for i in range(len(check)):
            attempt= checkColor(player2,player1,check[i][0],check[i][1],check[i][2],check[i][3])
            attemptCount += attempt
            if attempt == 0:
                deadEndList.append(i)
        if attemptCount == 0:
            print("その場所には置けません")
            continue
        else:
            deadEndList.sort(reverse=True)
            for i in deadEndList:
                del check[int(i)]                           
            for i in range(len(check)):
                changeColor(player2,player1,check[i][0],check[i][1],check[i][2],check[i][3])
                skip = 0
        break
result = ""
for i in range(7):
    result += ''.join(board[i])
player1score = 0
player2score = 0
for i in result:
    if i == player1:
        player1score += 1
    elif i == player2:
        player2score += 1
if player1score > player2score:
    print("先攻の勝利です")
elif player1score < player2score:
    print("後攻の勝利です")
elif player1score == player2score:
    print("引き分けです")
