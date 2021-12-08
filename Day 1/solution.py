def part_one(filename: str) -> int:
    with open(filename) as f:
        counter: int = 0
        prev_value: int = int(f.readline().rstrip())
        for line in f:
            actual_value: int = int(line.rstrip())
            if actual_value > prev_value:
                counter += 1
            prev_value = actual_value
        return counter


def part_two(filename: str) -> int:
    with open(filename) as f:
        counter: int = 0
        values = []

        while len(values) < 3:
            values.append(int(f.readline().rstrip()))
        prev_value: int = sum(values)
        for line in f:
            values.append(int(line.rstrip()))
            values.pop(0)
            actual_value: int = sum(values)
            if actual_value > prev_value:
                counter += 1
            prev_value = actual_value
    return counter


try:
    # part_one_result = part_one("sample_puzzle.txt")
    part_one_result = part_one("input_puzzle.txt")
    print(f"{part_one_result = }")

    part_two_result = part_two("input_puzzle.txt")
    # part_two_result = part_two("sample_puzzle.txt")
    print(f"{part_two_result = }")
except Exception as e:
    print(e)
