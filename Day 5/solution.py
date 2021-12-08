def get_coordinates_from_line(line: str) -> tuple[tuple[int, int],
                                                  tuple[int, int]]:
    numbers = line.split()
    coordinates_1 = tuple([int(i) for i in numbers[0].split(",")])
    coordinates_2 = tuple([int(i) for i in numbers[2].split(",")])
    return coordinates_1, coordinates_2


def grow_matrix(
        matrix: list[list[int]],
        current_coordinates: tuple
        [tuple[int, int],
         tuple[int, int]]) -> None:

    x_len = max(current_coordinates[0][0],
                current_coordinates[1][0])
    y_len = max(current_coordinates[0][1],
                current_coordinates[1][1])
    while len(matrix) < y_len + 1:
        matrix.append([])
    for row in matrix:
        while len(row) < x_len + 1:
            row.append(".")


def mark_lines_in_matrix(
        matrix: list[list[int]],
        current_coordinates: tuple) -> int:
    sub_counter = 0
    grow_matrix(matrix, current_coordinates)
    if current_coordinates[0][0] == current_coordinates[1][0]:
        """ Vertical line """
        x = current_coordinates[0][0]
        rango = range(
            min(current_coordinates[0][1],
                current_coordinates[1][1]),
            max(
                current_coordinates[0][1],
                current_coordinates[1][1])+1)
        for i in rango:
            if matrix[i][x] == ".":
                matrix[i][x] = 1
            else:
                matrix[i][x] += 1
                if matrix[i][x] == 2:
                    sub_counter += 1
    elif current_coordinates[0][1] == current_coordinates[1][1]:
        """ Horizontal line """
        y = current_coordinates[0][1]
        rango = range(
            min(current_coordinates[0][0],
                current_coordinates[1][0]),
            max(
                current_coordinates[0][0],
                current_coordinates[1][0])+1)
        for i in rango:
            if matrix[y][i] == ".":
                matrix[y][i] = 1
            else:
                matrix[y][i] += 1
                if matrix[y][i] == 2:
                    sub_counter += 1

    # PART TWO STUFF
    delta_x = current_coordinates[1][0] - current_coordinates[0][0]
    delta_y = current_coordinates[1][1] - current_coordinates[0][1]
    if abs(delta_x) == abs(delta_y):
        """ diagonal line """
        y_min = min(
            current_coordinates[0][1],
            current_coordinates[1][1])
        y_max = max(
            current_coordinates[0][1],
            current_coordinates[1][1])

        x_start = min(
            current_coordinates[0][0],
            current_coordinates[1][0])

        rango_y = None
        if delta_x * delta_y > 0:
            rango_y = range(y_min, y_max+1)
        elif delta_x * delta_y < 0:
            rango_y = range(y_max, y_min - 1, -1)
        j = x_start
        for i in rango_y:
            if matrix[i][j] == ".":
                matrix[i][j] = 1
            else:
                matrix[i][j] += 1
                if matrix[i][j] == 2:
                    sub_counter += 1
            j += 1

    return sub_counter


def print_matrix(matrix: list[list[int]]) -> None:
    print("---------- Matrix -----------")
    print('\n'.join(
        [' '.join([str(cell) for cell in row])
         for row in matrix]), sep="")
    print("-----------------------------")


matrix: list[list[int]] = []

# with open("sample_puzzle.txt") as f:
with open("input_puzzle.txt") as f:
    counter = 0
    try:
        for line in f:
            current_coordinates = get_coordinates_from_line(line)
            # print(f"{current_coordinates = }")
            mark_lines_in_matrix(matrix, current_coordinates)
        # print_matrix(matrix)
        for i in matrix:
            for j in i:
                if j != "." and j >= 2:
                    counter += 1
        print(f"{counter = }")

    except IndexError as e:
        print(e)
        print(f"Error ocurred at {current_coordinates = }")
