import random

# symbols representing dead or alive cells
DEAD = '.'
ALIVE = '0'

def init(rows, cols):
    # populate matrix with 0's
    matrix = [ [j * 0 for j in range(cols)] for i in range(rows) ]
    # populate matrix of i rows and j columns with 0's and *'s
    for i in range(rows):
        for j in range(cols):
            matrix[i][j] = ALIVE if random.randint(0, 1) else DEAD
    return matrix

def build(matrix, rows, cols, _100th_step=100):
    print('\nStarting Cellular Matrix ⚡☄️💨🚀')
    draw(matrix, cols)
    while _100th_step > 0:
        next_matrix = init(rows, cols)
        for i in range(rows):
            for j in range(cols):
                state = matrix[i][j] # get current cell value
                # get total number of living and dead neighbor of cell
                n_alive, _ = get_neighbors(matrix, i, j, rows, cols)
                if state == ALIVE and n_alive in (2,3,4) \
                        or state == DEAD and ((n_alive % 2 == 0) and n_alive > 0):
                    next_matrix[i][j] = ALIVE
                else:
                    next_matrix[i][j] = DEAD
        matrix = next_matrix
        _100th_step -= 1
    print('\nFinal Cellular Matrix⚡☄️💨🚀')
    draw(matrix, cols)

def get_neighbors(matrix, x_index, y_index, total_number_of_rows, total_number_of_cols):
    result = {'dead': 0, 'alive': 0}
    for row in range(-1, 2):
        for col in range(-1, 2):
            neighbor_row = x_index + row
            neighbor_col = y_index + col
            # check to see if it's a valid neighbor
            if (neighbor_row == x_index and neighbor_col == y_index) \
                    or (neighbor_row < 0 or neighbor_row >= total_number_of_rows) \
                    or (neighbor_col < 0 or neighbor_col >= total_number_of_cols):
                continue
            else:
                state = matrix[neighbor_row][neighbor_col]
                if state == DEAD:
                    result['dead'] += 1
                else:
                    result['alive'] += 1
    return result['alive'], result['dead']

def draw(matrix, width):
    """beautify grid on terminal."""
    # TODO: instead of printing the matrices on the terminal, save it on a file, maybe?
    header = "==** Game of life **=="
    footer = "==** .. **=="
    print(f"\n\t{header:^{width}}")
    for el in matrix:
        print(f"\t{''.join(el)}")
    print(f'\t{footer:^{width}}')

if __name__ == '__main__':
    print("Let's generate a Cellular Matrix 🎲 📌\n")
    q = ''
    while q.lower() not in ('n', 'no') :
        try:
            rows = int(input('Number of rows: '))
            columns = int(input('Number of columns: '))
            seed = input("Seed (or leave empty if you want to use the system generarted seed): ")
            # ~> see: https://docs.python.org/3/library/random.html
            # -> you may also find this useful: https://stackoverflow.com/questions/22639587/random-seed-what-does-it-do
            # initialize the random number generator
            random.seed(seed) if seed else random.seed()
            # the below methods call will do the magic:-)
            matrix = init(rows, columns)
            build(matrix, rows, columns) 
        except ValueError as e: # TODO: catch any other error/exception that may occur
            print(f'An error occurred - {e}\nPlease try again..')
        finally:
            q = input('Would you like to generate another cellular matrix [Y/N]?: ')
    print("🎆🎉🎇 Thank you for using the program 🎆🎉🎇")
