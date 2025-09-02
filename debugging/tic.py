#!/usr/bin/python3
def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < len(board) - 1:  # Ne pas afficher la ligne après la dernière rangée
            print("-" * 9)  # Ajusté pour un meilleur alignement

def check_winner(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while not check_winner(board):
        print_board(board)
        try:
            row_input = input("Enter row (0, 1, or 2) for player " + player + ": ")
            col_input = input("Enter column (0, 1, or 2) for player " + player + ": ")
            
            # Vérifier si l'entrée contient des lettres ou des caractères non numériques
            if not row_input.isdigit() or not col_input.isdigit():
                print("Erreur: Veuillez entrer uniquement des chiffres (0, 1, ou 2).")
                continue
            
            row = int(row_input)
            col = int(col_input)
            
            # Vérifier si les coordonnées sont dans les limites (0, 1, ou 2)
            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Erreur: Les coordonnées doivent être 0, 1, ou 2 uniquement.")
                continue
            
            if board[row][col] == " ":
                board[row][col] = player
                if player == "X":
                    player = "O"
                else:
                    player = "X"
            else:
                print("That spot is already taken! Try again.")
        except ValueError:
            print("Erreur: Entrée invalide. Veuillez entrer des nombres entre 0 et 2.")
        except IndexError:
            print("Erreur: Coordonnées hors limites. Utilisez 0, 1, ou 2.")

    print_board(board)
    print("Player " + ("O" if player == "X" else "X") + " wins!")

tic_tac_toe()
