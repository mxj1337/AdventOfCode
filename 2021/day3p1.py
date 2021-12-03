"""Calculating power consumption of the submarine"""
def main():
    """Calculating gamma and epsilon rate"""
    with open("2021/day3.txt", 'r', encoding='utf-8') as file:
        gamma_counter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        gamma = []
        epsilon = []
        lines = file.read().splitlines()

        for line in lines:
            for i in range(12):
                gamma_counter[i] += int(line[i])

        for i in range(12):
            if gamma_counter[i] < (len(lines) // 2):
                gamma.append("0")
                epsilon.append("1")
            else:
                gamma.append("1")
                epsilon.append("0")
        print(gamma, epsilon)

    print(int("".join(gamma), 2), int("".join(epsilon), 2), int("".join(gamma), 2) * int("".join(epsilon), 2))
if __name__ == "__main__":
    main()
    