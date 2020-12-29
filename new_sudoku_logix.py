from random import sample


def print_arr(li):
    for i in li:
        for j in range(3):
            for k in range(9):
                print(i[j][k], end=' ')
            print()
    print("-"*20)


def transpose_grid(grid):
    block_c = []
    i = 0
    for j in range(3):
        bl_tmp = [[grid[0][i][j*3+0], grid[0][i+1][j*3+0], grid[0][i+2][j*3+0],
                   grid[1][i][j*3+0], grid[1][i+1][j*3+0], grid[1][i+2][j*3+0],
                   grid[2][i][j*3+0], grid[2][i+1][j*3+0], grid[2][i+2][j*3+0]],
                  [grid[0][i][j*3+1], grid[0][i+1][j*3+1], grid[0][i+2][j*3+1],
                   grid[1][i][j*3+1], grid[1][i+1][j*3+1], grid[1][i+2][j*3+1],
                   grid[2][i][j*3+1], grid[2][i+1][j*3+1], grid[2][i+2][j*3+1]],
                  [grid[0][i][j*3+2], grid[0][i+1][j*3+2], grid[0][i+2][j*3+2],
                   grid[1][i][j*3+2], grid[1][i+1][j*3+2], grid[1][i+2][j*3+2],
                   grid[2][i][j*3+2], grid[2][i+1][j*3+2], grid[2][i+2][j*3+2]]]
        block_c.append(bl_tmp)
    return block_c


def randomize_grid(bl_r):
    bl_r = sample(bl_r, 3)
    bl_r[0] = sample(bl_r[0], 3)
    bl_r[1] = sample(bl_r[1], 3)
    bl_r[2] = sample(bl_r[2], 3)
    return bl_r


default_grid = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
                [4, 5, 6, 7, 8, 9, 1, 2, 3],
                [7, 8, 9, 1, 2, 3, 4, 5, 6],
                [2, 3, 4, 5, 6, 7, 8, 9, 1],
                [5, 6, 7, 8, 9, 1, 2, 3, 4],
                [8, 9, 1, 2, 3, 4, 5, 6, 7],
                [3, 4, 5, 6, 7, 8, 9, 1, 2],
                [6, 7, 8, 9, 1, 2, 3, 4, 5],
                [9, 1, 2, 3, 4, 5, 6, 7, 8]]

block_r = [[default_grid[0], default_grid[1], default_grid[2]],
           [default_grid[3], default_grid[4], default_grid[5]],
           [default_grid[6], default_grid[7], default_grid[8]]]

x = 100
while (x > 0):
    block_r = randomize_grid(block_r)
    block_r = transpose_grid(block_r)
    block_r = randomize_grid(block_r)
    block_r = transpose_grid(block_r)
    x = x-1

game_grid = block_r.copy()

print_arr(game_grid)
