import random

# symbols representing dead or alive cells
DEAD = '.'
ALIVE = '0'

def init(rows, cols, seed):
    # to initialize the random number generator
    if seed: # if '' use python defined seed ~> see: https://docs.python.org/3/library/random.html
        random.seed(seed)
    # populate matrix with 0's
    matrix = [ [j * 0 for j in range(cols)] for i in range(rows) ]
    # populate matrix of i rows and j columns with 0's and *'s
    for i in range(rows):
        for j in range(cols):
            matrix[i][j] = ALIVE if random.randint(0, 1) else DEAD
    return matrix

def build(matrix, rows, cols, seed, _100th_step=100):
    print('\nStarting Cellular Matrix ⚡☄️💨🚀')
    draw(matrix, cols)
    while _100th_step > 0:
        next_matrix = init(rows, cols, seed)
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
            if neighbor_row == x_index and neighbor_col == y_index:
                continue # cell shouldn't count itself as neighbor
            elif neighbor_row < 0 or neighbor_row >= total_number_of_rows:
                continue
            elif neighbor_col < 0 or neighbor_col >= total_number_of_cols:
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
    # TODO: instead of printing to the terminal, save to file
    header = "==** Game of life **=="
    footer = "==** .. **=="
    print(f"\n\t{header:^{width}}")
    for el in matrix:
        print(f"\t{''.join(el)}")
    print(f'\t{footer:^{width}}')

if __name__ == '__main__':
    print("let's generate a cellular matrix 🎲 📌\n")
    q = 'yes'
    while q.lower() not in ('n', 'no') :
        try:
            rows = int(input('Number of rows: '))
            columns = int(input('Number of columns: '))
            seed = input("Seed (or leave empty if you want to use the system generarted seed): ")
            # TODO: validate rows and columns
            matrix = init(rows, columns, seed)
            build(matrix, rows, columns, seed)
        except ValueError as e: # TODO: catch any other error/exception that may be thrown
            print(f'An error occurred - {e}\nPlease try again..')
        finally:
            q = input('Would you like to generate another cellular matrix [Y/N]?: ')
    print("🎆🎉🎇 Thank you for using the program 🎆🎉🎇")
