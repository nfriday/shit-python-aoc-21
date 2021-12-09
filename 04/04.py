data = open("04/input.txt","r").read().split("\n\n")

selections = data[0].split(",")

num_boards = [[[z for z in j.split(" ") if len(z)>0] for j in i.split("\n")] for i in data[1:]]

bingo_boards = [[[0] * 5 for _ in range(5)] for i in num_boards]

def arrprod(arr):
    product=1
    for x in arr: product *= x
    return product

def solved(board):
    col_solved = len([x for x in [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))] if arrprod(x)==1])==1
    row_solved = len([i for i in board if arrprod(i)==1])==1
    return (col_solved or row_solved)

solved_boards = []
solved_nums = []
for num in selections:
    for board in range(len(num_boards)):
        
        for row in range(len(num_boards[0])):
            for col in range(len(num_boards[0][0])):                
                if num_boards[board][row][col]==num and not board in solved_boards: bingo_boards[board][row][col]=1

        if not board in solved_boards and solved(bingo_boards[board]):
            solved_boards.append(board)
            solved_nums.append(num)
            
    if len(solved_boards)>=len(num_boards): break

def answer(x):
    final_sum = 0
    board=solved_boards[x]
    num_board = num_boards[board]
    bingo_board = bingo_boards[board]
    solved_num = solved_nums[x]
    for row in range(len(num_board)):
        for col in range(len(bingo_board)):
            if bingo_board[row][col]==0: final_sum += int(num_board[row][col])
    return final_sum*int(solved_num)

# part 1
print(answer(0))

# part 2
print(answer(len(solved_boards)-1))


