from colorama import Fore

# Get the starting and finishing points of the maze
def get_starting_finishing_points():
    _start = [i for i in range(len(maze[0])) if maze[0][i] == 'C']
    _end = [i for i in range(len(maze[0])) if maze[len(maze)-1][i] == 'C']
    return [0, _start[0]], [len(maze) - 1, _end[0]]

# Print the maze
def print_maze():
    for i in range(0, len(maze)):
        for j in range(0, len(maze[0])):
            if maze[i][j] == 'U':
                print(Fore.WHITE, f'{maze[i][j]}', end=" ")
            elif maze[i][j] == 'C':
                print(Fore.GREEN, f'{maze[i][j]}', end=" ")
            elif maze[i][j] == 'P':
                print(Fore.BLUE, f'{maze[i][j]}', end=" ")
            else:
                print(Fore.RED, f'{maze[i][j]}', end=" ")
        print('\n')

# Escape the maze
def escape():
    current_cell = mouse_path[len(mouse_path) - 1]

    if current_cell == finish:
        return

    if maze[current_cell[0] + 1][current_cell[1]] == 'C':
        maze[current_cell[0] + 1][current_cell[1]] = 'P'
        mouse_path.append([current_cell[0] + 1, current_cell[1]])
        escape()

    if maze[current_cell[0]][current_cell[1] + 1] == 'C':
        maze[current_cell[0]][current_cell[1] + 1] = 'P'
        mouse_path.append([current_cell[0], current_cell[1] + 1])
        escape()

    if maze[current_cell[0] - 1][current_cell[1]] == 'C':
        maze[current_cell[0] - 1][current_cell[1]] = 'P'
        mouse_path.append([current_cell[0] - 1, current_cell[1]])
        escape()

    if maze[current_cell[0]][current_cell[1] - 1] == 'C':
        maze[current_cell[0]][current_cell[1] - 1] = 'P'
        mouse_path.append([current_cell[0], current_cell[1] - 1])
        escape()

    current_cell = mouse_path[len(mouse_path) - 1]
    if current_cell != finish:
        cell_to_remove = mouse_path[len(mouse_path) - 1]
        mouse_path.remove(cell_to_remove)
        maze[cell_to_remove[0]][cell_to_remove[1]] = 'C'


if __name__ == '__main__':
    maze = [
        ['W', 'C', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W',
         'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
        ['W', 'C', 'C', 'W', 'C', 'W', 'C', 'C', 'W', 'W', 'C', 'C', 'C', 'C',
         'C', 'W', 'W', 'C', 'W', 'W', 'C', 'C', 'C', 'C', 'C', 'C', 'W'],
        ['W', 'W', 'C', 'W', 'C', 'C', 'C', 'W', 'W', 'W', 'W', 'W', 'W', 'W',
         'C', 'C', 'C', 'C', 'C', 'W', 'W', 'W', 'W', 'W', 'W', 'C', 'W'],
        ['W', 'C', 'C', 'C', 'C', 'W', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C',
         'C', 'W', 'C', 'W', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'W'],
        ['W', 'W', 'W', 'C', 'W', 'W', 'C', 'W', 'C', 'W', 'C', 'W', 'W', 'W',
         'W', 'W', 'W', 'W', 'W', 'W', 'W', 'C', 'W', 'W', 'W', 'C', 'W'],
        ['W', 'C', 'C', 'C', 'C', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'C',
         'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'W', 'C', 'C', 'C', 'W'],
        ['W', 'C', 'W', 'C', 'W', 'W', 'W', 'W', 'C', 'C', 'W', 'C', 'W', 'W',
         'W', 'C', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'C', 'W'],
        ['W', 'W', 'W', 'W', 'W', 'W', 'C', 'W', 'W', 'C', 'C', 'C', 'W', 'C',
         'W', 'W', 'W', 'W', 'W', 'W', 'C', 'C', 'C', 'C', 'C', 'C', 'W'],
        ['W', 'C', 'C', 'C', 'C', 'C', 'C', 'W', 'W', 'W', 'W', 'C', 'W', 'C',
         'C', 'C', 'C', 'C', 'C', 'C', 'C', 'W', 'C', 'W', 'C', 'W', 'W'],
        ['W', 'W', 'C', 'W', 'C', 'W', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C',
         'W', 'W', 'C', 'W', 'C', 'W', 'C', 'W', 'C', 'W', 'C', 'C', 'W'],
        ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W',
         'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'C', 'W']
    ]

    start, finish = get_starting_finishing_points()
    maze[start[0]][start[1]] = 'P'

    mouse_path = [start]
    print_maze()
    escape()
