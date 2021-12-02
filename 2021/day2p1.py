def main():
    with open("2021/day2.txt", 'r', encoding='utf-8') as file:
        depth = 0
        length = 0
        while True:
            cmd = str.split(file.readline())
            if not cmd:
                break

            if cmd[0] == "forward":
                length += int(cmd[1])
            elif cmd[0] == "down":
                depth += int(cmd[1])
            else:
                depth -= int(cmd[1])
            print("we're flying") if depth < 0  else None
    print(depth, length, depth*length)

if __name__ == "__main__":
    main()
    