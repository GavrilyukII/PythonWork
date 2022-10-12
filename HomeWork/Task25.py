# Создайте программу для игры в 'Крестики-нолики'.

print ('Итак, сыграем в крестики-нолики')

board = list(range(1,10))

def print_board(board):
   print("-" * 13)
   for i in range(3):
      print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
      print("-" * 13)


def take_input(player_queue):
   teg = False
   while not teg:
      player_answer = input("Куда поставить " + player_queue+"? ")
      try:
         player_answer = int(player_answer)
      except:
         print("Некорректный ввод. Вы уверены, что ввели число?")
         continue
      if player_answer >= 1 and player_answer <= 9:
         if(str(board[player_answer-1]) not in "XO"):
            board[player_answer-1] = player_queue
            teg = True
         else:
            print("Эта клетка уже занята!")
      else:
        print("Некорректный ввод. Введите число от 1 до 9.")

def win_case(board):
   victory = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
   for i in victory:
       if board[i[0]] == board[i[1]] == board[i[2]]:
          return board[i[0]]
   return False

def main(board):
    counter = 0
    win = False
    while not win:
        print_board(board)
        if counter % 2 == 0:
           take_input("X")
        else:
           take_input("O")
        counter += 1
        if counter > 4:
           tmp = win_case(board)
           if tmp:
              print(tmp, "выиграл!")
              win = True
              break
        if counter == 9:
            print("Ничья!")
            break
    print_board(board)
main(board)

