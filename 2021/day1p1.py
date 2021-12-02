"""Counts how many times the depth has increased.   """
def main():
    """Counts how many times the depth has increased.   """
    with open("2021/day1.txt", 'r', encoding='utf-8') as file:
        prev = file.readline()
        count = 0
        while True:
            depth = file.readline()
            count = count+1 if depth > prev else count
            prev = depth
            if not depth:
                break

    print(count)
if __name__ == "__main__":
    main()
    