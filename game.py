# Clear the UI Grid
def clear_grid():
    return [[" ", " ", " "] for i in range(3)]


# Zero the matrix weights corresponding to player moves
def zero_game():
    return [[0, 0, 0] for i in range(3)]


def print_grid(cells):
    for i in range(3):
        print("{} | {} | {}".format(cells[i][0], cells[i][1], cells[i][2]))
        print("_________")


def check_winner(cells):
    for i in range(3):
        row_sum = 0
        column_sum = 0
        diag1_sum = 0
        diag2_sum = 0
        for j in range(3):
            row_sum += cells[i][j]
            column_sum += cells[j][i]
            diag1_sum += cells[j][j]
            diag2_sum += cells[j][2-j]
        if (row_sum == 3) or (column_sum == 3):
            return 0
        if (row_sum == -3) or (column_sum == -3):
            return 1
        if (diag1_sum == 3) or (diag2_sum == 3):
            return 0
        if (diag1_sum == -3) or (diag2_sum == -3):
            return 1


if __name__ == "__main__":
    cell_numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    cell_positions = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2)
    }
    allowed_moves = [i for i in range(1, 10)]
    cells = zero_game()
    ui_cells = clear_grid()
    players = ["Player 1", "Player 2"]
    player_turn = 0

    while True:
        player1 = input("Press X or O to choose:\n")
        if player1 in ["X", "x"]:
            player2 = "O"
            print("Player 2 you play with O")
            break
        if player1 in ["O", "o"]:
            player2 = "X"
            print("Player 2 you play with X")
            break
    
    print("To play simply enter the number of the cell")
    print_grid(cell_numbers)

    counter = 0
    while counter < 9:
        while True:
            selected_cell = int(input(players[player_turn] + " turn \n"))
            if selected_cell in allowed_moves:
                break
            else:
                print("Enter a number in " + str(allowed_moves))

        if player_turn == 0:
            cells[cell_positions[selected_cell][0]][cell_positions[selected_cell][1]] += 1
            ui_cells[cell_positions[selected_cell][0]][cell_positions[selected_cell][1]] = "X"
        if player_turn == 1:
            cells[cell_positions[selected_cell][0]][cell_positions[selected_cell][1]] += -1
            ui_cells[cell_positions[selected_cell][0]][cell_positions[selected_cell][1]] = "O"

        print_grid(ui_cells)
        winner = check_winner(cells)
        if (winner == 0) or (winner == 1):
            print(players[winner] + " won")
            break


        player_turn = (player_turn+1) % 2
        counter += 1
