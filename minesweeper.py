import random

def initialize_board(width, height, num_mines):
    # Create an empty Minesweeper board
    board = [[" " for _ in range(width)] for _ in range(height)]

    # Place mines randomly on the board
    for _ in range(num_mines):
        x, y = random.randint(0, width - 1), random.randint(0, height - 1)
        while board[y][x] == "X":
            x, y = random.randint(0, width - 1), random.randint(0, height - 1)
        board[y][x] = "X"

    # Calculate numbers in neighboring cells
    for y in range(height):
        for x in range(width):
            if board[y][x] != "X":
                count = 0
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if 0 <= x + dx < width and 0 <= y + dy < height and board[y + dy][x + dx] == "X":
                            count += 1
                if count > 0:
                    board[y][x] = str(count)

    return board

def print_board(board, uncover):
    width = len(board[0])
    height = len(board)

    print("  ", end="")
    for i in range(width):
        print(f"{i} ", end="")
    print("\n")

    for y in range(height):
        print(f"{y} ", end="")
        for x in range(width):
            if uncover[y][x]:
                print(f"{board[y][x]} ", end="")
            else:
                print(". ", end="")
        print("\n")

def uncover_cells(board, uncover, x, y):
    if uncover[y][x]:
        return
    uncover[y][x] = True

    if board[y][x] == " ":
        width = len(board[0])
        height = len(board)
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if 0 <= x + dx < width and 0 <= y + dy < height:
                    uncover_cells(board, uncover, x + dx, y + dy)

def main():
    width = 8
    height = 8
    num_mines = 10
    board = initialize_board(width, height, num_mines)
    uncover = [[False for _ in range(width)] for _ in range(height)]

    while True:
        print_board(board, uncover)
        x = int(input("Enter x-coordinate: "))
        y = int(input("Enter y-coordinate: "))

        if board[y][x] == "X":
            print("Game Over! You hit a mine.")
            break

        uncover_cells(board, uncover, x, y)

if __name__ == "__main__":
    main()
