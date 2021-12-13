# Python version: 3.9.6


def get_positions(filename: str) -> list[int]:
    """
    Takes the filename of the puzzle to read
    and returns a list of the content parsed to integer.
    """
    with open(filename) as f:
        return [int(x) for x in f.readline().rstrip().split(",")]


def count_frequencies(array: list) -> tuple[tuple[int]]:
    """
    Takes an array with the positions in the puzzle
    and returns a tuple with the elements of the array without
    repetition and a tuple with the count of the respective position
    at each index.
    """
    N: int = len(array)
    range_N = range(N)
    visited: list[bool] = [False for i in range_N]

    frequencies: list[int] = []

    for i in range_N:
        if visited[i]:
            continue

        count: int = 1
        for j in range(i+1, N):
            if array[i] == array[j]:
                visited[j] = True
                count += 1
        frequencies.append(count)
    return tuple(set(array)), tuple(frequencies)


def calculate_fuel_at_constant_rate(
        positions: list[int],
        align_position: int) -> int:
    """
    Calculates the fuel spent to move all the crabs to the
    specified align_position when every movement costs 1 fuel unit.
    """
    total_fuel: int = 0
    for i in positions:
        total_fuel += abs(align_position-i)
    return total_fuel


def calculate_minimum_fuel_at_constant_rate(
        positions_original: list[int]) -> tuple[int]:
    """
    Calculates the position at where the fuel consumption is
    minimum to move every crab to and returns that minimum
    fuel amount and the position.

    The fuel consumption is constant and costs 1 fuel unit.
    """
    # tuple[0] -> minimum fuel
    # tuple[1] -> position of minimum fuel

    # Fuel_j = Fuel_{j-1} + sum{0,j-1}(freq_j) - sum{j,N}(freq_j)
    positions_original.sort()
    positions, frequencies = count_frequencies(positions_original)

    # print(f"{positions = }")
    # print(f"{frequencies = }")

    j: int = 0

    sum_previous_frequencies: int = 0
    current_frequency: int = frequencies[0]
    sum_next_frequencies: int = sum(frequencies[1:])
    total_frequencies: int = len(positions_original)

    # print(f"{sum_previous_frequencies = }")
    # print(f"{sum_next_frequencies = }")

    F_j: int = calculate_fuel_at_constant_rate(positions_original, j)
    # print(f"F_0= {F_j}")

    # print(f"{F_j = }")
    min_fuel: int = F_j
    min_fuel_position_index: int = 0

    lpwfi: int = 0  # last position with frequency index

    # for j in range(1, positions_original[-1]-1):
    j = 1
    while j <= positions_original[-1]:
        if j > positions[lpwfi] and j < positions[lpwfi+1]:
            current_frequency = 0
            sum_previous_frequencies = total_frequencies - sum_next_frequencies
        else:
            current_frequency = frequencies[lpwfi+1]
            sum_next_frequencies -= current_frequency
            sum_previous_frequencies = total_frequencies - sum_next_frequencies - current_frequency
            lpwfi += 1
        F_j = F_j - sum_next_frequencies + sum_previous_frequencies - current_frequency
        # print(f"F_{j}= {F_j}")
        if F_j < min_fuel:
            min_fuel = F_j
            min_fuel_position_index = j
        j += 1

    return min_fuel, min_fuel_position_index
    # print(f"{min_fuel = }")


def calculate_fuel_at_growing_rate(
        positions: list[int],
        align_position: int) -> int:
    total_fuel: int = 0
    # sum_all: int = 0
    distance: int = 0
    for i in positions:
        distance = abs(i-align_position)
        total_fuel += (1+distance)*distance//2
    print(total_fuel)


def calculate_minimum_fuel_at_growing_rate(
        positions_original: list[int]) -> tuple[int]:
    pass


def main():
    positions: list[int] = get_positions("sample_puzzle.txt")
    # positions: list[int] = get_positions("input_puzzle.txt")
    # minimum_fuel, position = calculate_minimum_fuel_at_constant_rate(
    # positions)
    # print(f"{minimum_fuel = }")
    # print(f"{position = }")

    calculate_fuel_at_growing_rate(positions, 2)
    calculate_fuel_at_growing_rate(positions, 3)
    calculate_fuel_at_growing_rate(positions, 5)
    # print(*count_frequencies(positions), sep="\n")
    # for i in range(0, max(positions)+1):
    # print(f"F_{i} = {calculate_fuel(positions,i)}")
    # print(calculate_fuel(positions, 7))
    # print(calculate_fuel(positions, 10))
    # print(calculate_fuel(positions, 5))
    # print(calculate_fuel(positions, 10))


main()
