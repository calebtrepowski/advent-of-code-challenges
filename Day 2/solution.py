def part_one(filename: str) -> int:
    position: list[int, int] = [0, 0]
    with open(filename) as f:
        for line in f:
            movement = line.rstrip().split()
            movement[1] = int(movement[1])
            if movement[0] == "forward":
                position[0] += movement[1]
            elif movement[0] == "down":
                position[1] += movement[1]
            elif movement[0] == "up":
                position[1] -= movement[1]

    return position[0]*position[1]


def part_two(filename: str) -> int:
    position: list[int, int] = [0, 0]
    aim: int = 0
    with open(filename) as f:
        for line in f:
            movement = line.rstrip().split()
            movement[1] = int(movement[1])
            if movement[0] == "forward":
                position[0] += movement[1]
                position[1] += aim*movement[1]
            elif movement[0] == "down":
                aim += movement[1]
            elif movement[0] == "up":
                aim -= movement[1]

    return position[0]*position[1]


try:
    # part_one_result: int = part_one("sample_puzzle.txt")
    part_one_result: int = part_one("input_puzzle.txt")
    print(f"{part_one_result = }")
    # part_two_result: int = part_two("sample_puzzle.txt")
    part_two_result: int = part_two("input_puzzle.txt")
    print(f"{part_two_result = }")
except Exception as e:
    print(e)
