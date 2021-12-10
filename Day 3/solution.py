from typing import Union


def generate_rates(filename: str) -> tuple[int]:
    # tuple[0] -> gamma rate
    # tuple[1] -> epsilon rate
    # tuple[2] -> oxygen rate
    # tuple[3] -> co2 rate
    total_inputs: int = 0
    count_1_bits: list[int] = []

    inputs: list[str] = []

    with open(filename) as f:
        binary: str = f.readline().rstrip()
        count_1_bits = [0]*len(binary)
        f.seek(0)
        for line in f:
            total_inputs += 1
            binary = line.rstrip()
            inputs.append(binary)

            for i, v in enumerate(binary):
                if v == "1":
                    count_1_bits[i] += 1

    gamma_rate: list[str] = []
    epsilon_rate: list[str] = []
    for x in count_1_bits:
        if x > total_inputs - x:
            gamma_rate.append("1")
            epsilon_rate.append("0")
        elif x < total_inputs - x:
            gamma_rate.append("0")
            epsilon_rate.append("1")

    gamma_rate = int("".join(gamma_rate), base=2)
    epsilon_rate = int("".join(epsilon_rate), base=2)
    oxygen_rate, co2_rate = generate_oxygen_co2_rates(inputs)
    return gamma_rate, epsilon_rate, oxygen_rate, co2_rate


def get_most_common_bit(
        values: list[str],
        position: int) -> Union[int, str]:
    """ Returns "1" if MCB is "1",
    "0" if MCB is "0",
    end -1 if quantities are the same """
    count_1: int = 0
    count_0: int = 0
    for i in values:
        if i[position] == "1":
            count_1 += 1
        elif i[position] == "0":
            count_0 += 1
    if count_0 > count_1:
        return "0"
    if count_0 < count_1:
        return "1"
    return -1  # equal count


def generate_oxygen_co2_rates(values: list[str]) -> tuple[int]:
    # tuple[0] -> oxygen generator rating
    # tuple[1] -> CO2 scrubber rating

    oxygen_rating: list[str] = values.copy()
    co2_rating: list[str] = values

    indexes_to_remove_oxygen: list[int] = []
    indexes_to_remove_co2: list[int] = []

    position: int = -1

    while len(oxygen_rating) > 1:
        position += 1
        MCB = get_most_common_bit(oxygen_rating, position)
        for i, v in enumerate(oxygen_rating):
            if MCB == -1:
                if v[position] == "0":
                    indexes_to_remove_oxygen.append(i)
            elif v[position] != MCB:
                indexes_to_remove_oxygen.append(i)
        for j in reversed(indexes_to_remove_oxygen):
            oxygen_rating.pop(j)
        indexes_to_remove_oxygen.clear()

    position = -1

    while len(co2_rating) > 1:
        position += 1
        MCB = get_most_common_bit(co2_rating, position)
        for i, v in enumerate(co2_rating):
            if MCB == -1:
                if v[position] == "1":
                    indexes_to_remove_co2.append(i)
            elif v[position] == MCB:
                indexes_to_remove_co2.append(i)
        for j in reversed(indexes_to_remove_co2):
            co2_rating.pop(j)
        indexes_to_remove_co2.clear()

    return int(oxygen_rating[0], base=2), int(co2_rating[0], base=2)


def main():
    try:
        # rates = generate_rates("sample_puzzle.txt")
        rates = generate_rates("input_puzzle.txt")
        power_consumption: int = rates[0]*rates[1]
        life_support: int = rates[2]*rates[3]
        print(f"{power_consumption = }")
        print(f"{life_support = }")
    except Exception as e:
        print(e)


main()
