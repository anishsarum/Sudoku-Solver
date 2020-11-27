import pygame

# colours
WHITE = 255, 255, 255
GREY = 100, 100, 100
BLACK = 0, 0, 0
GREEN = 0, 120, 0

# number of frames per second
FPS = 60

# initialising pygame
pygame.init()
pygame.display.set_caption("Sudoku Solver")
numbers = pygame.font.SysFont("notosans", 30)


# window size
screen = pygame.display.set_mode((9*50+5, 9*50+5))

def valid_check(board):
    valid = check_row(board) and check_column(board) and check_square(board)
    return valid


def check_row(board):
    bools = []

    for i in range(9):
        validity = bools.append(
            [x for x in sorted(board[i]) if x != 0] == [x for x in sorted(list(set(board[i]))) if x != 0])

    return all(bools)


def check_column(board):
    bools = []
    board = list(map(list, zip(*board)))

    for i in range(9):
        validity = bools.append(
            [x for x in sorted(board[i]) if x != 0] == [x for x in sorted(list(set(board[i]))) if x != 0])

    return all(bools)


def check_square(board):
    bools = []
    box_board = []

    for j in range(3):
        for i in range(3):
            box = take(j * 3, j * 3 + 3, [x for x in board[3 * i]]) +\
                  take(j * 3, j * 3 + 3, [x for x in board[3 * i + 1]]) +\
                  take(j * 3, j * 3 + 3, [x for x in board[3 * i + 2]])
            box_board.append(box)

    for i in range(9):
        bools.append([x for x in sorted(box_board[i]) if x != 0] ==
                     [x for x in sorted(list(set(box_board[i]))) if x != 0])

    return all(bools)


def take(n, p, t_list):
    new = []
    for i in range(n):
        t_list.pop(0)
    for i in range(p - n):
        new.append(t_list.pop(0))
    return new


def find_empty(board, i, j):
    for x in range(i, 9):
        for y in range(j, 9):
            if board[x][y] == 0:
                return x, y
    for x in range(0, 9):
        for y in range(0, 9):
            if board[x][y] == 0:
                return x, y
    return -1, -1


def solve(board, i=0, j=0):
    i, j = find_empty(board, i, j)
    if i == -1:
        return True
    for e in range(1, 10):
        screen.fill(WHITE)
        board[i][j] = e

        pygame.draw.line(screen, GREY, (0, 150), (500, 150), 1)
        pygame.draw.line(screen, GREY, (0, 300), (500, 300), 1)
        pygame.draw.line(screen, GREY, (150, 0), (150, 500), 1)
        pygame.draw.line(screen, GREY, (300, 0), (300, 500), 1)

        for x in range(9):
            for y in range(9):
                number_text = numbers.render(str(board[y][x]), True, BLACK)
                screen.blit(number_text, ((x+1)*50-45+10, (y+1)*50-45))

        pygame.display.update()
        pygame.time.Clock().tick(FPS)

        if valid_check(board):
            if solve(board, i, j):
                return True
        board[i][j] = 0
    return False


def main(board):
    while True:
        # refreshes screen each turn
        screen.fill(WHITE)

        solve(board)

        pygame.draw.line(screen, GREY, (0, 150), (500, 150), 1)
        pygame.draw.line(screen, GREY, (0, 300), (500, 300), 1)
        pygame.draw.line(screen, GREY, (150, 0), (150, 500), 1)
        pygame.draw.line(screen, GREY, (300, 0), (300, 500), 1)

        for x in range(9):
            for y in range(9):
                number_text = numbers.render(str(board[y][x]), True, GREEN)
                screen.blit(number_text, ((x+1)*50-45+10, (y+1)*50-45))

        pygame.display.update()
        pygame.time.Clock().tick(FPS)


if __name__ == "__main__":
    puzzle = eval(input("Enter puzzle here: "))
    main(puzzle)

sampleBoard = [[9, 0, 0, 8, 1, 0, 0, 0, 0],
               [0, 0, 5, 0, 0, 4, 7, 0, 6],
               [0, 0, 0, 2, 0, 5, 8, 0, 1],
               [0, 9, 0, 7, 4, 0, 5, 0, 0],
               [0, 0, 0, 0, 0, 3, 0, 7, 0],
               [7, 4, 0, 0, 0, 0, 0, 0, 0],
               [3, 0, 0, 9, 5, 0, 6, 0, 0],
               [0, 0, 6, 4, 0, 0, 0, 1, 3],
               [1, 7, 0, 0, 0, 0, 0, 0, 4]]

sampleBoard2 = [[5, 1, 7, 6, 0, 0, 0, 3, 4],
                [2, 8, 9, 0, 0, 4, 0, 0, 0],
                [3, 4, 6, 2, 0, 5, 0, 9, 0],
                [6, 0, 2, 0, 0, 0, 0, 1, 0],
                [0, 3, 8, 0, 0, 6, 0, 4, 7],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 9, 0, 0, 0, 0, 0, 7, 8],
                [7, 0, 3, 4, 0, 0, 5, 6, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0]]

# [[9, 0, 0, 8, 1, 0, 0, 0, 0],[0, 0, 5, 0, 0, 4, 7, 0, 6],[0, 0, 0, 2, 0, 5, 8, 0, 1],[0, 9, 0, 7, 4, 0, 5, 0, 0],[0, 0, 0, 0, 0, 3, 0, 7, 0],[7, 4, 0, 0, 0, 0, 0, 0, 0],[3, 0, 0, 9, 5, 0, 6, 0, 0],[0, 0, 6, 4, 0, 0, 0, 1, 3],[1, 7, 0, 0, 0, 0, 0, 0, 4]]
