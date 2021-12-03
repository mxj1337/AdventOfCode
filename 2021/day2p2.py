"""Submarine movement"""
def main():
    """Calculating submarines' depth and horizontal position - which now depends on aim"""
    with open("2021/day2.txt", 'r', encoding='utf-8') as file:
        depth, length, aim = 0, 0, 0
        while True:
            cmd = str.split(file.readline())
            if not cmd:
                break

            if cmd[0] == "forward":
                length += int(cmd[1])
                depth += aim * int(cmd[1])
            elif cmd[0] == "down":
                aim += int(cmd[1])
            else:
                aim -= int(cmd[1])
            #print("we're flying") if depth < 0  else None
    print(depth, length, depth*length)

if __name__ == "__main__":
    main()
    