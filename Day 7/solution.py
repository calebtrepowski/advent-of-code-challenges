""" 
Python version: 3.9.6
"""


def calculate_best_align_position(positions: list[int]) -> int:

    fuel_amounts: list[int] = []

    fuel: int = 0
    position: int = 0

    positions_with_frequency = Counter(positions)
    return calculate_fuel(
        positions, positions_with_frequency.most_common()[0][0])
    # while len(fuel_amounts) < len(positions):
    #     fuel = 0
    #     for i in positions:
    #         fuel += calculate_fuel(positions, position)
    #     fuel_amounts.append(fuel)
    #     position += 1

    # return fuel_amounts.index(min(fuel_amounts))


def calculate_fuel(positions: list[int], align_position: int) -> int:
    total_fuel: int = 0
    for i in positions:
        total_fuel += abs(align_position-i)
    return total_fuel


def calculate_minimum_fuel(positions_original: list[int]) -> int:
    # Fuel_n = Fuel_{n-1} + sum{0,n-1}(freq_j) - sum{n,N}(freq_j)
    positions_original.sort()
    positions, frequencies = count_frequencies(positions_original)

    # print(f"{positions = }")
    # print(f"{frequencies = }")

    n: int = 0

    sum_previous_frequencies: int = 0
    current_frequency: int = frequencies[0]
    sum_next_frequencies: int = sum(frequencies[1:])
    total_frequencies: int = len(positions_original)

    # print(f"{sum_previous_frequencies = }")
    # print(f"{sum_next_frequencies = }")

    F_j: int = calculate_fuel(positions_original, n)
    # print(f"F_0= {F_j}")

    # print(f"{F_j = }")
    min_fuel: int = F_j
    min_fuel_position_index: int = 0

    lpwfi: int = 0  # last position with frequency index

    # for j in range(1, positions_original[-1]-1):
    j: int = 1
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


def get_positions(filename: str) -> list[int]:
    with open(filename) as f:
        return [int(x) for x in f.readline().rstrip().split(",")]


def count_frequencies(array: list) -> tuple[tuple[int]]:
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


def main():
    # positions: list[int] = get_positions("sample_puzzle.txt")
    positions: list[int] = get_positions("input_puzzle.txt")
    minimum_fuel, position = calculate_minimum_fuel(positions)
    print(f"{minimum_fuel = }")
    print(f"{position = }")
    # for i in range(0, max(positions)+1):
    # print(f"F_{i} = {calculate_fuel(positions,i)}")
    # print(calculate_fuel(positions, 7))
    # print(calculate_fuel(positions, 10))
    # print(calculate_fuel(positions, 5))
    # print(calculate_fuel(positions, 10))


main()
