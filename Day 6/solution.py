# DAYS: int = 18
# DAYS: int = 80
DAYS: int = 256


def get_initial_states(filename: str) -> list[int]:
    with open(filename) as f:
        return [int(x) for x in f.readline().rstrip().split(",")]


def get_fish_amount_brute(states: list[int]) -> int:
    new_fishes: int = 0
    for day in range(0, DAYS):
        i: int = 0
        while i < len(states):
            if states[i] == 0:
                new_fishes += 1
                states[i] = 6
            else:
                states[i] -= 1
            i += 1
        if new_fishes > 0:
            for i in range(new_fishes):
                states.append(8)
            new_fishes = 0
    return len(states)


def get_fish_amount_efficient(states: list[int]) -> int:
    amounts: list[int] = [0]*9
    # position 0 -> 0 days
    # position 1 -> 1 days
    # and so on
    for i in states:
        amounts[i] += 1
    day: int = DAYS
    while day > 0:
        amount_with_zero_days: int = amounts[0]
        del amounts[0]
        amounts.append(amount_with_zero_days)
        amounts[6] += amount_with_zero_days
        day -= 1
    return sum(amounts)


def main():
    # states: list[int] = get_initial_states("sample_puzzle.txt")
    states: list[int] = get_initial_states("input_puzzle.txt")

    # print(f"total lanternfish after {DAYS} days:",
    #       get_fish_amount_brute(states))
    print(f"total lanternfish after {DAYS} days:",
          get_fish_amount_efficient(states))


main()
