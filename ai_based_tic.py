import os
os.system("cls")

class Board():
    def __init__(self):
        self.cells=[" "," "," "," "," "," "," "," "," "," "]

    def display(self):
        print(" %s | %s | %s " %(self.cells[1],self.cells[2],self.cells[3]))
        print("-------------")
        print(" %s | %s | %s " %(self.cells[4],self.cells[5],self.cells[6]))
        print("-------------")
        print(" %s | %s | %s " %(self.cells[7],self.cells[8],self.cells[9]))

    def cell_update(self,cell_no,player):
        if self.cells[cell_no] == " ":
            self.cells[cell_no] = player

    def is_winner(self,player):
        for combo in [[1,2,3],[4,5,6],[7,8,9],[1,5,9],[3,5,7],[1,4,7],[2,5,8],[3,6,9]]:
            result = True
            for i in combo:
                if self.cells[i]!=player:
                    result = False
            if result == True:
                return True

        return False

    def is_tie(self):
        used_cell = 0
        for cell in self.cells:
            if cell != " ":
                used_cell +=1

        if used_cell == 9:
            return True
        else:
            return False
    def reset(self):
        self.cells=[" "," "," "," "," "," "," "," "," "," "]

    def ai_move(self,player):

        for i in range(1,10):
            if self.cells[i]==" ":
                self.cell_update(i,player)
                break
        

board = Board()

def print_header():
    print("Welcome to Tic Tac Toe\n")

def refresh_screen():

    os.system("cls")

    print_header()
    
    board.display()


while True:
    refresh_screen()

    x_choice = int(input("\n(X)choose between <1-9>: "))

    board.cell_update(x_choice,"X")

    refresh_screen()

    if board.is_winner("X"):
        print("\nX wins\n")
        play_again = input("Do you wanna play again(Y/N) ?")
        if play_again == "Y":
            board.reset()
            continue
        else:
            break

    if board.is_tie():
        print("\nTie game\n")
        play_again = input("Do you wanna play again(Y/N) ?")
        if play_again == "Y":
            board.reset()
            continue
        else:
            break

    board.ai_move("O")

    refresh_screen()

    if board.is_winner("O"):
        print("\nO wins\n")
        play_again = input("Do you wanna play again(Y/N) ?")
        if play_again == "Y":
            board.reset()
            continue
        else:
            break

    if board.is_tie():
        print("\nTie game\n")
        play_again = input("Do you wanna play again(Y/N) ?")
        if play_again == "Y":
            board.reset()
            continue
        else:
            break 
    
        
