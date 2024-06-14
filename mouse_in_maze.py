from colorama import Fore

# Get the starting and finishing points of the maze
def get_starting_finishing_points():
    _start = [i for i in range(len(maze[0])) if maze[0][i] == 'C']
    _end = [i for i in range(len(maze[0])) if maze[len(maze)-1][i] == 'C']
    return [0, _start[0]], [len(maze) - 1, _end[0]]

# Print the maze
def print_maze():
    print("TODO: Implement print_maze()", end="\n")

# Escape the maze
def escape():
    print("TODO: Implement escape()", end="\n")

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
    escape()
    print_maze()
