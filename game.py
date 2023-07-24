#tic tak toe


board = ["-"]*9
game_winner = ""

def print_board(board):
  print(board[0]+" | "+board[1]+" | "+board[2])
  print(board[3]+" | "+board[4]+" | "+board[5])
  print(board[6]+" | "+board[7]+" | "+board[8])
def user_input(board,ch):
  b = 0
  print("-------This is "+ch+" turn----------")
  print("Enter a position form 1 to 9:")
  pos = int(input())
  if board[pos-1] == "-" and (pos >= 1 and pos <= 9):
    board[pos-1] = ch
    print_board(board)
    b = check_result(board,pos,ch)

  elif board[pos-1] != "-":
    print("Already filled")
    user_input(board,ch)
  else:
    print("Invalid input")
    user_input(board,ch)
  
  
  if b == 1:
    print("The Winner is ",board[pos-1])
    return True


def check_result(board,pos,ch):
  #row check:
  row = (pos-1)//3
  row_ele = board[row*3:(row*3)+3]
  if len(set(row_ele)) == 1:
    return 1

  #column check
  col = pos%3
  col_ele = []
  for i in range(3):
    col_ele.append(board[(3*i)+col])
  if all(ch == ele for ele in col_ele):
    return 1

  #diagonal check
  for i in ([0,4,8],[2,4,6]):
    if pos-1 in i:
      i,j,k = i
      if len(set([board[i],board[j],board[k]])) == 1:
        return 1

print_board(board)
result = False
for i in range(0,9):
  if result != True:
    if i%2 == 0 :
      result = user_input(board,"X")
    else:
      result = user_input(board,"O")    
